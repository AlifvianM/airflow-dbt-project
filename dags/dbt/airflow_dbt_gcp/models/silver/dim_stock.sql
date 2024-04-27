{{
    config(
        materialized='table'
    )
}}


select
    distinct StockCode
from {{ source('airflow_dbt', 'retail') }}