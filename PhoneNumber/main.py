import phonenumbers

from phonenumbers import  geocoder

number = "+8801939649428"

ch_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import  carrier
service_name = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_name,"en"))