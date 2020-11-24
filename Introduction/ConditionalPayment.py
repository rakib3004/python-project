hrs = input("Enter Hours:")
h = float(hrs)
f=1.5
if h<40 :
    pay = h*f
else :
    f=10.50
    pay = h*f
print(pay)