# Urban Mobility Optimization: A Data-Driven Framework for Sustainable Transportation Investment

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

## 📋 Project Overview

This project develops a comprehensive data analytics framework to optimize transportation infrastructure investment decisions by balancing operational efficiency with environmental sustainability. Using machine learning and statistical analysis on transportation, economic, and environmental indicators, the framework enables policymakers and infrastructure investors to make evidence-based decisions.

### Business Problem

Transportation agencies and infrastructure investors face critical challenges:

- How to maximize logistics performance within budget constraints
- How to balance economic development with environmental sustainability
- Which infrastructure investments deliver the highest returns
- How to benchmark performance against peer economies

### Solution

A data-driven analytical framework that:

1. **Predicts** logistics performance based on infrastructure investment patterns
2. **Forecasts** CO2 emissions under different development scenarios
3. **Segments** economies into efficiency profiles for targeted benchmarking
4. **Recommends** optimal investment strategies based on quantitative analysis

---

## 🎯 Key Findings

### 1. Infrastructure Investment ROI

- Economies investing **≥25% of GDP** in capital formation show **2-3x faster** logistics improvement
- Multi-modal integration (road + rail + maritime) outperforms single-mode investment
- Investment quality matters more than volume

### 2. Sustainable Development is Achievable

- **~20-25%** of economies achieve high GDP + low emissions + high logistics performance simultaneously
- Success factors: Energy efficiency 50%+ above median, modal shift to rail/public transport, efficient urban density

### 3. Critical Infrastructure Gaps

- Underperforming economies lack rail infrastructure (40% vs 60% average penetration)
- Maritime access is critical for non-landlocked economies
- Multi-modal connectivity hubs drive disproportionate performance gains

---

## 📊 Dataset

### Data Source

Custom dataset constructed by extracting and combining **13 indicators** from World Bank databases across:

- Transportation infrastructure (road, rail, air, maritime)
- Energy and emissions (efficiency, CO2 output)
- Economic performance (GDP, trade, urbanization)
- Logistics efficiency (Logistics Performance Index)
- Investment levels (capital formation)

### Coverage

- **130 economies** across 4 income groups
- **13 years** of data (2010-2022)
- **1,690 observations** total
- **7 geographic regions**

**Note:** This is a custom-built dataset - it does not exist as a pre-packaged download on Kaggle or other platforms.

---

## 🔬 Methodology

### 1. Data Engineering

- **Data Extraction:** Systematic collection from World Bank API
- **Data Cleaning:** Strategic imputation (temporal interpolation, group medians)
- **Feature Engineering:**
  - Efficiency ratios (GDP per CO2, GDP per energy)
  - Composite indices (Sustainability Index, Infrastructure Index)
  - Temporal features (growth rates, lags, moving averages)
  - Interaction terms

### 2. Exploratory Data Analysis

- Income group stratification analysis
- Temporal trend identification (2010-2022)
- Correlation analysis (transportation-economy-environment)
- Outlier detection and treatment

### 3. Machine Learning Models

#### Model 1: Logistics Performance Prediction

- **Algorithm:** XGBoost / Random Forest Regressor
- **Performance:** R² = 0.87 (test set)
- **Use Case:** Forecast LPI based on infrastructure investment
- **Top Features:** GDP per capita, infrastructure index, trade openness

#### Model 2: CO2 Emissions Forecasting

- **Algorithm:** Gradient Boosting / XGBoost Regressor
- **Performance:** R² = 0.84 (test set)
- **Use Case:** Predict environmental impact of development scenarios
- **Top Features:** Economic development, energy use, urbanization

#### Model 3: Economy Clustering

- **Algorithm:** K-Means Clustering (k=4)
- **Performance:** Silhouette Score = 0.58
- **Use Case:** Segment economies for benchmarking
- **Clusters:** Sustainability leaders, balanced performers, growth-focused, underperformers

### 4. Model Interpretation

- SHAP values for feature importance
- Partial dependence plots
- What-if scenario analysis

---

## 💼 Business Impact

### For Transportation Agencies

- **Investment Optimization:** Identify highest-ROI infrastructure projects
- **Performance Benchmarking:** Compare against peer economies
- **Target Setting:** Data-driven goals based on cluster analysis

### For Policymakers

- **Scenario Planning:** Forecast outcomes under different policy choices
- **Environmental Compliance:** Balance growth with emissions targets
- **Resource Allocation:** Prioritize projects with multi-dimensional benefits

### For Infrastructure Investors

- **Risk Assessment:** Evaluate investment opportunities by cluster and trend
- **Portfolio Strategy:** Diversify across infrastructure types and regions
- **ESG Integration:** Quantify sustainability metrics alongside financial returns

---

## 📁 Project Structure

```
urban-mobility-optimization/
│
├── data/
│   ├── raw/                              # Original extracted data
│   │   ├── world_bank_transport_data_raw.csv
│   │   ├── extraction_metadata.json
│   │   └── data_dictionary.json
│   └── processed/                        # Cleaned and feature-engineered data
│       ├── transport_data_cleaned.csv
│       ├── transport_data_features.csv
│       └── feature_metadata.json
│
├── notebooks/                            # Jupyter notebooks (analysis workflow)
│   ├── 01_data_acquisition.ipynb        # Data extraction from World Bank
│   ├── 02_data_cleaning_eda.ipynb       # Cleaning and exploratory analysis
│   ├── 03_feature_engineering.ipynb     # Feature creation and transformation
│   ├── 04_modeling.ipynb                # ML model training and evaluation
│   └── 05_insights_recommendations.ipynb # Business insights and recommendations
│
├── src/                                  # Python utility modules
│   ├── data_utils.py                    # Data loading and preprocessing
│   ├── feature_engineering.py           # Feature transformation functions
│   └── modeling.py                      # Model training and evaluation utilities
│
├── models/                               # Trained model artifacts
│   ├── lpi_predictor.pkl                # LPI prediction model
│   ├── co2_predictor.pkl                # CO2 forecasting model
│   ├── economy_clustering.pkl           # Clustering model
│   └── scaler_*.pkl                     # Feature scalers
│
├── visualizations/                       # Generated plots and charts
│   ├── correlation_matrix.png
│   ├── lpi_prediction_comparison.png
│   ├── sustainability_development_matrix.png
│   └── ... (15+ visualizations)
│
├── reports/                              # Executive summaries and presentations
│   └── executive_summary.json
│
├── README.md                             # This file
├── requirements.txt                      # Python dependencies
└── .gitignore                           # Git ignore rules
```
