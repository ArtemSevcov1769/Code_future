import contextlib
import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url, params=payload)
htm = BeautifulSoup(response.content, 'html.parser')
@contextlib.contextmanager
def get_course(idn):
    b = str(htm.find("valute", {'id': str(idn)}).value.text)
    c = str(htm.find("valute", {'id': str(idn)}).find('name').text)
    d = str(htm.find("valute", {'id': str(idn)}).nominal.text)
    try:
        yield f'({d} шт.) {c} стоит(ят) {b}руб'
    except:
        yield f"Такая валюта не найдена"

a = input('Введите ID валюты:')
with get_course(a) as val:
    print(val)
