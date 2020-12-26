import json

data = '''[
{"id ": "4101" ,
  "rating" : "1401" , 
  "ranking" : "154", 
  "star" : '4"},
{"id ": "4651" , 
 "rating" : "2484" ,
  "ranking" : "93",
   "star" :"7"}
]'''

neuralBioscope = json.loads(data)
print("Number of Data :",len(neuralBioscope))

for iData in neuralBioscope:
    print('ID :', iData['id'])
    print('RATING :', iData['rating'])
    print('RANKING :', iData['ranking'])
    print('STAR :', iData['star'])