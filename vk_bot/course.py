import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url, params=payload)
xml = BeautifulSoup(response.content, 'html.parser')
def get_course(idn):
    try:
        yield str(xml.find("valute", {'id': idn}).value.text)
        yield str(xml.finde('valute', {'id': idn}.name.text))
    except:
        yield f"Такая валюта не найдена"