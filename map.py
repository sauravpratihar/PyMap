import requests
import json


loc1 = input("Enter Name of First Location: ");
loc2 = input("Enter Name of Second Location: ");


link = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+ loc1 + '&destinations='+ loc2 +'&key=AIzaSyAvuBm5IVu3vvoPDj4zh1Gef3SJBhvijvM'



f = requests.get(link)
d = json.loads(f.text)

print("")
print( d['origin_addresses'][0]+ " to "+d['destination_addresses'][0] )
print("Distance : " + str(d['rows'][0]['elements'][0]['distance']['text']))
print("Duration : " + str(d['rows'][0]['elements'][0]['duration']['text']))
print("")

