import glob #imported the glob module to find all pathnames matching a specified pattern
import pandas as pd #Imported Pandas for data manipulation and analysis
import matplotlib.pyplot as plt #Imported matplotlib for plotting
import re #Imported regular expressions module for string matching

# Listed of Excel files which contains crawler json file data
excel_files = glob.glob(r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\OutputfilesjsontoExcel\*.xlsx')

# Initialized lists to store data
dates = []
normal_node_counts = []
storm_node_counts = []

# Defined the IPStorm botnet agent versions and protocols
agent_versions = {
    "goIpfs": [
        "go-ipfs/0.16.0", "go-ipfs/0.15.0", "go-ipfs/0.14.0", "go-ipfs/0.13.0", "go-ipfs/0.12.0",
        "go-ipfs/0.11.0", "go-ipfs/0.10.0", "go-ipfs/0.9.0", "go-ipfs/0.8.0", "go-ipfs/0.7.0",
        "go-ipfs/0.6.0", "go-ipfs/0.5.0", "go-ipfs/0.4.0", "go-ipfs/0.3.0", "go-ipfs/0.2.0",
        "go-ipfs/0.1.0"
    ],
    "kubo": [
        "kubo/0.29.0", "kubo/0.28.0", "kubo/0.27.0", "kubo/0.26.0", "kubo/0.25.0", "kubo/0.24.0",
        "kubo/0.23.0", "kubo/0.22.0", "kubo/0.21.0", "kubo/0.20.0", "kubo/0.19.0", "kubo/0.18.0",
        "kubo/0.17.0", "kubo/0.16.0", "kubo/0.15.0", "kubo/0.14.0"
    ],
    "jsIpfs": [
        "js-ipfs/0.59.0", "js-ipfs/0.58.0", "js-ipfs/0.57.0", "js-ipfs/0.56.0", "js-ipfs/0.55.0",
        "js-ipfs/0.54.0", "js-ipfs/0.53.0", "js-ipfs/0.52.0", "js-ipfs/0.51.0", "js-ipfs/0.50.0",
        "js-ipfs/0.49.0", "js-ipfs/0.48.0", "js-ipfs/0.47.0", "js-ipfs/0.46.0", "js-ipfs/0.45.0",
        "js-ipfs/0.44.0", "js-ipfs/0.43.0", "js-ipfs/0.42.0", "js-ipfs/0.41.0", "js-ipfs/0.40.0",
        "js-ipfs/0.39.0", "js-ipfs/0.38.0", "js-ipfs/0.37.0", "js-ipfs/0.36.0", "js-ipfs/0.35.0",
        "js-ipfs/0.34.0", "js-ipfs/0.33.0", "js-ipfs/0.32.0", "js-ipfs/0.31.0", "js-ipfs/0.30.0",
        "js-ipfs/0.29.0", "js-ipfs/0.28.0", "js-ipfs/0.27.0", "js-ipfs/0.26.0", "js-ipfs/0.25.0",
        "js-ipfs/0.24.0", "js-ipfs/0.23.0", "js-ipfs/0.22.0", "js-ipfs/0.21.0", "js-ipfs/0.20.0",
        "js-ipfs/0.19.0", "js-ipfs/0.18.0", "js-ipfs/0.17.0", "js-ipfs/0.16.0", "js-ipfs/0.15.0",
        "js-ipfs/0.14.0", "js-ipfs/0.13.0", "js-ipfs/0.12.0", "js-ipfs/0.11.0", "js-ipfs/0.10.0",
        "js-ipfs/0.9.0", "js-ipfs/0.8.0", "js-ipfs/0.7.0", "js-ipfs/0.6.0", "js-ipfs/0.5.0",
        "js-ipfs/0.4.0", "js-ipfs/0.3.0", "js-ipfs/0.2.0", "js-ipfs/0.1.0"
    ],
    "rustIpfs": [
        "rust-ipfs/0.5.0", "rust-ipfs/0.4.0", "rust-ipfs/0.3.0", "rust-ipfs/0.2.0", "rust-ipfs/0.1.0"
    ]
}

# Created a flattened list of all agent versions together
all_agent_versions = [version for sublist in agent_versions.values() for version in sublist]

# Defined protocols to check for the sign of IPStorm Botnet
protocols = [
    "/sreque/1.0.0", "/shsk/1.0.0", "/sfst/1.0.0", "/sbst/1.0.0",
    "/sbpcp/1.0.0", "/sbptp/1.0.0", "/strelayp/1.0.0"
]

# Created function to check protocols of IPStorm botnet
def check_protocols(supported_protocols):
    if pd.isna(supported_protocols):
        return False
    for protocol in protocols:
        if protocol in supported_protocols:
            return True
    return False

# Processed file one by one
for file in excel_files:
    # Extracted date from file name using regex
    match = re.search(r'\d{2}-\d{2}-\d{2}', file)
    if match:
        date = pd.to_datetime(match.group(0), format='%d-%m-%y')
        dates.append(date)

    # Read Excel file
    df = pd.read_excel(file, engine='openpyxl')

    # Separated storm nodes and normal nodes
    storm_nodes = df.apply(lambda row: check_protocols(row['supported_protocols']) and (pd.isna(row['agent_version']) or row['agent_version'] not in all_agent_versions), axis=1).sum()
    normal_nodes = len(df) - storm_nodes

    normal_node_counts.append(normal_nodes)
    storm_node_counts.append(storm_nodes)

# Created a DataFrame for plotting
plot_data = pd.DataFrame({
    'Date': dates,
    'Normal Nodes': normal_node_counts,
    'Storm Nodes': storm_node_counts
})

# Sorted by date
plot_data.sort_values('Date', inplace=True)

# Plotted the data as a line graph
plt.figure(figsize=(14, 8))
plt.plot(plot_data['Date'], plot_data['Normal Nodes'], marker='o', label='Normal Nodes')
plt.plot(plot_data['Date'], plot_data['Storm Nodes'], marker='o', label='Storm Nodes', linestyle='--')

# Added labels and title
plt.xlabel('Date')
plt.ylabel('Number of Nodes')
plt.title('Comparison of Normal and Storm Nodes Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Printed the data points with numbers
for i, row in plot_data.iterrows():
    plt.annotate(f"{row['Normal Nodes']}",
                 (row['Date'], row['Normal Nodes']),
                 textcoords="offset points",
                 xytext=(-10,10), ha='center', fontsize=9, color='blue')
    plt.annotate(f"{row['Storm Nodes']}",
                 (row['Date'], row['Storm Nodes']),
                 textcoords="offset points",
                 xytext=(-10,-15), ha='center', fontsize=9, color='red')

# Showed the plot
plt.tight_layout()
plt.show()