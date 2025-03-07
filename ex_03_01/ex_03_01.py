# Prompt the user to enter hours and rate per hour
str_hours = input('Enter Hours: ')
str_rate = input('Enter Rate: ')

# Convert input values to float
xp = float(str_hours) * float(str_rate)

# Calculate gross pay with overtime
if float(str_hours) > 40:
    overtime_hours = float(str_hours) - 40
    overtime_pay = overtime_hours * (float(str_rate) * 1.5)
    regular_pay = 40 * float(str_rate)
    xp = regular_pay + overtime_pay

# Print the total pay
print('Pay:', xp)

# Output:
# Enter Hours: 45
# Enter Rate: 10.50
# Pay: 498.75
