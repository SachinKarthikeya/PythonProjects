import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

number = input("Enter the phone number with country code: ")

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(f"Location: {location}")

service = phonenumbers.parse(number)
provider = carrier.name_for_number(service, "en")
print(f"Provider: {provider}")

key = "7d8ddc230dad4a59b51b3a251f7f8846"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"Coordinates: {lat, lng}")

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("location.html")