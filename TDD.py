import unittest


def add(num1, num2):
  return num1 + num2

class Test(unittest.TestCase):
  def test34(self):
    self.assertEqual(add(3,4), 7)
  def test67(self):
    self.assertEqual(add(6,7), 13)

  def setUp(self):
    print("running setUp")
  def tearDown(self):
    print("tests are done")

if __name__=="__main__":
  unittest.main()