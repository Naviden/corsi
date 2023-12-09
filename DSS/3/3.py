import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset = pd.read_csv('path_to_your_dataset.csv')  # Replace with the path to your dataset

# Convert the 'Date' column to datetime
dataset['Date'] = pd.to_datetime(dataset['Date'])

# Setting the style
plt.style.use('seaborn-darkgrid')

# Create a line plot for sales trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=dataset, x='Date', y='Sales', color='blue', label='Sales')

# Adding titles and labels
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()

# Show the plot
plt.show()
