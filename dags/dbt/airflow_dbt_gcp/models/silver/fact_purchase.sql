{{
    config(
        materialized='table',
        tags=['schedule:1d']
    )
}}

SELECT
    StockCode,
    CustomerID,
    InvoiceDate,
    quantity
FROM {{source('airflow_dbt', 'retail')}}
WHERE StockCode IS NOT NULL
AND CustomerID IS NOT NULL