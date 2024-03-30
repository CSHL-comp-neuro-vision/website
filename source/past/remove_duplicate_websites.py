import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('websites.csv', header=None, names=['Name', 'Website'])

# Remove duplicates based on the first column (Last Name)
df.drop_duplicates(subset='Name', keep='first', inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv('websites_no_duplicates.csv', index=False)

print("Duplicates removed and file saved successfully!")