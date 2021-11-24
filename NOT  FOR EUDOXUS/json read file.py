import json
# read a JSON file
# 1st option
file_name = "data1.json"
with open(file_name) as f:
    data = json.load(f)
    
print(data)