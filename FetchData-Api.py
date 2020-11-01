
import urllib.request as urllib2
import json
import random
from collections import Counter

url_api = 'https://api.publicapis.org/entries'
json_obj = urllib2.urlopen(url_api)
data = json.load(json_obj)
entries = data['entries']

teste = random.randint(1, len(entries))


for item in data['entries']:
    print('@@@@@@')

    print(item['API'])
    print(item['Description'])
    print(item['Category'])
    print(item['Link'])
 

'''
for item in data['entries']:
    print('aaa' + str(item))
    

with open('teste.json', 'w') as json_file:
        json.dump(entries, json_file)    
'''