import pandas as pd #Imported pandas for data manipulation and analysis
import glob #Imported glob to find files matching a pattern
import matplotlib.pyplot as plt #Imported matplotlib for plotting
import os #Imported OS for interacting with the operating system

# Path to the folder containing the Excel files, which contains only storm data
excel_files = glob.glob(r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\Sortedexcelfiles\*.xlsx')

# Sorted files by filename
excel_files.sort()

# Listed to store total nodes and corresponding dates
total_nodes_list = []
dates_list = []

# Processed each Excel file, in order to get the number
for file in excel_files:
    df = pd.read_excel(file)

    # Extracted date from filename assuming it's part of the filename
    date = os.path.basename(file).split('.')[0]  # Adjust this line based on actual filename structure
    dates_list.append(date)

    # Checked if 'node_id' column exists which will help us only plot the legitimate data
    if 'node_id' in df.columns:
        # Count the unique node IDs to determine the total number of nodes
        total_nodes = df['node_id'].nunique()
        total_nodes_list.append(total_nodes)
    else:
        print(f"Warning: 'node_id' column not found in {file}")

# Created a DataFrame for the total nodes as in total number of nodes
trend_df = pd.DataFrame({
    'Date': dates_list,
    'Total Nodes': total_nodes_list
})

# Plotted the trend
plt.figure(figsize=(10, 6))
plt.plot(trend_df['Date'], trend_df['Total Nodes'], marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Total Nodes')
plt.title('Total STORM Nodes Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()