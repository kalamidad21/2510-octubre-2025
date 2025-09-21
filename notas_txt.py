# notas_txt.py
import os

BASE_DIR = os.path.dirname(__file__) or "."
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

ruta_txt = os.path.join(DATA_DIR, "notas.txt")

# 1) Crear/escribir (sobrescribe si existe)
lineas = ["Primera nota", "Segunda nota"]
with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write("\n".join(lineas) + "\n")

# 2) Añadir al final
with open(ruta_txt, "a", encoding="utf-8") as f:
    f.write("Tercera nota\n")

# 3) Leer y mostrar
with open(ruta_txt, "r", encoding="utf-8") as f:
    contenido = f.read()

print("Contenido de notas.txt:\n" + contenido)
