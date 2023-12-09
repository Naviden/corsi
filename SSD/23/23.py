# Obiettivo: Dimostrare il valore delle tecniche di Business Intelligence come l'analisi di tendenza e la previsione delle vendite

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
dataset = pd.read_csv('path_to_your_dataset.csv')  # Replace with the path to your dataset

# Convert the 'Date' column to datetime
dataset['Date'] = pd.to_datetime(dataset['Date'])
dataset.set_index('Date', inplace=True)

# Time Series Decomposition
decomposition = seasonal_decompose(dataset['Sales'], model='additive', period=30)

# Setting the style
sns.set(style="whitegrid")

# Creating subplots for trend, seasonality, and residuals
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
decomposition.trend.plot(ax=ax1)
ax1.set_title('Trend')
decomposition.seasonal.plot(ax=ax2)
ax2.set_title('Seasonality')
decomposition.resid.plot(ax=ax3)
ax3.set_title('Residuals')

# Layout adjustments
plt.tight_layout()

# Show the plot
plt.show()
