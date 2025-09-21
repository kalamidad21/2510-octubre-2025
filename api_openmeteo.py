from pathlib import Path
from datetime import datetime
import json
import requests

# Murcia aprox.: 37.99, -1.13
LAT, LON = 37.99, -1.13

params = {
    "latitude": LAT,
    "longitude": LON,
    "hourly": "temperature_2m,relative_humidity_2m",
    "timezone": "Europe/Madrid",
}

headers = {"User-Agent": "fc-2510-ejercicio/1.0 (sin email)"}

resp = requests.get("https://api.open-meteo.com/v1/forecast", params=params, headers=headers, timeout=15)
resp.raise_for_status()  # lanza error si no es 200

data = resp.json()  # dict de Python

# Carpeta data/ junto al script
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M")
ruta = DATA_DIR / f"openmeteo_murcia_{stamp}.json"

with ruta.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Guardado:", ruta)
# Pequeña verificación
hourly = data.get("hourly", {})
print("Claves horarias:", list(hourly.keys())[:3])
print("Muestras temp:", hourly.get("temperature_2m", [])[:3])
