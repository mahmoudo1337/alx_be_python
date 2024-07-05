from datetime import *

current_date = datetime.now()

def display_current_datetime():
    return current_date

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)