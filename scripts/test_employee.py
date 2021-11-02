import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
  """Test cases for checking the behaviour of the Employee Class"""
  def setUp(self):
    f_name = "Ram"
    l_name = "Charan"
    salary = 20000
    self.employee = Employee(f_name, l_name, salary)

  def test_give_default_raise(self):
    """Tests that a default raise of 5000 is applied to Employee's salary"""
    self.employee.give_raise()
    self.assertEqual(self.employee.salary, 25000)

  def test_give_custom_raise(self):
    """Tests that a custom raise is accounted properly in Employee's salary"""
    self.employee.give_raise(2000)
    self.assertEqual(self.employee.salary, 22000)
    print("test passed!")

if __name__ == '__main__':
  unittest.main()
