data = 'From stephen@iit.du.ac.bd Jan 5 09:14:16'
aPosition = data.find('@')
print(aPosition)

bPosition = data.find('', aPosition)
print(bPosition)
mailId = data[aPosition+1 : bPosition]
print(mailId)