import requests

# The code to predict the weather
def weather_prediction():
    answer = input("Do you want to know the weather for the upcoming days? Type 'Y' for Yes and 'N' for 'No:\n").upper()
    if answer=='Y':
        city=input('input the city name: \n').upper()
        print(f"Displaying weather for : {city}")
        url='https://wttr.in/{}'.format(city)
        res=requests.get(url)
        print(res.text)
