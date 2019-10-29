class MathDojo:
  def __init__(self):
    self.result = 0
  def add(self, num, *nums):
    self.result += num 
    for number in nums:
      self.result += number
    return self
  def subtract(self, num, *nums):
    self.result -= num
    for number in nums:
      self.result -= number
    return self



#start TDD
import unittest

class MathTest(unittest.TestCase):
  def setUp(self):
    print("Creating MathDojo obj")
    self.md = MathDojo()

  def testAdd(self):
    self.assertEqual(self.md.add(1,2,3,4,5,6).result, 1+2+3+4+5+6)

  def testSubstract(self):
    self.assertEqual(self.md.subtract(1,2,3,4,5,6).result, -1-2-3-4-5-6)
  
  def tearDown(self):
    print("Done")

if __name__ == "__main__":
  unittest.main()


