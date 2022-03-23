def compute_score(score):
  if (score >= 0.0 and score <= 1.0):
    if (score < 0.6):
      print("F")
    elif (score < 0.7):
      print("D")
    elif(score < 0.8):
      print("C")
    elif( score < 0.9):
      print("B")
    else:
      print("A")
  else:
    print("Bad score")

score = input("Enter score:")
try:
  score = float(score)
  compute_score(score)
except:
  print("Bad score")