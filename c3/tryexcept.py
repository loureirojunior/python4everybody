# Getting the hour input from user
try:
  hours = input("Enter your worked hours:")
  hours = float(hours)
  rate = input("Enter your hour rate:")
  rate = float(rate)

# Calculating the total pay:
  overHours = 0
  overPay = 0

  if (hours > 40):
    overHours = hours - 40
    overPay = (overHours * rate)*1.5

  pay = ((hours - overHours) * rate) + overPay

# Prints the pay to the user
  print("Pay: " + str(pay))

except:
  print("Error, please enter numeric input")