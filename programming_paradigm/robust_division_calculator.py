

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        result = num / denom
        return f"The result is {result}"
    except ValueError:
      return "Error: Please enter numeric values only."