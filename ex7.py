import requests
from bs4 import BeautifulSoup
url='https://www.aladin.co.kr/home/welcome.aspx'
response=requests.get(url)
# print(response.text)
soap=BeautifulSoup(response.text, 'html.parser')
result=soap.select('.sub')
# print(result)
for r in result:
    print(r.text)

