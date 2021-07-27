import requests
import os
from datetime import datetime

api_key = '902a66c1d423a1386b917ec8b421e4d6'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data["cod"] == "404" :
    print("Invalid City: {}, Please check your City name".format(location))
else:   
    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc is :",weather_desc)
    print ("Current Humidity is :",hmdt, '%')
    print ("Current wind speed is :",wind_spd ,'kmph')

    print("====================================================")


