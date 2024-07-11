

def safe_divide(numerator, denominator):
    try:
      if denominator == 0:
          raise ZeroDivisionError("Error: Cannot divide by zero.")
      elif numerator != int or denominator != int:
          raise ValueError("Error: Please enter numeric values only.")
      else:
          print(f"The result of the division is {float(numerator) / float(denominator)}") 
    except:
      print('An exception occurred')