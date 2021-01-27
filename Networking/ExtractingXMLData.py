import xml.etree.ElementTree as ET

iInput ='''<stuff>
<users>
<user x="2">
<id>001</id>
<name>Shihab</name>
</user>
<user x="2">
<id>002</id>
<name>Rakib</name>
</user>
</users>
</stuff>'''

stuff = ET.fromstring(iInput)
lst = stuff.findall('users/user')
print('User Count:',len(lst))
for item in lst:
    print('Name:',item.find('name').text)
    print('Id:',item.find('id').text)
    print('Attribute:',item.get("x"))