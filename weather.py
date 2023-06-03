import pyowm
import requests
from pyowm import owm
from key import Token

# Configura la URL de la API y los parámetros de la solicitud
url = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Buenos Aires,AR',  # Reemplaza con la ubicación deseada en Argentina
    'appid': Token,  # Reemplaza con tu propia API key de OpenWeatherMap
    'units': 'metric'  # Configura las unidades de temperatura a Celsius
}

# Realiza la solicitud GET a la API de OpenWeatherMap
response = requests.get(url, params=params)
data = response.json()

# Extrae los datos del clima de la respuesta JSON
temperatura = data['main']['temp']
humedad = data['main']['humidity']
estado_cielo = data['weather'][0]['description']

#registramos en OpenWeatherMap
owm = pyowm.OWM (Token)

#obtenemos la información del clima
ubicacion = 'Buenos Aires, AR'

# Imprime los datos del clima
print(f'Temperatura: {temperatura}°C')
print(f'Humedad: {humedad}%')
print(f'Estado del cielo: {estado_cielo}')