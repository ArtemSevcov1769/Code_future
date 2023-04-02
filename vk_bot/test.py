import requests
from bs4 import BeautifulSoup

for i in range(2007, 2024):
    url = "https://cbr.ru/scripts/XML_daily.asp?date_req=03/02/" + str(i)
    responce = requests.get(url)
    xml = BeautifulSoup(responce.content, "html.parser")

    def getCourse(id):
        return xml.find("valute", {"id" : id}).value.text

    dollar = (getCourse("R01235") + " Доллар США")
    euro = (getCourse("R01239") + " Евро")
    uan = (getCourse("R01375") + " Китайский юань")
    tenge = (getCourse("R01335") + " Казахстанских тенге")
    eyn = (getCourse("R01820") + " Японских иен")
    funt = (getCourse("R01035") + " Фунт стерлингов Соединенного королевства")

