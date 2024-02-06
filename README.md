# Climate Change Analysis

## Table of Contents
- [Project Overview](project-overview)
- [Data Source](data-source)
- [Tools](tools)
- [Data Cleaning/Preparation](data-cleaning/preparation)
- [Exploratory Data Analysis](exploratory-data-analysis)
- [Data Analysis](data-analysis)
- [Results/Findings](results/findings)
- [Recommendations](recommendations)
- [Limitations](limitations)
- [References](references)


## Project Overview
This project aims to explore different parameters related to climate change. By analyzing
various aspects of the data, we aim to identify different trends and gain further insights into 
how the parameters affect each other and the overall changes they have undergone within the 
examined period.

## Data Source

Climate change data: The primary dataset for this analysis is the "climate_change_data.csv" file containing 
information about different atmospheric parameters from 2000 to 2024 across different countries.


## Tools
- Excel - 
- Jypter Notebook - Data cleaning, analysis, and Visualization


  ## Data Cleaning/Preparation
In the initial data preparation phase the following was done:
1. Data loading and Inspections
2. Handling missing values
3. Data cleaning and Formatting

## Exploratory Data Analysis
EDA involved exploring the climate change data to answer important questions such as:

- Is there a noticeable trend in temperature over time?
- How have CO2 emissions changed over the specified time period?
- Is there a correlation between temperature and CO2 emissions?
- Are there strong correlations between temperature, CO2 emissions, sea level rise, precipitation, humidity, and wind speed?

## Data Analysis
``` python
plt.figure(figsize=(12, 6))

# Calculate the average temperature over time
average_temperature = df.groupby('Date')['CO2 Emissions'].mean().reset_index()

# Plot the line
sns.lineplot(x='Date', y='CO2 Emissions', data=average_temperature)

plt.title("Temporal Trend in CO2 Emissions")
plt.show()
```

## Results/Findings


## Recommendations


## Limitations

## References



  
