#declaring the programs variables
userInput = None
total = None
count = 0

if (userInput == None): #checks for done
  userInput = input("Enter a number: ")
  while (userInput != "done") :
    try: #error exemption
      number = float(userInput)
      total[count] = number
      count += 1
      userInput = input("Enter a number: ")
    except:
      print("Invalid input")
      userInput = input("Enter a number: ")
print(min(total), max(total))

