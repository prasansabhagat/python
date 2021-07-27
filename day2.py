print("Welcome to the tip calculator😎")
total = float(input("What is the total expenditure? Rs"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
split_to = int(input("How many people to split the bill?"))
bill = (total + total*(tip/100))/split_to
bill_final = round(bill,2)
print(f"Each person should pay: Rs {bill_final} " )
#print("Each person should pay: Rs" + bill_final)
#25/07/21