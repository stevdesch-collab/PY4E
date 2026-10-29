import json
import urllib.parse
import urllib.request

api = 'http://py4e-data.dr-chuck.net/opengeo?'

address = input('Enter location: ')

parms = dict()
parms['q'] = address
parms['key'] = 42
url = api + urllib.parse.urlencode(parms)

print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

plus_code = js['features'][0]['properties']['plus_code']
print('Plus code', plus_code)
