import requests

def get_weather(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        current_weather = data['current']
        temperature = current_weather['temp']
        weather_description = current_weather['weather'][0]['description']
        
        print(f"Temperature: {temperature}°C")
        print(f"Weather Description: {weather_description}")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    get_weather(api_key, lat, lon)
