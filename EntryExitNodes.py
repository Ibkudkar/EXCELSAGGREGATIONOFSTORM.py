import glob #Imported the glob module to search for files matching a pattern
import pandas as pd #Imported pandas for data manipulation and analysis
import re #Imported the regular expressions module for pattern matching
import os #Imported OS for interacting with the operating system

# Directory which contains sorted Excel files which only contains STORM data
folder_path = r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\Sortedexcelfiles\\'

# List of all Excel files in the directory, so that each file is selected
excel_files = glob.glob(folder_path + '*.xlsx')

# Initialized sets to track each node and IP for our ease
previous_nodes = set()
previous_ips = set()
all_nodes = set()

# Initialized a list to store results after the Entry and exit node sorting
results = []

# Processed each file as an individual file
for file in sorted(excel_files):
    # Skipped hidden or temporary files as there might be other data files created
    if os.path.basename(file).startswith('~$'):
        continue

    # Extracted date from file name using regex, for date
    match = re.search(r'(\d{2}_\d{2}_\d{4})', os.path.basename(file))
    date = pd.to_datetime(match.group(0), format='%d_%m_%Y') if match else "Unknown Date"

    # Read the Excel file
    df = pd.read_excel(file, engine='openpyxl')

    # Got current nodes and IPs which already exists
    current_nodes = set(df['node_id'].dropna().unique())
    current_ips = set(df['multiaddrs'].dropna().unique())

    # Calculated churn for entered and exit nodes
    entered_nodes = current_nodes - previous_nodes
    exited_nodes = previous_nodes - current_nodes

    #Listed down new nodes which are there
    new_nodes = current_nodes - all_nodes
    all_nodes.update(current_nodes)

    #The IP addresses of the entry and exit nodes
    entered_ips = current_ips - previous_ips
    exited_ips = previous_ips - current_ips

    # Stored results for the latest date when the code is getting run
    results.append({
        'Date': date,
        'Entered Nodes': list(entered_nodes),
        'Exited Nodes': list(exited_nodes),
        'New Nodes': list(new_nodes),
        'Entered IPs': list(entered_ips),
        'Exited IPs': list(exited_ips)
    })

    # Updated previous nodes and IPs
    previous_nodes = current_nodes
    previous_ips = current_ips

# Converted results to a to excel file format
results_df = pd.DataFrame(results)

# Saved the results to a new excel file created
output_file = r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\churn_results.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    results_df.to_excel(writer, index=False)

print(f"Results saved to {output_file}")