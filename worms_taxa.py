#imports
import requests # connect to REST API
import pandas as pd # dataframe manipulation

# Read the sample csv into pandas dataframe. For your use, please change the path.
df = pd.read_csv('./files/sample_data.csv')

# Function to get AphiaID for a given scientific name
def get_aphia_id(scientific_name):
    url = f"http://marinespecies.org/rest/AphiaIDByName/{scientific_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get taxonomic breakdown using the previously requested AphiaID
def get_taxonomic_breakdown(aphia_id):
    url = f"http://marinespecies.org/rest/AphiaClassificationByAphiaID/{aphia_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Extract AphiaID for each scientific name and store it in a new column
df['aphia_id'] = df['scientific_name'].apply(get_aphia_id)

# Fetch full taxonomic breakdown using AphiaID and store it in a new column
df['taxonomic_breakdown'] = df['aphia_id'].apply(get_taxonomic_breakdown)

# Function to recursively flatten the taxonomic_breakdown JSON and create separate columns
def flatten_taxonomic_breakdown(row, prefix=''):
    if not row:
        return {}
    flat_dict = {}
    for key, value in row.items():
        if isinstance(value, dict):
            nested_dict = flatten_taxonomic_breakdown(value, f"{prefix}{key}_")
            flat_dict.update(nested_dict)
        else:
            flat_dict[f"{prefix}{key}"] = value
    return flat_dict

# Function to remove prefixes that are not user friendly 
def remove_prefix(df):
    df.columns = df.columns.str.replace('child_', '')
    return df

# Apply the flatten_taxonomic_breakdown function to each row in the DataFrame
df['flattened_taxonomic'] = df['taxonomic_breakdown'].apply(flatten_taxonomic_breakdown)

# Create a new DataFrame from the flattened data
flattened_df = pd.json_normalize(df['flattened_taxonomic'])

# Concatenate the original DataFrame with the flattened DataFrame
df = pd.concat([df, flattened_df], axis=1)

# Drop the 'aphia_id', 'taxonomic_breakdown', and 'flattened_taxonomic' columns
df.drop(['aphia_id', 'taxonomic_breakdown', 'flattened_taxonomic'], axis=1, inplace=True)

# Use function remove_prefix for easier readability of column names
df = remove_prefix(df)

# Write a new csv file with the requested information
df.to_csv('./files/taxa_breakdown.csv', index = False)

# Print the dataframe
print(df)