import phonenumbers
from phonenumbers import geocoder
ph=input("Enter the phone number(with country code as like +91.. :)") 
phone_number=phonenumbers.parse(ph)
print(geocoder.description_for_number(phone_number,'en'))
