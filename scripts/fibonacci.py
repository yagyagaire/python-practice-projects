import unittest

def fibonacci(n):
  """Prints the fibonacci sequence upto nth items
  :param: int Number of items in the sequence
  :return: list of fibonacci numbers
  """
  if n < 1:
    return None
  if n == 1:
    return [0]
  if n == 2:
    return [0, 1]
  series = [0, 1]
  for i in range(2, n):
    series.append(series[i-2] + series[i-1])
  return series

n = int(input("Enter the length of Fibonacci Series: \n"))
series = '  '.join([str(el) for el in fibonacci(n)]) if fibonacci(n) is not None else 0
print(f"The fibonacci series upto {n} items is: \n {series}" if series else "Please enter a value greater than 0")


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci.fibonacci(0), None)
        self.assertEqual(fibonacci.fibonacci(1), [0])
        self.assertEqual(fibonacci.fibonacci(2), [0, 1])
        self.assertEqual(fibonacci.fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci.fibonacci(13), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(fibonacci.fibonacci(-4), None)

if __name__ == '__main__':
    unittest.main()
