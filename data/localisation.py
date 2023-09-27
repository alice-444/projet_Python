import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

#country
num = "+330600000000"
myNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(myNum, "fr")
print (localisation)

#operator mobile
operator = phonenumbers.parse(num)
print(carrier.name_for_number(operator,"fr"))