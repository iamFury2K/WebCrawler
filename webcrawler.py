#Importing Libraries
import csv
from googleapiclient.discovery import build

# Defining Constant Values
API_KEY = 'AIzaSyAQDch3koClyrVfB6Y2oFYcOORqzi-JS2s'
CSE_ID = '27ba18017b7df41eb'
QUERY = 'site:youtube.com openinapp.co'

service = build('customsearch','v1', developerKey=API_KEY)

# Performing Search
result = []
starting_index = 1
while len(result) < 10000 and starting_index < 100: # starting_index is going till 100 beacause of google api restriction
    response = service.cse().list(q=QUERY, cx=CSE_ID, start=starting_index, num=10).execute()
    if 'items' in response:
        items = response['items']
        result.extend(items)
        starting_index += len(items)
    else:
        break
channel_links = []
for r in result:
    link = r['link']
    if 'youtube.com/channel/' in link:
        channel_links.append(link)
# Preparing data in csv format
data = [{'channel_link' : link} for link in channel_links]

# Saving Data in csv format
filename = 'youtube_channel.csv'
with open(filename, 'w', newline='') as f:
    fieldnames = ['channel_link']
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(data)
# printing channel links which have been saved
print(f'{len(data)} YouTube Channel links {filename}')