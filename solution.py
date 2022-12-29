import os
import json

from cat import Cat
from exeptions import nonPositiveAgeException

def make_cat(data):
  name = data.get('name')
  gender = data.get('gender').get('name')
  age = data.get('age')
  if isinstance(age, int) and age < 0:
      id = data.get('id')
      message = f'Введен отрицательный возраст питомца id: {id}'
      raise nonPositiveAgeException(message)

  return Cat(name, gender, age)

path_to_file  = os.path.join('.', 'response.json')
with open(path_to_file, encoding='utf-8') as f:
  items = json.load(f).get('results')

try:
  cats = [ make_cat(item) for item in items ]
except nonPositiveAgeException as e:
  print(e)
else:
  for cat in cats:
    print(cat)
