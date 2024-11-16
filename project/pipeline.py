# Import necessary libraries
import pandas as pd
import sqlite3
import ssl
import geopandas as gpd
from urllib.request import urlretrieve
import os

# Disable SSL verification (if needed)
ssl._create_default_https_context = ssl._create_unverified_context

# Ensure output directory exists
output_dir = "./data"
os.makedirs(output_dir, exist_ok=True)

def load_datasets():
    """
    Load datasets from given URLs and return as DataFrames.
    """
    url_socioeconomic = "https://data.cdc.gov/api/views/hn4x-zwk7/rows.csv?accessType=DOWNLOAD"
    url_obesity = "https://services3.arcgis.com/HESxeTbDliKKvec2/arcgis/rest/services/LakeCounty_Health/FeatureServer/8/query?outFields=*&where=1%3D1&f=geojson"
    
    # Load socioeconomic data as CSV
    socioeconomic_data = pd.read_csv(url_socioeconomic)
    
    # Load obesity data as GeoJSON
    obesity_data = gpd.read_file(url_obesity)
    
    return socioeconomic_data, obesity_data

def preprocess_socioeconomic_data(socioeconomic_data):
    """
    Preprocess the socioeconomic DataFrame: Select relevant columns, rename them, and standardize location names.
    """
    # Remove any extra spaces from column names
    socioeconomic_data.columns = socioeconomic_data.columns.str.strip()
    
    # Keep only the important columns
    important_columns = [
        "YearStart", "YearEnd", "LocationAbbr", "LocationDesc", "Data_Value", 
        "Education", "Income", "Age(years)", "Gender", "Race/Ethnicity", 
        "Sample_Size", "Low_Confidence_Limit", "High_Confidence_Limit"
    ]
    socioeconomic_data = socioeconomic_data[important_columns]
    
    # Rename 'LocationDesc' to 'Location' for consistency
    socioeconomic_data.rename(columns={'LocationDesc': 'Location'}, inplace=True)
    
    # Drop rows with missing values in the 'Location' column
    socioeconomic_data.dropna(subset=['Location'], inplace=True)
    
    # Standardize 'Location' column to lowercase and remove whitespace
    socioeconomic_data['Location'] = socioeconomic_data['Location'].str.lower().str.strip()
    
    return socioeconomic_data

def preprocess_obesity_data(obesity_data):
    """
    Preprocess the obesity DataFrame: Keep only relevant columns and standardize location names.
    """
    # Keep only the 'NAME' and 'Obesity' columns and rename 'NAME' to 'Location'
    obesity_data = obesity_data[['NAME', 'Obesity']]
    obesity_data.rename(columns={'NAME': 'Location'}, inplace=True)
    
    # Drop rows with missing values in the 'Location' column
    obesity_data.dropna(inplace=True)
    
    # Standardize 'Location' column to lowercase and remove whitespace
    obesity_data['Location'] = obesity_data['Location'].str.lower().str.strip()
    
    return obesity_data

def merge_data(socioeconomic_data, obesity_data):
    """
    Merge the two datasets on the 'Location' column.
    """
    # Merge the two datasets on 'Location' column
    merged_data = pd.merge(socioeconomic_data, obesity_data, on='Location', how='inner')
    return merged_data

def main():
    # Load datasets
    socioeconomic_data, obesity_data = load_datasets()
    
    # Preprocess the datasets
    socioeconomic_data = preprocess_socioeconomic_data(socioeconomic_data)
    obesity_data = preprocess_obesity_data(obesity_data)

    # Debugging: Inspect unique Location values to check for mismatches
    print("Columns in socioeconomic_data:", socioeconomic_data.columns)
    print("Columns in obesity_data:", obesity_data.columns)
    print("Unique Location values in socioeconomic_data:")
    print(socioeconomic_data['Location'].unique()[:10])  # Print first 10 unique locations

    print("Unique Location values in obesity_data:")
    print(obesity_data['Location'].unique()[:10])  # Print first 10 unique locations

    # Merge the datasets
    merged_data = merge_data(socioeconomic_data, obesity_data)

    # Display the merged DataFrame to check if merging was successful
    print("Merged Data:")
    print(merged_data.head())

    # Save to SQLite and CSV in the `/data` directory
    if not merged_data.empty:
        # Save to SQLite
        conn = sqlite3.connect(os.path.join(output_dir, 'obesity_socioeconomic.db'))
        merged_data.to_sql('merged_data', conn, if_exists='replace', index=False)
        conn.commit()
        conn.close()
        
        # Save to CSV
        merged_data.to_csv(os.path.join(output_dir, 'merged_obesity_socioeconomic_data.csv'), index=False)
        print("Merged dataset saved as merged_obesity_socioeconomic_data.csv")
    else:
        print("Warning: Merged data is empty. Please check the Location values.")

if __name__ == "__main__":
    main()
