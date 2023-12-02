drop table if exists Job;
create table Job (
    job_id primary key serial,
    job_title varchar(255) not null,
    salary_range varchar(50),
    salary_min float,
    salary_max float,
    currency_unit varchar(3),
    address varchar(255),
    time_deadline timestamp,
    rank varchar(50),
    experience int,
    number_of_recruits int, 
    working_form varchar(70),
    sex varchar(30),
    company_name varchar(255) not null,
    description text,
    requirements text,
    benefit text,
    link_job varchar(255)
    is_remote boolean default false
)

create index idx_job_title on Job(job_title);