"""
Data Utilities Module
Urban Mobility Optimization Project

Functions for data loading, preprocessing, and validation.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# File paths
DATA_DIR = Path(__file__).parent.parent / 'data'
RAW_DATA_PATH = DATA_DIR / 'raw' / 'world_bank_transport_data_raw.csv'
PROCESSED_DATA_PATH = DATA_DIR / 'processed' / 'transport_data_features.csv'


def load_raw_data():
    """
    Load raw transportation dataset.
    
    Returns:
    --------
    pd.DataFrame
        Raw dataset with all original indicators
    """
    try:
        df = pd.read_csv(RAW_DATA_PATH)
        print(f"✓ Raw data loaded: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"✗ Error: Raw data file not found at {RAW_DATA_PATH}")
        return None


def load_processed_data():
    """
    Load feature-engineered dataset ready for modeling.
    
    Returns:
    --------
    pd.DataFrame
        Processed dataset with engineered features
    """
    try:
        df = pd.read_csv(PROCESSED_DATA_PATH)
        print(f"✓ Processed data loaded: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"✗ Error: Processed data file not found at {PROCESSED_DATA_PATH}")
        return None


def get_latest_year_data(df, year=None):
    """
    Extract data for the most recent year (or specified year).
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with year column
    year : int, optional
        Specific year to extract. If None, uses most recent.
    
    Returns:
    --------
    pd.DataFrame
        Filtered dataframe for specified year
    """
    if year is None:
        year = df['year'].max()
    
    df_filtered = df[df['year'] == year].copy()
    print(f"✓ Extracted {len(df_filtered)} records for year {year}")
    return df_filtered


def validate_data_quality(df, threshold=0.5):
    """
    Check data quality and flag high-missingness columns.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    threshold : float
        Maximum acceptable missing percentage (default 0.5)
    
    Returns:
    --------
    dict
        Data quality report
    """
    quality_report = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'total_missing': df.isnull().sum().sum(),
        'missing_pct': (df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100,
        'high_missing_columns': []
    }
    
    # Identify high-missing columns
    for col in df.columns:
        missing_pct = (df[col].isnull().sum() / len(df))
        if missing_pct > threshold:
            quality_report['high_missing_columns'].append({
                'column': col,
                'missing_pct': round(missing_pct * 100, 2)
            })
    
    print(f"Data Quality Report:")
    print(f"  Total Missing: {quality_report['total_missing']} ({quality_report['missing_pct']:.2f}%)")
    print(f"  High-Missing Columns: {len(quality_report['high_missing_columns'])}")
    
    return quality_report


def filter_by_income_group(df, income_groups):
    """
    Filter dataset by income group(s).
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    income_groups : str or list
        Income group(s) to filter ('High income', 'Upper middle income', etc.)
    
    Returns:
    --------
    pd.DataFrame
        Filtered dataframe
    """
    if isinstance(income_groups, str):
        income_groups = [income_groups]
    
    df_filtered = df[df['income_group'].isin(income_groups)].copy()
    print(f"✓ Filtered to {len(df_filtered)} records for income groups: {income_groups}")
    return df_filtered


def calculate_growth_rate(df, column, groupby_col='economy'):
    """
    Calculate year-over-year growth rates.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe (must be sorted by economy and year)
    column : str
        Column to calculate growth for
    groupby_col : str
        Grouping column (default 'economy')
    
    Returns:
    --------
    pd.Series
        Growth rates (percentage)
    """
    growth = df.groupby(groupby_col)[column].pct_change() * 100
    return growth


def summarize_by_region(df, metrics):
    """
    Generate regional summary statistics.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    metrics : list
        List of metric columns to summarize
    
    Returns:
    --------
    pd.DataFrame
        Summary statistics by region
    """
    summary = df.groupby('region')[metrics].mean().round(2)
    return summary


# Example usage
if __name__ == "__main__":
    print("Data Utilities Module - Urban Mobility Optimization")
    print("=" * 60)
    
    # Load data
    df_raw = load_raw_data()
    
    if df_raw is not None:
        # Quality check
        quality = validate_data_quality(df_raw, threshold=0.3)
        
        # Get latest year
        df_latest = get_latest_year_data(df_raw)
        
        # Regional summary
        metrics = ['gdp_per_capita_ppp', 'co2_emissions_per_capita', 'lpi_overall_score']
        regional_summary = summarize_by_region(df_latest, metrics)
        
        print("\nRegional Summary (Latest Year):")
        print(regional_summary)
