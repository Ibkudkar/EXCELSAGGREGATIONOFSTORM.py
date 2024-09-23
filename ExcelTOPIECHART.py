import pandas as pd # Imported pandas library to handle data frames
import matplotlib.pyplot as plt #Imported matplot library to support charting functionality.

# Defined IPStorm agent versions and protocols
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

# Defined protocols to check whether the IPStorm botnet
protocols = [
    "/sreque/1.0.0", "/shsk/1.0.0", "/sfst/1.0.0", "/sbst/1.0.0",
    "/sbpcp/1.0.0", "/sbptp/1.0.0", "/strelayp/1.0.0"
]

# Flattened the list of agent versions
all_agent_versions = [version for sublist in agent_versions.values() for version in sublist]

# Loaded the Excel file for each sorted
input_excel_file = r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\OutputfilesjsontoExcel\output-05-07-24.xlsx'

# Read the Excel file
df = pd.read_excel(input_excel_file, engine='openpyxl')

# Displayed the DataFrame to verify the contents
print(df)

# Defined a function to check if any of the protocols were present in the supported_protocols column
def check_protocols(supported_protocols):
    if pd.isna(supported_protocols):
        return False
    for protocol in protocols:
        if protocol in supported_protocols:
            return True
    return False

# Filtered the data based on the presence of specific protocols and agent versions
storm_present_rows = []
other_versions_rows = []

for index, row in df.iterrows():
    agent_version = row['agent_version']
    supported_protocols = row['supported_protocols']

    if (pd.isna(agent_version) or agent_version not in all_agent_versions) and check_protocols(supported_protocols):
        storm_present_rows.append(row)
    else:
        other_versions_rows.append(row)

# Created DataFrames for the STORM PRESENT rows and other versions rows
storm_present_df = pd.DataFrame(storm_present_rows)
other_versions_df = pd.DataFrame(other_versions_rows)

# Counted the occurrences of each agent_version
storm_present_counts = storm_present_df['agent_version'].value_counts()
other_versions_counts = other_versions_df['agent_version'].value_counts()

# Combined counts into a single series
combined_counts = pd.concat([storm_present_counts, other_versions_counts], axis=1, keys=['STORM PRESENT', 'Other Versions']).fillna(0)

# Defined a colormap for STORM PRESENT pie chart
storm_present_colors = plt.cm.tab20.colors[:len(storm_present_counts)]

# Plotted the pie charts
fig, ax = plt.subplots(1, 2, figsize=(18, 8))

# STORM PRESENT pie chart with custom colors
combined_counts['STORM PRESENT'].plot.pie(ax=ax[0], autopct='%1.1f%%', startangle=90, colors=storm_present_colors, title='STORM PRESENT')

# Other Versions pie chart with default colormap
combined_counts['Other Versions'].plot.pie(ax=ax[1], autopct='%1.1f%%', startangle=90, cmap='tab20', title='Other Versions')

# Formatting
ax[0].set_ylabel('')  # Hide the y-label
ax[1].set_ylabel('')  # Hide the y-label
plt.suptitle('Distribution of Agent Versions')

# Showed the pie charts
plt.show()