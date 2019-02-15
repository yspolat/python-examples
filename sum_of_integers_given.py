startValue = input("Enter start value:")

flag=0
check = True

for ch in startValue:
  if not("0" <= ch <= "9"):
    check = False
    break
    
if check:
  if(int(startValue) < 0 or int(startValue) > 100):
    print("Incorrect input for the start value!")
  else:
    stopValue = int(input("Enter stop value:"))
    sumVal = 0
    for x in range(int(startValue),stopValue):
      sumVal+=x
    print(sumVal)
else:
  print("Incorrect input for the start value!")