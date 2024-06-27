task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
reminder = f"Reminder: '{task} is a {priority} priority task that requires immediate attention today!'"
note = f"Note: '{task} is a {priority}. Consider completing it when you have free time.'"

match priority:
    case "high":
        if time_bound == "yes":  
            print(reminder)
        elif time_bound == "no":
            print(note)
    case "medium":
        if time_bound == "yes":  
            print(reminder)
        elif time_bound == "no":
            print(note)
    case "low":
        if time_bound == "no":
            print(note)
        elif time_bound == "yes":
            print(reminder)
    case _:
        print("Invalid Input")
        