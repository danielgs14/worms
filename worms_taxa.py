#imports
import requests # connect to REST API
import pandas as pd # dataframe manipulation

# Read csv into pandas dataframe
df = pd.read.csv("")

# Function to fetch AphiaID for a given scientific name
def get_aphia_id(scientific_name):
    url = f"http://marinespecies.org/rest/AphiaIDByName/{scientific_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Extract AphiaID for each scientific name and store it in a new column
df['aphia_id'] = df['scientific_name'].apply(get_aphia_id)

# Display the updated dataframe
print(df)

# Write dataframe to new csv