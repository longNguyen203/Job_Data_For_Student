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

def extract_data() -> None:
    pass

def tranform_data() -> None:
    pass

def load_data() -> None:
    pass

extract_data_task = PythonOperator(task_id="extract_data_task", python_callable=extract_data, dag=dag)
tranform_data_task = PythonOperator(task_id="tranform_data_task", python_callable=tranform_data, dag=dag)
load_data_task = PythonOperator(task_id="load_data_task", python_callable=load_data, dag=dag)

extract_data_task >> tranform_data_task >> load_data_task