largest = -1
smallest = 1000000
while True:
    num = input("Enter a number: ")
    if num == "done": break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if largest < num:
        largest = num
        maximum = largest
    if smallest > num:
        smallest = num
        minimum = smallest

print("Maximum is", maximum)
print("Minimum is", minimum)
