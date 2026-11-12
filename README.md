# UK Electricity Demand and Renewable Generation Analysis

## Project Overview

This project explores electricity demand and embedded renewable generation in Great Britain throughout 2025.

Using publicly available data from the National Energy System Operator (NESO), the analysis investigates patterns in electricity demand, wind generation and solar generation.

The objective is to develop practical experience in Python-based data analysis while exploring the relationship between electricity demand and renewable energy generation.

## Research Questions

- How does electricity demand vary throughout the year?
- What patterns can be observed in embedded wind and solar generation?
- How does renewable generation vary relative to electricity demand?
- What insights can these patterns provide about the UK's electricity system?

## Dataset

Source: NESO (National Energy System Operator).

The dataset contains 17,520 observations covering 1 January to 31 December 2025, representing half-hourly settlement periods.

Key variables include:
- National demand (ND)
- Transmission system demand (TSD)
- England and Wales demand
- Embedded wind generation
- Embedded solar generation
- Interconnector flows

## Methodology

The analysis uses Python, principally pandas for data manipulation and Matplotlib for visualisation.

The methodology includes:
1. Loading and inspecting the original dataset.
2. Checking data types and missing values.
3. Calculating descriptive statistics.
4. Grouping and analysing observations across different periods.
5. Creating visualisations to identify patterns and relationships.

## Key Findings

1. Demand:
The average demand profile shows a spike in the early waking hours, and a bigger one during the evening hours to a maximum of circa 26,000 MW, with a slight dip in between these times. Demand really drops during the night, with 5am being the lowest demand time, at around 13,000 MW. 

2. Renewable generation:
Solar generation has a predictable pattern: an upward sloping curve until midday, and then a downward slope until it reaches zero after sunset. It stays at zero until sunrise.

3. Business implications and limitations:
The analysis highlights the variability of embedded renewable generation, particularly solar generation, across the day.

For data-centre developers, this reinforces the importance of securing reliable electricity supply rather than relying solely on intermittent generation sources.

Potential solutions include combining renewable power purchase agreements (PPAs), grid electricity, battery storage and other dispatchable generation sources.

However, this dataset does not establish the cost, availability or optimal energy mix for an individual data centre. Further analysis of electricity prices, grid constraints and storage economics would be required.

## Limitations

- The analysis covers only one calendar year, limiting the ability to identify long-term trends.
- The dataset is observational and does not establish causal relationships.
- Embedded generation represents only part of the UK's renewable electricity system.
- The analysis does not independently assess electricity prices, grid constraints or the economics of individual generation assets.

## Tools

- Python
- pandas
- Matplotlib
- Jupyter Notebook

## Reproducibility

Open the file names 'UK_AI_Infrastructure_W1' for the code. At one point, it will prompt you to upload the dataset, which is attached as 'demanddata_2025.csv'

## Author

Javier Fraga
