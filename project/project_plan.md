# Project Plan

## Title

Uncovering U.S. Obesity Trends: The Socioeconomic Impact of Income and Education Levels

## Main Question

Is there a correlation between obesity rates and socioeconomic factors, such as income or education levels?

## Description

Obesity is a growing public health concern in the United States, with various factors contributing to its prevalence. Socioeconomic factors, such as income and education levels, may influence lifestyle choices, access to health resources, and ultimately impact obesity rates. This project aims to analyze the relationship between obesity rates and socioeconomic factors (income and education levels) across different U.S. states. By examining this correlation, the study seeks to provide insights into how socioeconomic disparities might affect health outcomes, particularly obesity, and offer guidance for addressing these disparities through targeted public health interventions.

## Datasources

### Datasource1: Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System
* Metadata URL: https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system/resource/0280bb9c-4de8-4b95-9642-93f727c4d305
* Data URL: https://data.cdc.gov/api/views/hn4x-zwk7/rows.csv?accessType=DOWNLOAD
* Data Type: CSV
* Description: This dataset provides state-specific data on various health metrics, including obesity rates, physical activity, and nutritional habits, with additional socioeconomic variables like income and education levels.

### Datasource2: Obesity Rates and Geographic Information by State
* Metadata URL: https://data-lakecountyil.opendata.arcgis.com/datasets/lakecountyil::national-obesity-by-state/explore
* Data URL: https://services3.arcgis.com/HESxeTbDliKKvec2/arcgis/rest/services/LakeCounty_Health/FeatureServer/8/query?outFields=*&where=1%3D1&f=geojson
* Data Type: GeoJSON
* Description: This dataset provides state-level obesity rates and other demographic information, allowing for spatial analysis. It includes variables that may enable a geographic analysis of obesity and its potential links with socioeconomic factors.

## Work Packages

1. Data Cleaning and Preprocessing: Load both datasets into a suitable analysis environment (e.g., Python with Pandas and GeoPandas)

2. Data Integration and Mergin: Merge the datasets based on common identifiers (e.g., state or location codes)

3. Exploratory Data Analysis (EDA): Conduct an initial exploration to understand the distribution of obesity rates and socioeconomic factors across states.

4. Correlation Analysis: Use statistical techniques to analyze the relationship between obesity rates and socioeconomic factors.

5. Results Interpretation and Report: Summarize the findings, focusing on any significant correlations between socioeconomic factors and obesity rates.

6. Final Presentation Preparation: Create visualizations, key findings, and interpretations for presentation.