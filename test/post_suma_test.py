import numpy as np
import requests
import json


files = {'a':1,
         'b':2}

r = requests.post('http://127.0.0.1:5000//operaciones//suma', json=files)

# print(r)
# print(r.url)
# print(r.status_code)
print(r.text)
