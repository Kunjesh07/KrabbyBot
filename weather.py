import requests


def return_weather(place):
     words = place.split(" ")
     r = data = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + words[1] + '&APPID=0216d3975efcbccb926efbaf5d521b86')
     weatherDetails = r.json()
     temp = weatherDetails["main"]["temp"]
     weatherDescription = weatherDetails["weather"][0]["description"]

     msg = "It is {temp} degrees with {desc}".format(temp=temp,desc=weatherDescription)
     return msg

