import requests
city_name='울산'
API_key='574b1ecbc402b6ca2771bfae0b542c09'
limit=5
url=f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'
res=requests.get(url)
loc_data=res.json()
# print(len(loc_data))
lat=loc_data[0]['lat']
lon=loc_data[0]['lon']
# print(lat,lon)
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
res=requests.get(url)
wea_data=res.json()
print(wea_data['weather'][0]['description'])#20122이재묵