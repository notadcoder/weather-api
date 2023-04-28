import requests

# Enter your API key here
api_key = "YOUR_API_KEY"

# Enter the location for which you want to fetch the weather
location = input("Enter the location: ")

# Send an HTTP request to the OpenWeatherMap API to fetch weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
response = requests.get(url)

# Parse the JSON response to get the temperature and weather description
data = response.json()
temp = data["main"]["temp"]
weather = data["weather"][0]["description"]

# Convert the temperature from Kelvin to Celsius
temp_celsius = temp - 273.15

# Print the weather information to the user
print(f"The temperature in {location} is {temp_celsius:.2f}°C and the weather is {weather}.")
