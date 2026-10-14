day = int(input("enter 1 to 7 : "))
if day < 7 and day > 0 :
    pass
else:
  print("enter right value")
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
