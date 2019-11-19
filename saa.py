import requests
import calendar

api_key = 'd45a4689c7ff92c093ee18f3c3dafac9'
api_call = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=oulu'
#'https://api.openweathermap.org/data/2.5/forecast?&q=Oulu&appid=d45a4689c7ff92c093ee18f3c3dafac9'
running = True

print('Welcome to Jaimes Subroto\'s 5 day weather forecast application using OpenWeatherMap\'s API!')

# Program loop
while running:

    json_data = requests.get(api_call).json()

    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }

    print('\n{city}, {country}'.format(**location_data))

    # The current date we are iterating through
    current_date = ''

    # Iterates through the array of dictionaries named list in json_data
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

        

        # Temperature is measured in Kelvin
        temperature = item['main']['temp']

        # Weather condition
        description = item['weather'][0]['description'],

        # Prints the description as well as the temperature in Celcius and Farenheit
        print('Weather condition: %s' % description)
        print('Celcius: {:.2f}'.format(temperature - 273.15))
        

    # Prints a calendar of the current month
    calendar = calendar.month(int(year), int(month))
    print('\n'+ calendar)

    # Asks the user if he/she wants to exit
    while True:
        running = input('Anything else we can help you with? ')
        if running.lower() == 'yes' or running.lower() == 'y':
            print('Great!')
            break
        elif running.lower() == 'no' or running.lower() == 'n' or running == 'exit':
            print('Thank you for using Jaimes Subroto\'s 5 day weather forecast application.')
            print('Have a great day!')
            running = False
            break
        else:
            print('Sorry, I didn\'t get that.')