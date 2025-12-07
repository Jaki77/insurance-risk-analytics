# Insurance Risk Analytics --- 10 Academy KAIM Week 3

## Overview

This repository contains my work for **10 Academy's KAIM Week 3
Challenge**:\
**End-to-End Insurance Risk Analytics & Predictive Modeling**.

The objective of the challenge is to analyze real insurance data,
uncover risk patterns, perform hypothesis testing, and build predictive
models to support pricing and marketing decisions.

## Business Objective

AlphaCare Insurance Solutions (ACIS) aims to identify low-risk segments,
optimize premiums, and enhance customer acquisition using data-driven
insights. This project supports those goals through: - Exploratory Data
Analysis (EDA) - A/B Hypothesis Testing - Predictive Modeling - Model
Interpretability (SHAP/LIME) - Reproducible data pipelines (DVC)

## Repository Structure

    INSURANCE-RISK-ANALYTICS/
    ├── data/
    ├── notebooks/
    │   └── eda_analysis.ipynb
    ├── src/
    │   ├── convert_to_parquet.py
    │   └── check_parquet.py
    ├── scripts/
    ├── tests/
    ├── .github/workflows/
    ├── README.md
    ├── requirements.txt
    └── .gitignore

## Tasks Summary

### Task 1 --- EDA + Git/GitHub

-   Modular OOP code for EDA
-   Outlier analysis, distributions, trends
-   3 creative plots

### Task 2 --- Data Version Control (DVC)

-   Initialize DVC
-   Configure local remotes
-   Track large datasets
-   Version dataset changes

### Task 3 --- A/B Hypothesis Testing

Tests include: 1. Risk differences across provinces 2. Risk differences
across postal codes 3. Margin differences between postal codes 4.
Gender-based risk differences

### Task 4 --- Predictive Modeling

Models: - Linear Regression - Random Forest - XGBoost

Includes: - Claim severity prediction - Premium optimization - SHAP/LIME
interpretability

## How to Run

### Setup Environment

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Run Notebook

    jupyter notebook notebooks/eda_analysis.ipynb

### Run EDA Script

    python src/convert_to_parquet.py

### DVC Commands

    dvc pull
    dvc repro

