# Obiettivo: Confrontare l'efficacia di due campagne di marketing analizzando la correlazione tra visite al sito web e vendite

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load the dataset
dataset = pd.read_csv('path_to_your_dataset.csv')  # Replace with the path to your dataset

# Convert the 'Date' column to datetime
dataset['Date'] = pd.to_datetime(dataset['Date'])

# Basic statistics for each campaign
campaign_stats = dataset[['Campaign_A_Sales', 'Campaign_B_Sales', 'Website_Visits_A', 'Website_Visits_B']].describe()

# Correlation analysis
correlation_a = pearsonr(dataset['Campaign_A_Sales'], dataset['Website_Visits_A'])
correlation_b = pearsonr(dataset['Campaign_B_Sales'], dataset['Website_Visits_B'])

# Setting the style
sns.set(style="whitegrid")

# Creating subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Sales trends for each campaign
sns.lineplot(ax=axes[0, 0], data=dataset, x='Date', y='Campaign_A_Sales', color='blue', label='Campaign A Sales')
sns.lineplot(ax=axes[0, 0], data=dataset, x='Date', y='Campaign_B_Sales', color='green', label='Campaign B Sales')
axes[0, 0].set_title('Sales Comparison of Campaign A and B')

# Website visits trends for each campaign
sns.lineplot(ax=axes[0, 1], data=dataset, x='Date', y='Website_Visits_A', color='blue', label='Campaign A Website Visits')
sns.lineplot(ax=axes[0, 1], data=dataset, x='Date', y='Website_Visits_B', color='green', label='Campaign B Website Visits')
axes[0, 1].set_title('Website Visits Comparison of Campaign A and B')

# Scatter plot for Campaign A Sales vs. Website Visits
sns.scatterplot(ax=axes[1, 0], data=dataset, x='Website_Visits_A', y='Campaign_A_Sales')
axes[1, 0].set_title('Campaign A: Sales vs. Website Visits\nCorrelation: {:.2f}'.format(correlation_a[0]))

# Scatter plot for Campaign B Sales vs. Website Visits
sns.scatterplot(ax=axes[1, 1], data=dataset, x='Website_Visits_B', y='Campaign_B_Sales')
axes[1, 1].set_title('Campaign B: Sales vs. Website Visits\nCorrelation: {:.2f}'.format(correlation_b[0]))

# Layout adjustments
plt.tight_layout()

# Show the plot
plt.show()

campaign_stats
