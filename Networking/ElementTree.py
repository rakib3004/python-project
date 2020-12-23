import xml.etree.ElementTree as ET

data = '''<person>
<name>Rakib</name>
<phone type="intl">11803004</phone>
<email hide="yes"/></person>'''

tree = ET.fromstring(data)
print('My Name is:', tree.find('name').text)
print('My Email Attribute is:',tree.find('email').get('hide'))