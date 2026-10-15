import requests

# taking user input for coordinates
lat = input("Enter latitude - ")
lon = input("Enter longitude - ")

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

try:
    response = requests.get(url, timeout=10)
    
    # checking status code
    if response.status_code != 200:
        print("Failed to get data, status code:", response.status_code)
    else:
        data = response.json()
        
        # extracting required values
        timezone = data.get("timezone")
        current = data.get("current_weather", {})
        temp = current.get("temperature")
        wind = current.get("windspeed")
        code = current.get("weathercode")
        
        # summary text
        summary = (
            "*** Weather Report ***\n"
            f"Timezone: {timezone}\n"
            f"Temperature: {temp} °C\n"
            f"Windspeed: {wind} km/h\n"
            f"Weather Code: {code}\n"
        )
        print(summary)
        
        # saving into text file
        f = open("weather_report.txt", "w")
        f.write(summary)
        f.close()
        print("Report successfully saved to weather_report.txt")

except requests.exceptions.RequestException as e:
    print("Network error occurred:", e)