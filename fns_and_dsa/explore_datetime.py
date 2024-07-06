from datetime import *

current_date = datetime.strptime(datetime.now(), "%y-%m-%d %H:%M:%S")

def display_current_datetime():
    return current_date

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.strptime(current_date + timedelta(days=number_of_days), "%y-%m-%d %H:%M:%S")
    return future_date