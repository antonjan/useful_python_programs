import json
import pandas as pd

#Load the JSON data

with open('book.json','r') as f:
data = json.load(f)

#Create a DataFrame from the JSON data

df = pd.DataFrame(data['books'])

df
