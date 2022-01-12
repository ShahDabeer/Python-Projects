print("Welcome to the tip calculator!")
bill_total=input("What was the total bill? $")
bill_tot=int(bill_total)
tip=input("How much tip would you like to give? 10,12 or 15 ")
tip_tot=int(tip)
people=input("How many people to split the bill?")
people_tot=int(people)

bill_split=(bill_tot/people_tot)

pay = bill_split + (tip_tot/100*bill_split)
pay1=round(pay,2)
print(f"Each person should pay:${pay1}")