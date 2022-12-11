# ============ Q:5-Python Program for compound interest ==============


p = float(input("Enter Your Total Amout: "))
t = float(input("Enter Time in Years: "))
r = float(input("Enter Rate of Interest: "))
a = float()

a = p*(1 + (r/100))**t
ci = a - p

print(f"Your Total Compound Interest is {ci}")
