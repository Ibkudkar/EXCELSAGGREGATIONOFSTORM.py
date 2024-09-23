import json #Imported JSON module to handle JSON data
import pandas as pd #Imported pandas library to handle data frames
import os  #Imported OS module to handle file paths

#Defined the path of JSON file - Used raw strings, escape characters were creating problem.
json_file_path = r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\IPFSCrawlerJSON\visitedPeers_2024-09-01_10-53-55_UTC.json'

#Opened the JSON file and loaded the data into python dictionary
with open(json_file_path, 'r') as file:
    data = json.load(file)

#Initialized an empty list to store rows for the Dataframe
rows = []

#Looped through each nodes in the 'found_nodes' list within the JSON data
for node in data.get("found_nodes", []):
    # Extracted the node ID
    node_id = node.get("id")
    # Joined the list of multiaddrs into a single string separated by commas
    multiaddrs = ','.join(node.get("multiaddrs", []))
    # Extracted the connection error if encountered
    connection_error = node.get("connection_error")
    result = node.get("result", {})

    # Initialized variables to None
    agent_version = None
    supported_protocols = None

    # Extracted the result if it exists
    result = node.get("result")
    if result:  # Checked if result is not None
        # Extracted the agent version
        agent_version = result.get("agent_version")
        # Joined the list of supported protocols into a single string separated by commas
        supported_protocols = ', '.join(result.get("supported_protocols", []))

    # Appended a dictionary of the extracted data to the rows list
    rows.append({
        "node_id": node_id,
        "multiaddrs": multiaddrs,
        "connection_error": connection_error,
        "agent_version": agent_version,
        "supported_protocols": supported_protocols
    })

#Created a dataframe from the list of rows
df = pd.DataFrame(rows, columns=[
    "node_id", "multiaddrs", "connection_error", "agent_version", "supported_protocols"
])

#Defined the path to the output excel file using a raw string
output_file_path = (r'C:\Users\ISHA\Downloads\Dissertation collected data + Code\OutputfilesjsontoExcel\output-01-09-24.xlsx')

# Debugged print to ensure the file path is correct
print(f"Output file path: {output_file_path}")

# Saved to Excel file without the index column
df.to_excel(output_file_path, index=False)

#Printed a success message
print("Excel file has been created successfully.")