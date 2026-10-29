import json
import urllib.request

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info['comments']

total = 0
for comment in comments:
    total += comment['count']

print('Count:', len(comments))
print('Sum:', total)
