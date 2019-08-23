import urllib.request
import json

url = 'http://api.open-notify.org/astros.json'

response = urllib.request.urlopen(url)

result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']
print(people)
