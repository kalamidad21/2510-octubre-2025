from pathlib import Path
import sqlite3, pandas as pd

BASE = Path(__file__).parent
DB = BASE / "data" / "clima.db"
TABLE = "mediciones"

if not DB.exists() or DB.stat().st_size == 0:
    raise SystemExit(f"❌ DB no encontrada o vacía: {DB}")

with sqlite3.connect(DB) as con:
    tabs = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table';")]
    if TABLE not in tabs:
        raise SystemExit(f"❌ No existe la tabla '{TABLE}'. Tablas: {tabs}")

    head = pd.read_sql(f"SELECT * FROM {TABLE} ORDER BY time LIMIT 5;", con)
    stats = pd.read_sql(
        f"""SELECT COUNT(*) AS rows,
                   MIN(time) AS min_time,
                   MAX(time) AS max_time,
                   ROUND(AVG(temperature_2m),2) AS avg_temp,
                   ROUND(AVG(relative_humidity_2m),2) AS avg_rh
            FROM {TABLE};""", con)

print("== HEAD =="); print(head.to_string(index=False))
print("\n== STATS =="); print(stats.to_string(index=False))
