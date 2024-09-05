from datetime import datetime

# Original date string
date_str = "2024-09-04"

# Convert string to datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Convert datetime object to desired string format
formatted_date = date_obj.strftime("%Y-%B-%d")

print(formatted_date)  # Output: 2024-September-04
print(type(formatted_date))  # Output: <class 'str'>
print(formatted_date.split('-'))  # Output: ['2024', 'September', '04']