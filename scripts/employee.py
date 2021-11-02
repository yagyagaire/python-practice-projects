class Employee:
  """A class representing an employee"""
  def __init__(self, first_name, last_name, salary):
    self.f_name = first_name
    self.l_name = last_name
    self.salary = salary

  def give_raise(self, raise_amt=5000):
    self.salary += raise_amt

  def __str__(self):
    return f"Employee {self.f_name.title()} {self.l_name.title()}"
