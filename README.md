Project Structure:

Appendix C - Python implementation.txt: Contains the Python code for the analysis.

C.1 Storm botnet json file to excel: This script reads data from a JSON file containing information about IPFS nodes and converts it into an Excel spreadsheet.
C.2 Excel segregation of Storm: This script processes the Excel file generated in the previous step. It identifies potential Storm botnet nodes based on their reported agent versions and supported protocols.
C.3 PIE chart output: This script generates pie charts visualizing the distribution of agent versions among the identified Storm botnet nodes and other nodes in the dataset.
C.4 Linegraph (truncated): This script appears to be intended to generate a line graph, but the provided code is incomplete.

Dependencies:
Python 3
pandas
matplotlib
openpyxl
glob
re
json
Usage:

Install Dependencies: Install the required Python libraries.
Data Collection: Obtain a JSON file containing data on IPFS nodes.
Data Conversion 
(C.1):
Update the json_file_path variable in C.1 to point to your JSON file.
Update the output_file_path variable to specify the desired location for the output Excel file.
Run the script C.1.
Botnet Identification 
(C.2):
Update the input_excel_file variable in C.2 to point to the Excel file generated in the previous step.
Update the output_excel_file variable to specify the desired location for the output Excel file containing the identified Storm nodes.
Run the script C.2.
Data Visualization (
C.3 & C.4):
Pie Chart (C.3):
Update the input_excel_file variable in C.3 to point to the Excel file containing the analyzed data.
Run the script C.3 to generate pie charts.
Line Graph (C.4):
The provided code for C.4 is incomplete. You will need to complete the script to generate the line graph.
Note:

The provided code includes hardcoded file paths. Make sure to update these paths to match your system's file structure.
The code snippet for generating the line graph (C.4) is incomplete. You will need to fill in the missing parts to generate the graph.
This code is provided as a starting point for analyzing IPFS data for Storm botnet activity. You may need to modify or adapt the code based on your specific needs and data.
