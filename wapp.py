import requests
import json
city = input("City Name: ")
url = f"http://api.weatherapi.com/v1/current.json?key=8de403809a3b406e8eb195106240902&q={city}"
response = requests.get(url)
weather_data = response.json()
current_weather = weather_data.get("current", {})
temperature_celsius = current_weather.get("temp_c")
humidity = current_weather.get("humidity")
print("Temperature (C):", temperature_celsius,"°C")
print("Humidity:", humidity)
option = int(input("Select an option:\n1. Wind Speed (kph)\n2. Wind Speed (mph)\n3. Wind Degree\n4. Wind Direction\n5. Pressure (mb)\n6. Pressure (in)\n7. Precipitation (mm)\n8. Precipitation (in)\n9. Cloud\n10. Feels Like (C)\n11. Feels Like (F)\n12. Visibility (km)\n13. Visibility (miles)\n14. UV\n15. Wind Gust (mph)\n16. Wind Gust (kph)\n0. Exit\nEnter option number: "))
match option:
    case 1:
        wind_speed_kph = current_weather.get("wind_kph")
        print("Wind Speed (kph):", wind_speed_kph)
    case  2:
        wind_speed_mph = current_weather.get("wind_mph")
        print("Wind Speed (mph):", wind_speed_mph)
    case  3:
        wind_degree = current_weather.get("wind_degree")
        print("Wind Degree:", wind_degree)
    case 4:
        wind_dir = current_weather.get("wind_dir")
        print("Wind Direction:", wind_dir)
    case 5:
        pressure_mb = current_weather.get("pressure_mb")
        print("Pressure (mb):", pressure_mb)
    case 6:
        pressure_in = current_weather.get("pressure_in")
        print("Pressure (in):", pressure_in)
    case 7:
        precip_mm = current_weather.get("precip_mm")
        print("Precipitation (mm):", precip_mm)
    case 8:
        precip_in = current_weather.get("precip_in")
        print("Precipitation (in):", precip_in)
    case 9:
        cloud = current_weather.get("cloud")
        print("Cloud:", cloud)
    case 10:
        feels_like_c = current_weather.get("feelslike_c")
        print("Feels Like (C):", feels_like_c)
    case 11:
        feels_like_f = current_weather.get("feelslike_f")
        print("Feels Like (F):", feels_like_f)
    case 12:
        vis_km = current_weather.get("vis_km")
        print("Visibility (km):", vis_km)
    case 13:
        vis_miles = current_weather.get("vis_miles")
        print("Visibility (miles):", vis_miles)
    case 14:
        uv = current_weather.get("uv")
        print("UV:", uv)
    case 15:
        wind_gust_mph = current_weather.get("gust_mph")
        print("Wind Gust (mph):", wind_gust_mph)
    case 16:
        wind_gust_kph = current_weather.get("gust_kph")
        print("Wind Gust (kph):", wind_gust_kph)
    case 0:
        print("Exiting...")
    case _:
        print("Invalid option")
