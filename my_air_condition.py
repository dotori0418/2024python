# import requests
# service_key = 'JX5/3IWW8+bd78eXeDN1yeCrDVh8JsPpmSBJ+/Omf8nQNzYr8IBFJxMPRq+R5SeYq9yiHZ/jCBQ2KdEDaR5Jng=='
# url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
# params ={'serviceKey' : service_key, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '2.0' }

# response = requests.get(url, params=params)
# data=response.json()
# print(data['response']['body']['items'][0]['pm10Value'])
import requests
service_key = 'JX5/3IWW8+bd78eXeDN1yeCrDVh8JsPpmSBJ+/Omf8nQNzYr8IBFJxMPRq+R5SeYq9yiHZ/jCBQ2KdEDaR5Jng=='
url = 'http://apis.data.go.kr/6480000/gnPolcCntVsCrmnlOccrrncRtNdArrstRtDataService/getgnPolcCntVsCrmnlOccrrncRtNdArrstRtData'
params ={'serviceKey' : service_key, 'numOfRows' : '10', 'pageNo' : '1', 'resultType' : 'json' }

response = requests.get(url, params=params)
data=response.json()
print(data['getgnPolcCntVsCrmnlOccrrncRtNdArrstRtData'])