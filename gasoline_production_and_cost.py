# Program that will prompt the user for a floating point number that stands for gallons of gasoline. 
# You will re-print that value along with other information about gasoline and gasoline usage:
# - number of liters
# - number of barrels of oil required to make this amount of gasoline
# - price in US dollars

# Here are some approximate conversion values:
# - 1 gallon is equivalent to 3.7854 liters
# - 1 barrel of oil approximately produces 19.5 gallons of gas
# - God knows what the cost should be, but let’s assume it $0.75/liter

gallon = 3.7854
barrel = 19.5
dollar_liter = 0.75

print("======= Current Price ======")
print("Gasoline Litter : ", dollar_liter, " $")

i_gallon_of_gas = float(input("Enter a number which stands for gallons of gasoline:"))
a = i_gallon_of_gas * gallon
b = i_gallon_of_gas / barrel
c = dollar_liter * a
print(i_gallon_of_gas," gallon(s) = ", a ," liter(s)", sep="")
print(b," barrel(s) of oil required to produce ", i_gallon_of_gas, " gallon(s) of gas", sep="")
print("It will cost ",c, " dollar(s).", sep="")