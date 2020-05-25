class calc:
  def add(self, num1, num2):
    return num1 + num2
    
  def subtract(self, num1, num2):
    return num1 - num2
    
  def product(self, num1, num2):
    return num1 * num2
  
  def divide(self, num1, num2):
    return num1 / num2

if __name__ == "__main__":
  c = calc()
  print(c.add(20,10))
  print(c.subtract(20,10))
  print(c.product(20,10))
  print(c.divide(20,10))
