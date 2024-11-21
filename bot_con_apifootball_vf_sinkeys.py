import tweepy
import requests
from datetime import datetime

# Fecha actual automática
fecha_actual = datetime.now().strftime("%Y-%m-%d")
season_current = datetime.now().strftime("%Y")
url = "X"
headers = {
    "X-RapidAPI-Key": "X",
    "X-RapidAPI-Host": "X"
}

def obtener_partido_hoy(equipo_id):
    params = {
        "team": equipo_id,
        "date": fecha_actual,
        "season": season_current
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
    consumer_key="X",
    consumer_secret="X",
    access_token="X",
    access_token_secret="X"
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

def obtener_partido_hoy(equipo_id):
    params = {
        "team": equipo_id,
        "date": fecha_actual,
        "season": "2024"
    }
    response = requests.get(url, headers=headers, params=params)
    print("URL solicitada:", response.url)  # Verifica los parámetros enviados
    print("Estado de la respuesta:", response.status_code)  # Verifica si la solicitud fue exitosa
    print("Respuesta completa de la API:", response.json())  # Muestra toda la respuesta
    
    data = response.json()

    if data['response']:
        fixture = data['response'][0]
        return (f"{fixture['teams']['home']['name']} juega hoy contra "
                f"{fixture['teams']['away']['name']} en "
                f"{fixture['fixture']['venue']['name']}.")
    else:
        return f"No hay partidos para el equipo con ID {equipo_id} hoy."
# cuenta de twitter @PinchaTriperoLP
