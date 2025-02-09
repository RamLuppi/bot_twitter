# 🏆 Proyecto: Publicador Automático de Partidos de Fútbol en Twitter ⚽

Este proyecto automatiza la publicación de partidos de fútbol en Twitter para equipos específicos, utilizando la API de [API-Football](https://www.api-football.com/) y la biblioteca [Tweepy](https://www.tweepy.org/) para interactuar con la API de Twitter.

## 🚀 Características

- **Consulta de partidos**: Obtiene los partidos de fútbol programados para el día actual.
- **Publicación en Twitter**: Publica automáticamente en Twitter los partidos de los equipos configurados.
- **Manejo de errores**: Registra errores y advertencias en caso de problemas con las APIs.
- **Configuración flexible**: Utiliza variables de entorno para manejar claves de API y configuraciones sensibles.

## 🛠️ Requisitos

Para ejecutar este proyecto, necesitarás:

- Python 3.8 o superior.
- Una cuenta en [API-Football](https://www.api-football.com/) para obtener una clave API.
- Una cuenta de desarrollador de Twitter para obtener las claves de API de Twitter.
- Las siguientes bibliotecas de Python:
  - `tweepy`
  - `requests`
  - `python-decouple`
  - `pytz`

## 🔧 Instalación

1. Clona este repositorio en tu máquina local:
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2. Crea un archivo .env en la raíz del proyecto y añade las siguientes variables de entorno:
RAPIDAPI_KEY=tu_clave_api_football
CONSUMER_KEY=tu_consumer_key_de_twitter
CONSUMER_SECRET=tu_consumer_secret_de_twitter
ACCESS_TOKEN=tu_access_token_de_twitter
ACCESS_TOKEN_SECRET=tu_access_token_secret_de_twitter

3. Instala las dependencias necesarias:
pip install -r requirements.txt



🏃 Ejecución
Para ejecutar el script, simplemente corre:
python main.py
El script consultará los partidos de fútbol para los equipos configurados y publicará en Twitter si hay partidos programados para el día actual.

🧩 Estructura del Código
Configuración de logs: Se configura el logging para registrar eventos importantes.

Consulta a la API de fútbol: Se realiza una solicitud a la API de fútbol para obtener los partidos del día.

Publicación en Twitter: Si hay partidos, se publica un tweet con la información del partido.

🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar el proyecto, por favor abre un issue o envía un pull request.

📄 Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

¡Gracias por revisar este proyecto! Si te gusta, no olvides darle una ⭐ en GitHub.

