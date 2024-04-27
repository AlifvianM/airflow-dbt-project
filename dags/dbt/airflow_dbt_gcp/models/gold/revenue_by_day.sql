{{
    config(
        materialized='view',
        schema='finance'
    )
}}

SELECT 
    InvoiceDate,
    count(InvoiceNo) as total_order,
    sum(quantity * unitprice) as total_price
from {{source('airflow_dbt', 'retail')}}
group by 1
order by 1 desc
