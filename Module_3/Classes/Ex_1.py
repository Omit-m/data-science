class Person:
  pass

  def Y(self, name, age,address):
    self.name = name
    self.age = age
    self.address = address


p1 = Person()

p1.Y("omit",23," Alfadanga")
print(f" {p1.name}  is  {p1.age} years  old and he is from {p1.address} ")
