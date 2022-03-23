def pay(rate, hours):
  if (hours > 40):
    overtime = hours - 40
    return ((hours - overtime) * rate + ((overtime*1.5) * rate))
  else:
    return (hours * rate)

hours = input("Enter your worked hours:")
rate = input("Enter your hour rate:")
hours = float(hours)
rate = float(rate)

payment = pay(rate, hours)
print("Pay: " + str(payment))



