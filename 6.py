# ========== Q:6-Python Program to check Armstrong Number ============


num = int(input("Enter Your Number: "))
s=num
sum1=0

while num!=0:
  r=num%10
  sum1=sum1+(r*r*r)
  num=num//10 

if s==sum1:
  print(f"The Number {s} is Armstrong Number")
else:
  print(f"The Number {s} is not Armstrong Number")
