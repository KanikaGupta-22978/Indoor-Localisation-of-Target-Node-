import os
import pandas as pd

# Directory containing .xls files
xls_directory = 'C:\\Users\\ftska\\all projects\\sample_project_2\\Mini_Project'

# Output directory for .csv files
output_directory = 'C:\\Users\\ftska\\all projects\\sample_project_2\\Mini_Project'

# Iterate through each file in the directory
for file_name in os.listdir(xls_directory):
    if file_name.endswith('.xlsx'):
        # Construct input file path
        input_file = os.path.join(xls_directory, file_name)
        
        # Read all sheets in the Excel file
        xls_data = pd.read_excel(input_file, sheet_name=None)
        
        # Iterate through each sheet and save as CSV
        for sheet_name, df in xls_data.items():
            # Construct output file path
            output_file = os.path.join(output_directory, os.path.splitext(file_name)[0] + '_' + sheet_name + '.csv')
            
            # Write to CSV file
            df.to_csv(output_file, index=False)
