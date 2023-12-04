CREATE SCHEMA IF NOT EXISTS job_it;

DROP TABLE IF EXISTS job_it.job;
CREATE TABLE job_it.job (
    job_id SERIAL,
    job_title VARCHAR(512) NOT NULL,
    salary_range VARCHAR(512),
    salary_min FLOAT,
    salary_max FLOAT,
    currency_unit VARCHAR(3),
    address TEXT,
    time_deadline VARCHAR(10),
    rank VARCHAR(50),
    experience INT,
    number_of_recruits INT, 
    working_form VARCHAR(70),
    sex VARCHAR(50),
    company_name VARCHAR(512) NOT NULL,
    description TEXT,
    requirements TEXT,
    benefit TEXT,
    link_job VARCHAR(512),
    is_remote BOOLEAN DEFAULT false,
    PRIMARY KEY (job_id)
);

DROP TABLE IF EXISTS job_it.company_info;
CREATE TABLE job_it.company_info (
    company_id SERIAL,
    job_id SERIAL,
    company_name VARCHAR(255),
    size VARCHAR(70),
    address VARCHAR(150),
    web VARCHAR(70),
    introduction TEXT,
    url_company VARCHAR(170),
    PRIMARY KEY (company_id)
);

ALTER TABLE job_it.company_info
ADD CONSTRAINT fk_job_it_job
FOREIGN KEY (job_id)
REFERENCES job_it.job(job_id)

