# You can compute the tax as 8 percent of the meal amount and the tip as 10 percent of the meal amount (without the tax). 
# The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip.

costOfMeal=float(input("Enter the cost value:"))
tax = costOfMeal * 0.08
tip = costOfMeal * 0.10
total = tax + tip + costOfMeal
print("The tax is ",tax," $ and the tip is ",tip," $, making the total ", format(total,".2f")," $.",sep="")