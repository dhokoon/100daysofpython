#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇




# greeting
print("Welcome to the tip calculator.")

# Get user input for total cost of bill
bill = float(input("What was the total bill? $"))

# calculate the cost of the tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# divide the total cost including tip amongst people in party
split = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / split

final_cost = round(bill_per_person, 2)
final_cost = "{:.2f}".format(bill_per_person)

# total of how much everyone owes
print(f"Each person should pay: ${final_cost}")
