def computepay(h,f):
	pay = h*f
	if h>40 :
		array = (h - 40.0) * (f *0.5)
		pay = pay+array
	return pay


h = input("Enter Hours:")
h = float(h)
r = input("Enter Rates:")
r = float(r)
p = computepay(h,r)
print("Pay",p)