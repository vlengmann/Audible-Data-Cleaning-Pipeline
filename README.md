
# Audible Data Pipeline

A production-style data pipeline for ingesting and cleaning Audible audiobook data.

[Data Source](https://www.kaggle.com/datasets/snehangsude/audible-dataset)

---
## Project Timeline
* **Original Completion:** April 2026
* **Github Upload:** April 2026

## Data  

* `name`: Name of title
* `author`: Author of title
* `time`: Length of title
* `releasedate`: Date of release
* `language`: Language of title
* `stars`: Rating of title, this column also includes a rating count
* `price`: Price of title

## Project Overview

This project details a data pipeline centered on data ingestion via zip files and cleaning of files. In the future, visualitation using cloud stystems will be showcased.

## Method and Analysis


This pipeline follows the **Factory design pattern** to separate ingestion and cleaning into 
modular, interchangeable components. An abstract base class defines the contract for each layer, 
with concrete implementations handling the specifics — `ZipDataIngestor` for extracting and 
loading data from compressed files, and `AudibleDataCleaner` for standardizing the dataset. 
Cleaning steps included parsing a composite `stars` column into separate `rating` and 
`rating_count` fields, converting a formatted time string into numeric minutes, stripping 
prefixes from `author` and `narrator` fields, and enforcing consistent data types across 
all columns. The cleaned output is saved to `data/processed/` for downstream analysis.

## Project Structure

Audible/
├── data/              # Raw data
├── notebooks/         # Exploratory data analysis
├── src/
│   ├── main.py        # Pipeline entry point
│   └── utils/
│       ├── data_ingestor.py   # Ingestion layer
│       └── data_cleaner.py    # Cleaning layer
├── environment.yml    # Conda environment
└── README.md
## Pipeline Overview
Raw ZIP -> Ingestor -> Raw DataFrame -> Cleaner -> Cleaned and Final CSV

## Key Features
- Factory design pattern for extensible ingestion and cleaning
- Handles ZIP extraction automatically
- Cleans and standardizes 87,000+ Audible records
- Outputs cleaned CSV ready for analysis or visualization

## Tech Stack
Python, pandas, conda

## How to Run
```bash
conda activate vsproj
python src/main.py
```
