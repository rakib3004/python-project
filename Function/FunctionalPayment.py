def computepay(h,f):
    if h > 40:
		pay = h * f + (h - 40.00) * (f *0.5)
	else:
    	pay = f * h
	return pay

h = input("Enter Hours:")
h = float(h)
r = input("Enter Rates:")
r = float(r)
p = computepay(h,r)
print("Pay",p)