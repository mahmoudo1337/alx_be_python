

def safe_divide(numerator, denominator):
    try:
      if denominator == 0:
          raise ZeroDivisionError("Error: Cannot divide by zero.")
      elif numerator != int or denominator != int:
          raise ValueError("Error: Please enter numeric values only.")
      else:
          return numerator / denominator
    except:
      print('An exception occurred')