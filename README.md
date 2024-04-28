# Airflow DBT Project

This repo I built as a documentation of my learning about data engineering. Here I try to build a data pipeline where data is sourced from one csv which will later be extracted into several new tables which aim to facilitate analysis. This project serves as a practical showcase of the capabilities of these powerful tools in orchestrating data workflows and performing analytics tasks.

# Key Components
1. **Apache Airflow**: As the backbone of our project, Apache Airflow provides a flexible and scalable platform for defining, scheduling, and monitoring data pipelines. Through its intuitive interface, users can easily create workflows to automate data processing tasks.
2. **Google BigQuery**: Leveraging the cloud-native data warehouse capabilities of Google BigQuery, our project demonstrates how to store, query, and analyze large datasets efficiently. With its serverless architecture and SQL-like syntax, BigQuery simplifies the process of deriving insights from your data.
3. **dbt (data build tool)**: dbt empowers us to transform and model our data in a scalable and reproducible manner. With dbt's SQL-based approach to data transformation, we can define data models, run tests, and document our analytics workflows effectively.

# Project Overview
In this project, we showcase a comprehensive data pipeline that incorporates the following key steps:

* Data ingestion: Raw data is ingested from various sources into Google BigQuery using Apache Airflow operators.
* Data transformation: Using dbt, we define SQL-based transformations to clean, enrich, and model the raw data into structured analytics tables.
* Data analysis: Leveraging BigQuery's powerful SQL querying capabilities, we perform analytics and derive insights from the transformed data.
* Workflow orchestration: Apache Airflow schedules and executes the pipeline tasks, ensuring data processing tasks are executed in a timely and efficient manner.

# How to Use
To explore this project, refer to the provided documentation or setup instructions for guidance on configuring Airflow DAGs, dbt models, and connecting to BigQuery. Follow the step-by-step instructions to run the data pipeline and analyze the results. 
## Installing Dependencies
As we mention before, there are some key tools/dependencies that we need to install
### Apache Airflow
Follow the instructions in [apache aiflow](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) installing guide. We recommend to install docker and docker compose first before installing airflow.

NOTE: while you following the instruction, make a folder named `include`. It will stored some data that will use in the project like `dataset.csv` and `service_account.json` for connect to bigquery.
### Airflow Google Providers 