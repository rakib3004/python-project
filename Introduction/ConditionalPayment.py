#Calculate pay
hrs = input("Enter Hours:")
h = float(hrs)
f = input("Enter Pay Rate:")
f = float(f)
if h > 40:
    pay = h * f + ((h - 40.00) * (f * .5))
else:
    pay = f * h
print(pay)