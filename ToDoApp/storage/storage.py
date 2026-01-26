import json
from pathlib import Path

data_path =  Path("./data/task.json")

print("Resolved path:", data_path)
print("Exists:", data_path.exists())

def load_tasks():

    if data_path.exists():
        with open(data_path,"r") as f:
            return json.load(f)
        
    return []


def save_tasks(tasks):
    with open(data_path,"w") as f:
        json.dump(tasks,f,indent=2)

 



