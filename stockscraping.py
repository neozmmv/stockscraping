from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests

def getstock(link) -> str:
    stock_url = link
    stock_result = requests.get(stock_url)
    stock = BeautifulSoup(stock_result.text, "html.parser")
    stock_value = stock.find("div", {"class": "BNeawe iBp4i AP7Wnd"})
    return stock_value.text

def tofloat(value) -> float:
    varfloat = value.split(" ")[0].replace(",", ".")
    return float(varfloat)

now = datetime.now()
print(f"Start: {now.strftime('%d/%m/%Y %H:%M:%S')}")

with open("stockdata.csv", "a") as database:
    while True:
        now = datetime.now()
        try:
            PETR4_value = getstock("https://www.google.com/search?client=firefox-b-d&q=petr4").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, PETR4: {PETR4_value}\n")
        except AttributeError:
            print(f"Erro em PETR4 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            BBAS3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=BVMF%3A+BBAS3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, BBAS3: {BBAS3_value}\n")
        except AttributeError:
            print(f"Erro em BBAS3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            ITUB4_value = getstock("https://www.google.com/search?client=firefox-b-d&q=itub4").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, ITUB4: {ITUB4_value}\n")
        except AttributeError:
            print(f"Erro em ITUB4 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            VALE3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=vale3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, VALE3: {VALE3_value}\n")
        except AttributeError:
            print(f"Erro em VALE3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            ABEV3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=abev3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, ABEV3: {ABEV3_value}\n")
        except AttributeError:
            print(f"Erro em ABEV3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            SANB11_value = getstock("https://www.google.com/search?client=firefox-b-d&q=sanb11").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, SANB11: {SANB11_value}\n")
        except AttributeError:
            print(f"Erro em SANB11 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            ITSA4_value = getstock("https://www.google.com/search?client=firefox-b-d&q=itsa4").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, ITSA4: {ITSA4_value}\n")
        except AttributeError:
            print(f"Erro em ITSA4 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            BBDC3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=bbdc3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, BBDC3: {BBDC3_value}\n")
        except AttributeError:
            print(f"Erro em BBDC3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            GOAU4_value = getstock("https://www.google.com/search?client=firefox-b-d&q=goau4").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, GOAU4: {GOAU4_value}\n")
        except AttributeError:
            print(f"Erro em GOAU4 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            ELET3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=elet3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, ELET3: {ELET3_value}\n")
        except AttributeError:
            print(f"Erro em ELET3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            CXSE3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=cxse3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, CXSE3: {CXSE3_value}\n")
        except AttributeError:
            print(f"Erro em CXSE3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            WEGE3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=wege3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, WEGE3: {WEGE3_value}\n")
        except AttributeError:
            print(f"Erro em WEGE3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            ASAI3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=asai3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, ASAI3: {ASAI3_value}\n")
        except AttributeError:
            print(f"Erro em ASAI3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            BPAC11_value = getstock("https://www.google.com/search?client=firefox-b-d&q=bpac11").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, BPAC11: {BPAC11_value}\n")
        except AttributeError:
            print(f"Erro em BPAC11 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            RADL3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=radl3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, RADL3: {RADL3_value}\n")
        except AttributeError:
            print(f"Erro em RADL3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            PSSA3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=pssa3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, PSSA3: {PSSA3_value}\n")
        except AttributeError:
            print(f"Erro em PSSA3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            RENT3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=rent3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, RENT3: {RENT3_value}\n")
        except AttributeError:
            print(f"Erro em RENT3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            EMBR3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=embr3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, EMBR3: {EMBR3_value}\n")
        except AttributeError:
            print(f"Erro em EMBR3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            EGIE3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=egie3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, EGIE3: {EGIE3_value}\n")
        except AttributeError:
            print(f"Erro em EGIE3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass
        try:
            GRND3_value = getstock("https://www.google.com/search?client=firefox-b-d&q=grnd3").replace(",", ".")
            database.write(f"{now.strftime('%d/%m/%Y %H:%M:%S')}, GRND3: {GRND3_value}\n")
        except AttributeError:
            print(f"Erro em GRND3 {now.strftime('%d/%m/%Y %H:%M:%S')}")
            pass