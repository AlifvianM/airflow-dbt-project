import os
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

CURRENT_DIR = os.getcwd()
# DBT_DIR = os.path.join(CURRENT_DIR,"/dags/dbt/airflow_dbt_gcp/")
DBT_DIR = CURRENT_DIR + "/dags/dbt/airflow_dbt_gcp"

print("CURRENT_DIR :", CURRENT_DIR)
print("DBT_DIR :",DBT_DIR)

with DAG(
    "dbt_dag_gcp",
    start_date=datetime(2024, 1, 1),
    description="Sample DAG for DBT",
    schedule='@daily'
):
    def get_dbt_dir(**kwargs):
        dir = [CURRENT_DIR,DBT_DIR]
        return dir
    
    push_dir = PythonOperator(
        task_id = "get_dir_dbt",
        python_callable=get_dbt_dir
    )

    run_dbt = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt run --profiles-dir ."
    )

    test_dbt = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt run --profiles-dir ."
    )

    push_dir >> run_dbt >> test_dbt