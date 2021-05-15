wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for val,clth in wardrobe.items():
	for data in clth:
		print("{} {}".format(data,val))