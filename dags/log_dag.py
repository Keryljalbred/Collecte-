from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from ingest import read_logs
from clean import clean_and_transform_logs
from storage import store_cleaned_logs  # ✅ Assure-toi que ce nom est correct

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='log_processing_pipeline',
    default_args=default_args,
    description='Pipeline de traitement des logs',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    def ingest_task(**context):
        logs = read_logs('/opt/airflow/dags/logs.txt')
        context['ti'].xcom_push(key='raw_logs', value=logs)

    def clean_task(**context):
        raw_logs = context['ti'].xcom_pull(key='raw_logs', task_ids='ingest_logs')
        cleaned = clean_and_transform_logs(raw_logs)
        context['ti'].xcom_push(key='cleaned_logs', value=cleaned)

    def store_task(**context):
        cleaned_logs = context['ti'].xcom_pull(key='cleaned_logs', task_ids='clean_logs')
        store_cleaned_logs(cleaned_logs)

    ingest = PythonOperator(
        task_id='ingest_logs',
        python_callable=ingest_task
    )

    clean = PythonOperator(
        task_id='clean_logs',
        python_callable=clean_task
    )

    store = PythonOperator(
        task_id='store_logs',
        python_callable=store_task
    )

    ingest >> clean >> store
