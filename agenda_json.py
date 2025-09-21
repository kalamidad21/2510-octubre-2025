# agenda_json.py
import os, json

BASE_DIR = os.path.dirname(__file__) or "."
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

ruta_json = os.path.join(DATA_DIR, "agenda.json")

agenda = [
    {"nombre": "Ana", "tel": "600111222"},
    {"nombre": "Luis", "tel": "600333444"},
]

# Guardar JSON legible
with open(ruta_json, "w", encoding="utf-8") as f:
    json.dump(agenda, f, ensure_ascii=False, indent=2)

# Leer JSON y reportar
with open(ruta_json, "r", encoding="utf-8") as f:
    agenda_leida = json.load(f)

print(f"Contactos guardados: {len(agenda_leida)}")
