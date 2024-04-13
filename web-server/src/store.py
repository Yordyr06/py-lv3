import requests

def get_data(path):
  req = requests.get(path)
  res = req.json()
  
  for data in res:
    print(data['name'])