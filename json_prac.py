import json
with open('studentsjson', 'r') as fdes:
     data = json.load(fdes)
     print(data)
