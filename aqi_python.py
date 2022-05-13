import requests
import urllib.parse
import time
from condition_for_air_results import Calc
api_key = "a798738eb14a6439ff0fc54014b1a69eb9fdd6e3"
is_continued=True
while (is_continued):
    print('''
    █▀▀ █░░ █ █▀▄▀█ ▄▀█ ▀█▀ █▀▀   █▄▄ █▀█ ▀█▀
    █▄▄ █▄▄ █ █░▀░█ █▀█ ░█░ ██▄   █▄█ █▄█ ░█░''')
    time.sleep(4)
    print("\n\n")
    print("Welcome to the CLIMATE BOT")
    print("Here are a few things that you can take advantage of using this: ")
    print("1. Air Quality Information of a city")
    print("2. Have a reference of the DATA TABLE for air quality index")
    print("3. To predict weather for the next 3 days")
    print("4. Climate Data Collected from 1880 to 2020 showing global temperature comparison")
    print("5. Water Quality Analysis using Machine Learning through python")
    print("6. Visit our Climate Action website")
    print("0. To exit the bot!")
    final_consent = int(input("\n\nChoose any number to start with:-: \n"))


    # 1. Air Quality Information

# ----------------------------------------------------------------------------------------------------

    if final_consent==1:
        city_name = input("Enter the name of the city: \n")
        url = f"https://api.waqi.info/feed/{city_name}/?token={api_key}"
        response = requests.get(url)
        json_data = response.json()
        air_quality_index = json_data['data']['aqi']
        carbon_monoxide = json_data['data']['iaqi']['co']['v']
        no2 = json_data['data']['iaqi']['no2']['v']
        hydrogen = json_data['data']['iaqi']['h']['v']
        o3 = json_data['data']['iaqi']['o3']['v']
        temp = json_data['data']['iaqi']['t']['v']

        print(f"The AQI of {city_name} is {air_quality_index}\nThe level of CO is {carbon_monoxide}\n"
              f"The level of NO2 is {no2}\nThe level of Hydrogen is {hydrogen}\n"
              f"The level of O3 is {o3}\n"f"The temperature of {city_name} is {temp}°C ")
        final_consent = input("\n\nDo you want to know if this air is breathable? Type 'Y' for yes and 'N' for no-: \n").lower()

    # ----------------------------------------------------------------------------------------------------

        if final_consent=='y':
        # Asks if it is good to breathe this air?

            time.sleep(1)

        # 2. Below code is extracted from file="condition_for_air_results"by creating CLASS
        # --> Code tells how healthy or unhealthy this air is for us.

            air_quality_index_checker=Calc(air_quality_index)
            air_quality_index_checker.is_air_safe()
            print("\nPlease Visit The Following Website For Solutions:")

        s = urllib.parse.quote(
            'timesofindia.indiatimes.com/life-style/health-fitness/health-news/effective-tips-to-prevent-yourself-from-smog-air-pollution/articleshow/61574445.cms')
        print('https://' + s)
        print('''
        ╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗
        ╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝''')

    # ----------------------------------------------------------------------------------------------------
# 3. To show the DATA TABLE for air quality index
    elif final_consent==2:
        time.sleep(5)
        from image_aqi import aqi_table
        consent=input(
                "Do you want to see the AQI table? Type 'Y' for Yes and 'N' for 'No:\n").upper()
        if consent=='Y':
            print("You can now see the table which is open in a new tab")
            aqi_table()
        print('''
        ╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗
        ╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝''')

    # ----------------------------------------------------------------------------------------------------

# 4. To predict weather for the next 3 days
    elif final_consent==3:
        time.sleep(1)
        from weather_prediction_3_days import weather_prediction
        weather_prediction()
        print('''
        ╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗
        ╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝''')

    # ----------------------------------------------------------------------------------------------------

# 5. Climate Data Collected from 1880 to 2020
    elif final_consent==4:
        consents=input("Do you want to see the graphical represantation of more than 100 years of data? Type 'Y' for Yes and 'N' for 'No:\n").upper()
        from Climate_data import datas
        if consents=='Y':
            datas()
            print('''
            ╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗
            ╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝''')

    # ----------------------------------------------------------------------------------------------------

# 6 Water Quality Analysis
    elif final_consent==5:
        consentra=input("Do you want to know the 'Water Data Analysis' of a large amount of data.Type 'Y' for Yes and 'N' for 'No:\n")
        if consentra=='y':
            from water_portability import machine_learn
            machine_learn()
    elif final_consent==6:
        cos=input("Do you want to visit our website.Type 'Y' for Yes and 'N' for 'No:\n").lower()
        if cos=='y':
            print("This is our website:-")
            s = urllib.parse.quote(
                'nilesh-d-yadav.github.io/mmmm/')
            print('https://' + s)
            print('''
                    ╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗
                    ╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝''')
    elif final_consent==0:
        print('''
███████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░███░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█
█░░▄▀░░░░░░▄▀░░███░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░█
█░░▄▀░░██░░▄▀░░█████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████░░▄▀░░█
█░░▄▀░░░░░░▄▀░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█
█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░░░░░█
█░░▄▀░░████░░▄▀░░███████░░▄▀░░███████░░▄▀░░████████████████
█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░░░░░█░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█
█░░░░░░░░░░░░░░░░███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░█
███████████████████████████████████████████████████████████
''')
        is_continued=False
        exit()

    # final_consent=int(input("\nChoose from the above numbers \n"))

