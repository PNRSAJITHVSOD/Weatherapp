import requests

api_key = '31ef246948c034219409e87a9c61b375'
city = 'Hyderabad'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()
print(data)


