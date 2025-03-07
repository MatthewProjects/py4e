# Prompt the user to enter hours and rate per hour
str_hours = input('Enter Hours: ')
str_rate = input('Enter Rate: ')

# Convert input values to float
hours = float(str_hours)
rate = float(str_rate)

# Calculate gross pay with overtime
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 * rate
    xp = regular_pay + overtime_pay
else:
    xp = hours * rate

# Print the total pay
print('Pay:', xp)

# Output:
# Enter Hours: 45
# Enter Rate: 10.50
# Pay: 498.75
