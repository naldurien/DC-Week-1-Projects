total = input("What is your total?")
float_total = float(total)
tip_percent = input("What percentage would you like to tip (as a whole number)?")
float_tip_percent = float(tip_percent)/100
tip = float_total * float_tip_percent
print(f"Your tip amount is ${tip}")
