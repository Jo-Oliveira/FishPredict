import requests

def obter_tempo(latitude, longitude):
    url_tempo = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    url_mar = f"https://marine-api.open-meteo.com/v1/marine?latitude={latitude}&longitude={longitude}&current=wave_height"
    resposta_tempo = requests.get(url_tempo)
    resposta_mar = requests.get(url_mar)

    if resposta_tempo.status_code == 200:
        dados_tempo = resposta_tempo.json()
        temperatura = dados_tempo["current_weather"]["temperature"]
        vento = dados_tempo["current_weather"]["windspeed"]

    if resposta_mar.status_code == 200:
        dados_mar = resposta_mar.json()
        ondas = dados_mar["current"]["wave_height"]


        return {
            "temperatura" : temperatura,
            "vento" : vento,
            "ondas" : ondas
        }
    else:
        return None
