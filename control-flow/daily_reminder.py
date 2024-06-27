task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
reminder = "'{task}' is a {priority} priority task that requires immediate attention today!"

match priority:
    case "high":
        if time_bound == "yes":  
            print(f"Reminder: ", reminder)
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority}. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":  
            print(f"Reminder: ", reminder)
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority}. Consider completing it when you have free time.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        elif time_bound == "yes":
            print(f"Reminder: ", reminder)
    case _:
        print("Invalid Input")
        