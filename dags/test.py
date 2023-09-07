from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scripts.trigger import hello_world

args = {
    'owner': 'Marcus Lau',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id = 'crm-elastic-dag',
    default_args = args,
    schedule_interval='@daily' # this workflow happens every day
)

with dag:
    hello_world = PythonOperator(
        task_id = 'hello_world',
        python_callable=hello_world
    )