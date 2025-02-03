import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


filepath = "./data/vgsales new.csv"
sales_data = pd.read_csv(filepath, index_col="Rank")


# Print first 5 rows
print(sales_data.head())


# Filter the data for heatmap
barplot_filtered = sales_data[['Genre', 'Global_Sales']].copy()


# Set the width and height of the figure
plt.figure(figsize=(14,8))


grouped_heatmap_data = barplot_filtered.groupby(['Genre']).mean().sort_values(by='Global_Sales', ascending=False).reset_index()


sns.barplot(data=grouped_heatmap_data, x='Genre', y='Global_Sales')
plt.xticks(rotation=70)
plt.show()


# Filter the data
temp_data = sales_data[['Genre', 'Global_Sales']].groupby(['Genre']).sum()
sorted_temp_data = temp_data.sort_values(by='Global_Sales', ascending=False).reset_index()


# Set the width and height of the figure
plt.figure(figsize=(14,8))

sns.set_style('whitegrid')
sns.barplot(data=sorted_temp_data, x='Genre', y='Global_Sales')
plt.xticks(rotation=60)
plt.show()


# Add title and labels