class Cat:
  def __init__(self, name='', gender='', age=None) -> None:
    self.name = name
    self.gender = gender
    self.age = age

  def __str__(self):
    return f'имя: {self.name}\tпол: {self.gender}\tвозраст: {self.age}'

  # def init_from_dict(self, cat_dict={}):
  #   self.name = cat_dict.get('name')
  #   self.gender = cat_dict.get('gender')
  #   self.age = cat_dict.get('age')

  # def getName(self):
  #   return self.name

  # def getGender(self):
  #   return self.gender

  # def getAge(self):
  #   return self.age
