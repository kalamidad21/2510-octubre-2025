\# 2510-Octubre 2025 · Mini-pipeline \*\*API → CSV → SQLite\*\* (Formación Continua)



Repositorio de práctica para asentar \*\*Git/GitHub\*\*, \*\*Python básico\*\* (ficheros, `pathlib`, `json`) y \*\*Data Pipelines\*\*: ingesta desde \*\*Open-Meteo (sin clave)\*\*, transformación a \*\*CSV\*\* y persistencia en \*\*SQLite\*\*, trabajando siempre con \*\*ramas + PR\*\*.



---



\## ✳️ Objetivos del mes (medibles)



1\. Hacer peticiones HTTP reales (`requests`) y \*\*guardar JSON\*\* en `data/`.

2\. Convertir \*\*JSON → CSV\*\* (Pandas o `csv`).

3\. Cargar \*\*CSV → SQLite\*\* y consultar.

4\. Publicar \*\*release etiquetada (v1.0)\*\* del mini-pipeline.



---



\## 🗂️ Estructura del repo (prevista)



```

.

├── README.md

├── api\_openmeteo.py          # S02: ingesta desde Open-Meteo (Murcia por defecto)

├── data/                     # Datos generados (JSON/CSV/DB)

│   └── .gitkeep              # (opcional) para versionar la carpeta vacía

├── docs/                     # Documentación ligera (roadmap, notas)

│   └── roadmap.md            # (opcional) Mapa sesiones ↔ plan

└── CHANGELOG.md              # (opcional) Cambios por release

```



> \*\*Regla:\*\* El \*\*código\*\* vive en la raíz (por ahora). Los \*\*datos generados\*\* SIEMPRE en `data/`.



---



\## 🧰 Requisitos



\* \*\*Python 3.10+\*\*

\* Conexión a Internet (para la API)

\* Librerías:



&nbsp; \* \*\*obligatoria ahora:\*\* `requests`

&nbsp; \* \*\*próximas sesiones:\*\* `pandas` (para CSV). `sqlite3` viene con Python.



---



\## ⚙️ Instalación rápida



\*\*Windows (PowerShell):\*\*



```powershell

\# (opcional) entorno virtual

py -m venv .venv

.\\.venv\\Scripts\\Activate.ps1



\# dependencias mínimas

py -m pip install --upgrade pip

py -m pip install requests

\# (próximo bloque) py -m pip install pandas

```



\*\*Linux/macOS (bash/zsh):\*\*



```bash

python3 -m venv .venv

source .venv/bin/activate



python -m pip install --upgrade pip

python -m pip install requests

\# (próximo bloque) python -m pip install pandas

```



---



\## ▶️ Uso rápido: \*\*`api\_openmeteo.py`\*\* (S02)



Descarga meteorología de \*\*Murcia\*\* y guarda un JSON fechado en `data/`.



```powershell

\# Desde la carpeta del repo

python api\_openmeteo.py    # o: py api\_openmeteo.py

```



\*\*Salida esperada (ejemplo):\*\*



```

Guardado: data/openmeteo\_murcia\_20250921\_1815.json

Claves horarias: \['time', 'temperature\_2m', 'relative\_humidity\_2m']

Muestras temp: \[24.1, 23.7, 23.5]

```



> \*\*Convención de nombre:\*\* `data/openmeteo\_<ciudad>\_YYYYMMDD\_HHMM.json`

> \*\*Zona horaria:\*\* `Europe/Madrid`.



---



\## 🌿 Flujo de trabajo con Git (siempre igual)



1\. Trabaja en \*\*`dev`\*\*



&nbsp;  ```powershell

&nbsp;  git switch dev

&nbsp;  ```

2\. Añade y comitea cambios atómicos



&nbsp;  ```powershell

&nbsp;  git add api\_openmeteo.py data/openmeteo\_\*.json

&nbsp;  git commit -m "feat: ingesta Open-Meteo (Murcia) y guardado JSON en data/"

&nbsp;  git push

&nbsp;  ```

3\. Abre \*\*Pull Request\*\* `dev → main` y \*\*merge\*\*.

