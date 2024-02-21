import pandas as pd

# Load Excel file
excel_file = pd.ExcelFile('data\DS-Hackathon-1.xlsx')

# Iterate through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name)
    
    # Write the DataFrame to a CSV file
    csv_file_name = f'{sheet_name}.csv'
    df.to_csv(csv_file_name, index=False)

    print(f'Saved {csv_file_name}')
