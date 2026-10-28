import requests


def obter_tempo(latitude, longitude):
    url_tempo = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    url_mar = f"https://marine-api.open-meteo.com/v1/marine?latitude={latitude}&longitude={longitude}&current=wave_height"
    try:
        resposta_tempo = requests.get(url_tempo, timeout = 10)
        resposta_mar = requests.get(url_mar, timeout = 10)
    except requests.exceptions.RequestException:
        return None

    if resposta_tempo.status_code == 200 and resposta_mar.status_code == 200:
        try:
            dados_tempo = resposta_tempo.json()
            dados_mar = resposta_mar.json()
            temperatura = dados_tempo["current_weather"]["temperature"]
            vento = dados_tempo["current_weather"]["windspeed"]
            ondas = dados_mar.get("current", {}).get("wave_height", None)
        except (KeyError, TypeError):
            return None

        return {
            "temperatura" : temperatura,
            "vento" : vento,
            "ondas" : ondas
        }
    else:
        return None

