import urllib.request
import json

url = 'http://singlesecond.com/dong.json'

response = urllib.request.urlopen(url)

result = json.loads(response.read())
#print(result)
#print(result['name'])
#print(result['bde'])

for Key in result:
	print(Key, result[Key])
