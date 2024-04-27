from airflow.decorators import dag, task
import pandas as pd
from airflow import DAG
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


with DAG(
    dag_id="retail_dag",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False,
    # tags=['retail']
):
    
    upload_csv_to_gcp = LocalFilesystemToGCSOperator(
        task_id="upload_csv_to_gcp",
        src="/opt/airflow/include/dataset/online_retail.csv",
        dst="raw/online_retail.csv",
        bucket="marco_airflow_online_retail",
        gcp_conn_id="gcp",
        mime_type='text/csv'
    )

    create_retail_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id = "create_retail_dataset",
        dataset_id="retail",
        gcp_conn_id="gcp"
    )

    retail_csv_to_dataset = GCSToBigQueryOperator(
        task_id = "send_retail_to_dataset",
        gcp_conn_id="gcp",
        # bigquery_conn_id="gcp",
        bucket="marco_airflow_online_retail",
        source_objects=["raw/online_retail.csv"],
        destination_project_dataset_table=f'airflow-tutorial-418113.retail.retail',
        write_disposition='WRITE_TRUNCATE',
        autodetect=True,
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
            {'name':'InvoiceNo', 'type':'STRING'},
            {'name':'StockCode', 'type':'STRING'},
            {'name':'Description', 'type':'STRING', 'mode':'NULLABLE'},
            {'name':'Quantity', 'type':'INTEGER'},
            {'name':'InvoiceDate', 'type':'DATETIME'},
            {'name':'UnitPrice', 'type':'FLOAT'},
            {'name':'CustomerID', 'type':'FLOAT', 'mode':'NULLABLE'},
            {'name':'Country', 'type':'STRING'}
        ]
    )

    upload_csv_to_gcp >> create_retail_dataset >> retail_csv_to_dataset