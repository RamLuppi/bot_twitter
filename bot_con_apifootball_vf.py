import tweepy
import requests
from datetime import datetime, timedelta
from pytz import timezone
from decouple import config
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Fecha y zona horaria
zona_horaria_local = timezone("America/Argentina/Buenos_Aires")
fecha_actual = datetime.now(zona_horaria_local).strftime("%Y-%m-%d")
season_current = datetime.now().strftime("%Y")

# API Configuración
url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
headers = {
    "X-RapidAPI-Key": config("RAPIDAPI_KEY"),
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# Twitter configuración
client = tweepy.Client(
    consumer_key=config("CONSUMER_KEY"),
    consumer_secret=config("CONSUMER_SECRET"),
    access_token=config("ACCESS_TOKEN"),
    access_token_secret=config("ACCESS_TOKEN_SECRET")
)

def obtener_datos_fixture(equipo_id, desde, hasta):
    """Consulta la API y devuelve los datos del fixture."""
    params = {"team": equipo_id, "from": desde, "to": hasta, "season": season_current}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al hacer la solicitud a la API: {e}")
        return None

def obtener_partido_hoy(equipo_id):
    """Obtiene el partido de hoy para un equipo específico."""
    data = obtener_datos_fixture(
        equipo_id,
        fecha_actual,
        (datetime.now(zona_horaria_local) + timedelta(days=1)).strftime("%Y-%m-%d")
    )

    if not data or "response" not in data or not isinstance(data["response"], list):
        logging.warning("Formato inesperado en la respuesta de la API.")
        return "No se pudo obtener información."

    for fixture in data["response"]:
        fecha_utc = datetime.strptime(fixture["fixture"]["date"], "%Y-%m-%dT%H:%M:%S%z")
        fecha_local = fecha_utc.astimezone(zona_horaria_local).strftime("%Y-%m-%d")
        if fecha_local == fecha_actual:
            return (f"⚽ {fixture['teams']['home']['name']} 🆚 {fixture['teams']['away']['name']} "
                    f"🏟️ {fixture['fixture']['venue']['name']} 📅 {fecha_actual}.")
    
    return f"No hay partidos para el equipo con ID {equipo_id} hoy."

# IDs de los equipos
equipos = {
    450: "Estudiantes",
    434: "Gimnasia"
}

# Iterar sobre los equipos y publicar tweets
for equipo_id, equipo_nombre in equipos.items():
    mensaje = obtener_partido_hoy(equipo_id)
    if "No hay partidos" not in mensaje:
        client.create_tweet(text=mensaje)
        logging.info(f"Tweet publicado para {equipo_nombre}.")
    else:
        logging.info(f"Hoy no hay partido para {equipo_nombre}.")
