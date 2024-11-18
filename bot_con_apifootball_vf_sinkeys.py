import tweepy
import requests
from datetime import datetime

# Fecha actual automática
fecha_actual = datetime.now().strftime("%Y-%m-%d")

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
headers = {
    "X-RapidAPI-Key": "x",
    "X-RapidAPI-Host": "x"
}

def obtener_partido_hoy(equipo_id):
    params = {
        "team": equipo_id,
        "date": fecha_actual,
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if data['response']:
        fixture = data['response'][0]
        return (f"{fixture['teams']['home']['name']} juega hoy contra "
                f"{fixture['teams']['away']['name']} en "
                f"{fixture['fixture']['venue']['name']}.")
    else:
        return f"No hay partidos para el equipo con ID {equipo_id} hoy."

# IDs de los equipos
id_estudiantes = 450
id_gimnasia = 434

# Mensajes a twittear
mensaje_estudiantes = obtener_partido_hoy(id_estudiantes)
mensaje_gimnasia = obtener_partido_hoy(id_gimnasia)

# Configuración de las claves de acceso para la API v2
client = tweepy.Client(
    consumer_key="x",
    consumer_secret="x",
    access_token="x-x",
    access_token_secret="x"
)

# Publicar tweets con la API v2 solo si hay partidos
if mensaje_estudiantes != "No hay partidos para el equipo con ID 450 hoy.":
    client.create_tweet(text=mensaje_estudiantes)
    print("Tweet publicado para Estudiantes.")
else:
    print("Hoy no hay partido de Estudiantes.")

if mensaje_gimnasia != "No hay partidos para el equipo con ID 434 hoy.":
    client.create_tweet(text=mensaje_gimnasia)
    print("Tweet publicado para Gimnasia.")
else:
    print("Hoy no hay partido de Gimnasia.")
