import json

path = './flavors.json'

print('[~] Loading flavors from "' + path + '"..')

try:
    with open(path, 'r') as flavors:
        flavors = json.load(flavors)
except:
    print('Something went wrong when opening the file.')
else:
    print('[OK] Flavors loaded')
