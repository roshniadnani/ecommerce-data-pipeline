# E-commerce Data Engineering Pipeline

An end-to-end, production-style data pipeline built using:

- Snowflake
- Snowpark (Python)
- dbt
- Apache Airflow

## Architecture

Raw E-commerce data → Snowflake (raw layer) → dbt (staging & marts)
→ Snowpark Python models → Airflow orchestration

## Goals

- Demonstrate modern data engineering practices
- Build analytics-ready fact and dimension tables
- Automate transformations with Airflow
