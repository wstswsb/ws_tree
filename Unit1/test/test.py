import json
from pprint import pprint


number_of_tasks = 3
for i in range(number_of_tasks):
    with open(f"../task_{i+1}/answer.json", "r") as file:
        content = json.load(file)
    pprint(content)
    
