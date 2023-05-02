import requests, json, os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
# Load the token from the Notion Integration
#   and the database ID 
token = os.getenv('TOKEN')
dbid = os.getenv('DBID')

# Provide the token in the headers 
#   (provided by the documentation) to authenticate
headers = {
    "Authorization": "Bearer "+token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-08-16"
}

# Prepare the API call with the database ID
url = f'https://api.notion.com/v1/databases/{dbid}/query'
# Specify the HTTP request, the URL and headers
# This returns the data
res = requests.request("POST", url, headers=headers)
data = res.json()

hours = []
days = []

# Fetch hours and dates in separate arrays from the response
for x in data['results']:
    hours.append(x['properties']['Hours']['number'])
    days.append(x['properties']['Date']['date']['start'])

# Shorten the dates so they do not include the year
days2 = []
for x in days:
    x = x[5:]
    days2.append(x)

# By default, the data would be ordered from newer to older
# I want the graph to show newest data at the end
days2.reverse()
hours.reverse()

# We prepare the graph with X and Y vectors respectively 
plt.plot(days2, hours)

# Put a label on each vector and generate it with a grid
plt.ylabel("Hours")
plt.xlabel("Day")
plt.grid()

# We save the file
plt.savefig('productivity.png')