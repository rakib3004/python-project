import json

data = '''{
"name" : "Rakib",
"phone" : {
"type" :  "intl",
"number" : "11803004"
},
"email" : {
"hide" : "yes"
}
}'''

info = json.loads(data)

print('Name :', info["name"])
print('Hide :', info["email"]["hide"])
print('Phone number:', info["phone"]["number"])