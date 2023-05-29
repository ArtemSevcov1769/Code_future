import contextlib
import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url, params=payload)
htm = BeautifulSoup(response.content, 'xml')
@contextlib.contextmanager
def get_course(idn):
    b = str(htm.find("Valute", {'ID': str(idn)}).Value.text)
    c = str(htm.find("Valute", {'ID': str(idn)}).find('Name').text)
    d = str(htm.find("Valute", {'ID': str(idn)}).Nominal.text)
    try:
        yield f'({d} шт.) {c} стоит(ят) {b}руб'
    except:
        yield f"Такая валюта не найдена"

a = input('Введите ID валюты:')
with get_course(a) as val:
    print(val)
