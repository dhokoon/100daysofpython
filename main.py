#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇




# greeting
print("Welcome to the tip calculator.\n")

# Get user input for total cost of bill
bill = float(input("What was the total bill?\n$ "))

# calculate the cost of the tip
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n "))

# divide the total cost including tip amongst people in party
split = int(input("How many people to split the bill?\n "))

bill_tip = bill * (1 + (tip / 100))
total_split = bill_tip / float(split)
sum = round(total_split, 2)
sum = "{:.2f}".format(sum)

# total of how much everyone owes
print(f"Each person should pay: ${sum}")
