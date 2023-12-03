from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os


default_args: dict = {
    'owner': 'A44306',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag: DAG = DAG(
    dag_id='crawl_process_data_dag',
    default_args=default_args,
    description='a DAG simple for project of data engineer!!!!',
    schedule_interval=timedelta(days=1),
)

def crawl_data() -> None:
    crawl_data_script_path: str='/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/scripts/JobITScraper/JobITScraper/spiders/jobITSpider.py'
    os.system(f"python {crawl_data_script_path}")

def preprocessing_data() -> None:
    process_data_script_path: str='/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/scripts/process_data.py'
    os.system(f"python {process_data_script_path}")

def load_data_to_database() -> None:
    load_data_scripts_path=''
    os.system(f"python {load_data_scripts_path}")

crawl_data_task = PythonOperator(task_id="crawl_data_task", python_callable=crawl_data, dag=dag)
preprocess_data_task = PythonOperator(task_id="pre-process_data_task", python_callable=preprocessing_data, dag=dag)
load_data_task = PythonOperator(task_id="load_data_task", python_callable=load_data_to_database, dag=dag)

crawl_data_task >> preprocess_data_task >> load_data_task