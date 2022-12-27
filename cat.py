class Cat:
  def __init__(self, name='', gender='', age=None) -> None:
    self.name = name
    self.gender = gender
    self.age = age

  # def init_from_dict(self, cat_dict={}):
  #   self.name = cat_dict.get('name')
  #   self.breed = cat_dict.get('breed')
  #   self.age = cat_dict.get('age')

  def getName(self):
    return self.name

  def getGender(self):
    return self.gender

  def getAge(self):
    return self.age
