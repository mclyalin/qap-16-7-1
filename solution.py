import os
import json
from cat import Cat

def make_cat(data):
  name = data.get('name')
  gender = data.get('gender').get('name')
  age = data.get('age')
  return Cat(name, gender, age)

path_to_file  = os.path.join('.', 'response.json')
with open(path_to_file, encoding='utf-8') as f:
  items = json.load(f).get('results')

cats = [ make_cat(item) for item in items ]

for cat in cats:
  print(f'name: {cat.getName()},\tgender: {cat.getGender()},\tВозраст: {cat.getAge()} лет')
