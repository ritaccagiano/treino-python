import requests

token = "f47fe5e8e6ff04f8ad7c00175e799fc1"
region = input("Qual a sua região?: ")
date_br = input("Informe o mês da consulta (MM/YYYY): ")

url = f"http://apiadvisor.climatempo.com.br/api/v1/climate/region/{region}/days/90?token={token}"
response = requests.get(url)

data = response.json()

if "data" in data:
    for day in data["data"]:
        if day["date_br"] == date_br:
            print(f"Previsão para {day['date_br']}: {day['text_icon']['text']['phrase']} - Temperatura mínima: {day['temperature']['min']}°C - Temperatura máxima: {day['temperature']['max']}°C")
            print(f"Descrição da previsão: {day['text_icon']['text']['phrase_extended']}")
else:
    print("Não foi possível obter dados de previsão do tempo para a região e data informadas.")
      



    



