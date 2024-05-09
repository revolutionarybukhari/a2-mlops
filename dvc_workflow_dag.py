from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import data_processing

dag = DAG('data_version_control', description='Automated Data Extraction and DVC Workflow',
          schedule_interval='@daily',
          start_date=datetime(2024, 9, 25), catchup=False)

def run_data_processing():
    data_processing.main()

task1 = PythonOperator(task_id='process_data',
                       python_callable=run_data_processing,
                       dag=dag)
