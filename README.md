# Sales Data ETL Pipeline using Databricks

## Project Overview
This project implements an end-to-end ETL pipeline for processing sales data using Databricks and PySpark. 
The pipeline follows the Medallion Architecture (Bronze, Silver, Gold) for scalable and reliable data processing.

## Business Problem
Organizations generate large volumes of sales data daily. 
This project demonstrates how to ingest, clean, transform, and analyze sales data efficiently using modern data engineering tools.

## Technologies Used
- Databricks
- PySpark
- Spark SQL
- Delta Lake
- Python
- SQL

## Architecture
Raw Data → Bronze Layer → Silver Layer → Gold Layer → Business Reports

## Features
- Data ingestion from raw sources
- Data cleaning and transformation
- Deduplication of records
- Revenue calculations
- Delta Lake storage with ACID compliance
- Business report generation using Spark SQL
