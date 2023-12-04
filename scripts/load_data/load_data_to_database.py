from dotenv import load_dotenv
import pandas as pd
import psycopg2
import os


load_dotenv()

job_data = '/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/data/processed_data/results.csv'
company_data = '/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/data/processed_data/company.csv'

# Thông tin kết nối đến PostgreSQL
db_params = {
    'host': '127.0.0.1',
    'port': 5432,
    'user': 'postgres',
    'password': os.getenv('PASSWORD'),
    'database': 'postgres'
}

def load_data_to_database(processed_data: str, table_name: str) -> None:
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        data = pd.read_csv(processed_data)

        for index, row in data.iterrows():
            # Câu lệnh SQL INSERT
            insert_sql = f'''
            INSERT INTO {table_name} (job_title, salary_range, salary_min, salary_max, currency_unit, 
            address, time_deadline, rank, experience, number_of_recruits, working_form, sex, company_name, 
            description, requirements, benefit, link_job)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            '''
            # Thực hiện lệnh INSERT với giá trị từ mỗi hàng của DataFrame
            cur.execute(insert_sql, tuple(row))

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        conn.commit()
        conn.close()

load_data_to_database(job_data, 'job_it.job')