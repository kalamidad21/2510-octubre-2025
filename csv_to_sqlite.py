from pathlib import Path
import argparse, sqlite3, pandas as pd

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

DB = DATA / "clima.db"
TABLE = "mediciones"

ALIASES = {
    "time": {"time","fecha","datetime","date","hora","timestamp"},
    "temperature_2m": {"temperature_2m","temperature","temp","temperatura","temperatura_2m","t2m"},
    "relative_humidity_2m": {"relative_humidity_2m","humidity","humedad_relativa","rh","relativehumidity_2m"},
}

def pick_csv():
    # El CSV más reciente con tamaño > 0 en data/
    csvs = [p for p in DATA.glob("*.csv") if p.stat().st_size > 0]
    return max(csvs, key=lambda p: p.stat().st_mtime) if csvs else None

def normalize_columns(df):
    cols = {c.lower().strip(): c for c in df.columns}
    mapping = {}
    for target, candidates in ALIASES.items():
        found = next((c for c in candidates if c in cols), None)
        if found: mapping[target] = cols[found]
    # 'time' y 'temperature_2m' son obligatorias; humedad la rellenamos si falta
    if "time" not in mapping or "temperature_2m" not in mapping:
        raise SystemExit(f"❌ Columnas detectadas: {list(df.columns)}\n"
                         f"Se requieren al menos 'time' y 'temperature_2m' (aceptamos alias).")
    if "relative_humidity_2m" not in mapping:
        df["relative_humidity_2m"] = pd.NA
        mapping["relative_humidity_2m"] = "relative_humidity_2m"
        print("⚠️ No encontré humedad; se importará como vacío.")
    # Renombra a estándar
    return df.rename(columns={v:k for k,v in mapping.items()})[["time","temperature_2m","relative_humidity_2m"]]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", help="Ruta CSV; si no, se usa el más reciente en data/")
    args = ap.parse_args()

    src = Path(args.csv) if args.csv else pick_csv()
    if not src or not src.exists() or src.stat().st_size == 0:
        raise SystemExit("❌ No encuentro un CSV válido en data/. Genera uno o pasa --csv.")

    # Detecta separador automáticamente
    df = pd.read_csv(src, encoding="utf-8", engine="python", sep=None)
    print(f"ℹ️ CSV: {src.name} | filas={len(df)} | columnas={list(df.columns)}")

    df_std = normalize_columns(df)

    with sqlite3.connect(DB) as con:
        df_std.to_sql(TABLE, con, if_exists="replace", index=False)
        con.execute("CREATE INDEX IF NOT EXISTS idx_med_time ON mediciones(time);")
        con.commit()

    print(f"✅ Importado a {DB.resolve()} | tabla={TABLE} | filas={len(df_std)}")

if __name__ == "__main__":
    main()
