import requests
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt

API_KEY = "21d26b4a54e7128929ed2bb80e3e036b"


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

states = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

weather_list = []



for state, city in states.items():


    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    print("\nAPI URL :")
    print(url)

    response = requests.get(url)


    print("Status Code :", response.status_code)


    if response.status_code == 200:

        data = response.json()

        weather_data = {
            "State": state,
            "Capital": city,
            "Temperature": data["main"]["temp"],
            "Feels_Like": data["main"]["feels_like"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
            "Weather": data["weather"][0]["description"],
            "Wind_Speed": data["wind"]["speed"],
            "Clouds": data["clouds"]["all"],
            "Visibility": data.get("visibility", "N/A")
        }

        weather_list.append(weather_data)

        print("Data Fetched Successfully")

    else:

        print("API Error")
        print(response.json())


    time.sleep(1)

df = pd.DataFrame(weather_list)


df.to_csv("india_weather_data.csv", index=False)



print("\nComplete Weather Data")
print(df)

print("\nCSV File Saved Successfully")

plt.figure(figsize=(15, 8))
sns.barplot(x='Capital', y='Temperature', data=df)
plt.xlabel('Capital City')
plt.ylabel('Temperature (°C)')
plt.title('Current Temperature in Indian Capital Cities')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


plt.figure(figsize=(18, 10))
heatmap_data = df.set_index('Capital')[['Temperature', 'Humidity', 'Wind_Speed', 'Pressure']]
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".1f", linewidths=.5)
plt.title('Weather Parameters Heatmap Across Indian Capital Cities')
plt.xlabel('Weather Parameter')
plt.ylabel('Capital City')
plt.tight_layout()
plt.show()
plt
