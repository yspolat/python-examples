first_coefficient = int(input("Please enter 1st coefficient (a): "))

if first_coefficient == 0:
  print("1st coefficient (a) can't be 0!")
else:
  second_coefficient = int(input("Please enter 2nd coefficient (b): "))
  third_coefficient = int(input("Please enter 3rd coefficient (c): "))
  determinant = (second_coefficient * second_coefficient) - (4 * first_coefficient * third_coefficient)
  print("Discriminant of this equation is ", determinant,".",sep="")
  
  if determinant > 0:
    print("There are two distinct roots.")
  elif determinant == 0:
    print("There is exactly one root.")
  else:
    print("There are no real roots.")
