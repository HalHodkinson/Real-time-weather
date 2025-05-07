import requests
from geopy import GoogleV3


while True: #loop the program until break reached
    print()
    place_name = input('Input the location you want a current weather report from?: ') #get location from user
    geolocator = GoogleV3(api_key = 'YOUR_API_KEY') #access google maps geocode API
    coordinates = geolocator.geocode(place_name) #geocode (place name to coordinates)

    if coordinates: #error handle an unrecognised location input
        google_maps_api_key = 'YOUR_API_KEY' #google maps API key
        lat = coordinates.latitude #latitude
        lon = coordinates.longitude #longitude
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={google_maps_api_key}' #API request for current weather

        response = requests.get(url) #get response from API
        data = response.json() #get data in JSON format

        #get stats from json output
        place_name = data['name']

        country = data['sys']['country']

        description_no_caps = data['weather'][0]['description']
        description = description_no_caps.capitalize() #capitalise the first letter of the string

        temp_kelvin = data['main']['temp']
        temp_celcius = round(temp_kelvin - 273.15,1) #convert from kelvin to celcius

        wind_speed = data['wind']['speed']
        wind_speed_mph = round((wind_speed * 3600)/1609.34,2) #convert m/s to mph

        wind_direction = data['wind']['deg']

        #print summary
        print()
        print(f'Location: {place_name}, {country}')
        print(f'Description: {description}')
        print(f'Current temperature: {temp_celcius} celcius')
        print(f'Wind direction: {wind_direction} degrees')
        print(f'Wind speed: {wind_speed} m/s or {wind_speed_mph} mph')

        #option to exit while loop
        print()
        exit_loop = input('Press enter to continue or q to quit program. ')
        if exit_loop == 'q':
            break
        else:
            continue

    else:
        print()
        exit_loop = input(f'Didnt recognise location {place_name}. Press enter to enter another location or q to quit. ')
        if exit_loop == 'q':
            break
        else:
            continue
