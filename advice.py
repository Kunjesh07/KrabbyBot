import requests

# return advice
def return_advice():
    r = requests.get('https://api.adviceslip.com/advice')
    if r.status_code == 200:
        data = r.json();
        advice = data["slip"]["advice"]
    return advice