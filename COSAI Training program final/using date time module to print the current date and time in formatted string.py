from datetime import datetime

current_datetime = datetime.now()

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time:", formatted_datetime)
