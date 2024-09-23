import pandas as pd #Imported pandas for data manipulation and analysis
import matplotlib.pyplot as plt #Import matplotlib for creating visualizations

# Path to the churn results file, the entry exit node sorted file
input_file = r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\churn_results.xlsx'
output_file = r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\detailed_churn_analysis.xlsx'

# Read the churn results, to plot it in a graph
df = pd.read_excel(input_file)

# Prepared lists to store detailed analysis
detailed_data = []

# Processed each row in the file
for index, row in df.iterrows():
    date = row['Date']

    # Count the number of nodes and IPs which entered or exited
    detailed_data.append({
        'Date': date,
        'Entered Nodes': len(eval(row['Entered Nodes'])),
        'Exited Nodes': len(eval(row['Exited Nodes'])),
        'New Nodes': len(eval(row['New Nodes'])),
        'Entered IPs': len(eval(row['Entered IPs'])),
        'Exited IPs': len(eval(row['Exited IPs']))
    })

# Converted detailed analysis to a excel file format
detailed_df = pd.DataFrame(detailed_data)

# Set the date as the index
detailed_df.set_index('Date', inplace=True)

# Sorted the entire DataFrame by date
detailed_df.sort_index(inplace=True)

# Splitted data into five parts (8, 8, 8, 8, 12 days) for easy image sorting
splits = [
    detailed_df.iloc[:8],
    detailed_df.iloc[8:16],
    detailed_df.iloc[16:24],
    detailed_df.iloc[24:32],
    detailed_df.iloc[32:44]
]


# Function to plot the data as bar graphs as its easy
def plot_data(data, title):
    ax = data.plot(kind='bar', stacked=False, figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title(title)
    plt.legend(loc='upper right')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Added numbers on the bars
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))


# Plotted each split, by the given number of days split
titles = [
    'Node and IP Churn - Days 1-8',
    'Node and IP Churn - Days 9-16',
    'Node and IP Churn - Days 17-24',
    'Node and IP Churn - Days 25-32',
    'Node and IP Churn - Days 33-44'
]

for split, title in zip(splits, titles):
    plot_data(split, title)

# Showed all plots at once
plt.show()

# Saved the detailed analysis to an Excel file
detailed_df.to_excel(output_file)

print(f"Detailed analysis saved to {output_file}.")