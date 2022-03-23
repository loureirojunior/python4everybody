hours = input("Enter your worked hours:")
rate = input("Enter your hour rate:")
hours = float(hours)
rate = float(rate)

overHours = 0
overPay = 0

if (hours > 40):
  overHours = hours - 40
  overPay = (overHours * rate)*1.5

pay = ((hours - overHours) * rate) + overPay
print("Pay: " + str(pay))
