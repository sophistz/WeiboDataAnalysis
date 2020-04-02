import json

file = open('test.json')
dict = json.load(file)
for id in dict:
    print(dict[id])
    pass