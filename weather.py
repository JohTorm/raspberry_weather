# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests , json 
from datetime import datetime
import calendar

LANG = 'en'

# Enter your API key here 
api_key = "d45a4689c7ff92c093ee18f3c3dafac9"

# base_url variable to store url 
#base_url = "http://api.openweathermap.org/data/2.5/forecast/daily?"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# Give city name 
city_name = "Oulu" 

# complete_url variable to store 
# complete url address 
#complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units&metric"
#												Oulun id=643485			7 päivän ennuste
#complete_url = base_url + "appid=" + api_key + "&q=oulu&units&metric&cnt=7"
complete_url = 'api.openweathermap.org/data/2.5/forecast?appid=' + api_key + "&q=oulu"
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
json_data = response.json()
 
current_date = '' 

for item in json_data['list']:

        # Time of the weather data received, partitioned into 3 hour blocks
        time = item['dt_txt']

        # Split the time into date and hour [2018-04-15 06:00:00]
        next_date, hour = time.split(' ')

        # Stores the current date and prints it once
        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('\n{m}/{d}/{y}'.format(**date))
        
        # Grabs the first 2 integers from our HH:MM:SS string to get the hours
        hour = int(hour[:2])

        # Sets the AM (ante meridiem) or PM (post meridiem) period
        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        # Prints the hours [HH:MM AM/PM]
        print('\n%i:00 %s' % (hour, meridiem))

        # Temperature is measured in Kelvin
        temperature = item['main']['temp']

        # Weather condition
        description = item['weather'][0]['description'],

        # Prints the description as well as the temperature in Celcius and Farenheit
        print('Weather condition: %s' % description)
        print('Celcius: {:.2f}'.format(temperature - 273.15))
        print('Farenheit: %.2f' % (temperature * 9/5 - 459.67))

    # Prints a calendar of the current month
    # calendar = calendar.month(int(year), int(month))
    # print('\n'+ calendar)

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
# if x["cod"] != "404": 
  
    # # store the value of "main" 
    # # key in variable y 
    # y = x["main"] 
  
    # # store the value corresponding 
    # # to the "temp" key of y 
    # current_temperature = y["temp"] 
  
    # # store the value corresponding 
    # # to the "pressure" key of y 
    # current_pressure = y["pressure"] 
  
    # # store the value corresponding 
    # # to the "humidity" key of y 
    # current_humidiy = y["humidity"] 
  
    # # store the value of "weather" 
    # # key in variable z 
    # z = x["weather"] 
  
    # # store the value corresponding  
    # # to the "description" key at  
    # # the 0th index of z 
    # weather_description = z[0]["description"] 
  
    # # print following values 
    # print(" Temperature (in celsius unit) = " +
                    # str(current_temperature-273.15) + 
          # "\n atmospheric pressure (in hPa unit) = " +
                    # str(current_pressure) +
          # "\n humidity (in percentage) = " +
                    # str(current_humidiy) +
          # "\n description = " +
                    # str(weather_description)) 
  
# else: 
    # print(" City Not Found ")