4\. Sincroniza local:



&nbsp;  ```powershell

&nbsp;  git switch main

&nbsp;  git pull

&nbsp;  ```



> Mensajes de commit sugeridos (Conventional Commits): `feat:`, `fix:`, `docs:`, `chore:`…



---



\## 🗺️ Mapa \*\*Sesiones ↔ Plan Octubre\*\*



| Sesión | Semana (plan) | Objetivo observable                                   | Evidencias (ruta/artefacto)                                     | Estado |

| -----: | ------------- | ----------------------------------------------------- | --------------------------------------------------------------- | ------ |

|    S01 | Semana 1      | Ficheros con `pathlib` (TXT/JSON) + orden de proyecto | `data/ejemplo\_\*.txt/json` (mínimo 1)                            | ✅      |

|    S02 | Semana 2      | \*\*API sin clave → JSON en `data/`\*\* (Open-Meteo)      | `data/openmeteo\_murcia\_YYYYMMDD\_HHMM.json`                      |✅     |

|    S03 | Semana 3      | \*\*JSON → CSV\*\* (Pandas o `csv`)                       | `data/openmeteo\_murcia\_YYYYMMDD\_HHMM.csv`                       | ✅     |

|    S04 | Semana 4      | \*\*CSV → SQLite\*\* y \*\*release v1.0\*\*                   | `data/meteo.sqlite`, \*\*tag\*\* `v1.0`, `CHANGELOG.md` actualizado | ▶️     |



> Mantén esta tabla al día en cada PR.



---



\## 📑 Evidencias mínimas por bloque



\* \*\*S02\*\*: al menos \*\*1 JSON\*\* válido en `data/` con sello de fecha.

\* \*\*S03\*\*: \*\*1 CSV\*\* con columnas `time,temperature\_2m,relative\_humidity\_2m`.

\* \*\*S04\*\*: \*\*BD SQLite\*\* con una tabla `meteo\_hourly` + \*\*consulta de verificación\*\* documentada.



---



\## ✅ Checklist rápida (por PR)



\* \[ ] Código ejecuta sin errores

\* \[ ] Archivos generados van a `data/`

\* \[ ] Commit \*\*atómico\*\* y mensaje claro

\* \[ ] PR `dev → main` creado

\* \[ ] Actualicé esta tabla (Sesiones ↔ Plan) / README

\* \[ ] (si aplica) `CHANGELOG.md` actualizado



---



\## 🧪 Verificación manual (S02)



\* Ejecuta `api\_openmeteo.py` y confirma:



&nbsp; \* Se crea un archivo `data/openmeteo\_murcia\_\*.json`.

&nbsp; \* El JSON contiene `hourly.time`, `hourly.temperature\_2m`, `hourly.relative\_humidity\_2m`.

\* Abre el JSON y comprueba \*\*3 valores\*\* de ejemplo (no `null`).



---



\## 🆘 Problemas comunes



\* \*\*`ModuleNotFoundError: requests`\*\* → instala con `pip install requests` en el \*\*mismo\*\* entorno.

\* \*\*`403/timeout`\*\* → vuelve a ejecutar; revisa conexión y firewall; asegúrate de no bloquear `https://api.open-meteo.com`.

\* \*\*No aparece `data/`\*\* → el script la crea; si no, créala manualmente.

\* \*\*`git push` pide login\*\* → inicia sesión por navegador cuando lo solicite.



---



\## 📦 Próximos pasos



\* \*\*S03 (30–45’):\*\* convertir el JSON a \*\*CSV\*\* (`hora, temperatura, humedad`) y subir por PR.

\* \*\*S04 (60–90’):\*\* cargar el CSV a \*\*SQLite\*\*, documentar 1–2 consultas y publicar \*\*release v1.0\*\*.



---



\## ℹ️ Notas



\* Proyecto \*\*formativo\*\*; sin licencia de redistribución comercial.

\* Zona horaria de referencia: \*\*Europe/Madrid\*\*.

\* Si creas nuevos scripts o ciudades, sigue la convención de nombres y \*\*documenta\*\* en este README.



