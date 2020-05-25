import unittest
import calc

class test_calc(unittest.TestCase):
  def setUp(self):
    self.calc = calc.calc()
 
  def tearDown(self):
    pass
    
  def test_add(self):
    self.assertEqual(self.calc.add(20,10), 30)
    
  def test_subtract(self):
    self.assertEqual(self.calc.subtract(20,10), 10)
 
  def test_product(self):
    self.assertEqual(self.calc.product(20, 10), 200)
    
  def test_divide(self):
    self.assertEqual(self.calc.divide(20,10), 2)
    
  def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
      self.calc.divide(20,0)

if __name__ == "__main__":
	unittest.main()
