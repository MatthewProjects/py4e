# Prompt the user to enter hours and rate per hour
str_hours = input('Enter Hours: ')
str_rate = input('Enter Rate: ')

try:
    # Convert input values to float
    hours_worked = float(str_hours)
    hourly_rate = float(str_rate)
except:
    print("Error, Please enter numeric input")
    quit()

print(hours_worked, hourly_rate)

# Calculate gross pay with overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    regular_pay = 40 * hourly_rate
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours_worked * hourly_rate

# Print the total pay
print('Pay:', total_pay)

# Output:
# Enter Hours: 45
# Enter Rate: 10.50
# Pay: 498.75
