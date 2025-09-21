from pathlib import Path
import argparse, json, csv, re, sys

DATA_DIR = Path(__file__).parent / "data"

def pick_latest_json():
    files = sorted(DATA_DIR.glob("openmeteo_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None

def infer_city(path: Path) -> str:
    m = re.match(r"openmeteo_([a-zA-ZñÑáéíóúÁÉÍÓÚ\-]+)_\d{8}_\d{4}\.json$", path.name)
    return (m.group(1) if m else "").lower()

def to_csv(src: Path, dst: Path | None = None):
    if not src.exists():
        raise FileNotFoundError(f"No existe JSON: {src}")
    with src.open("r", encoding="utf-8") as f:
        data = json.load(f)

    hourly = data.get("hourly") or {}
    t, temp, rh = hourly.get("time"), hourly.get("temperature_2m"), hourly.get("relative_humidity_2m")
    if not (isinstance(t, list) and isinstance(temp, list) and isinstance(rh, list)):
        raise ValueError("JSON sin claves esperadas en hourly (time/temperature_2m/relative_humidity_2m).")
    n = min(len(t), len(temp), len(rh))
    if n == 0:
        raise ValueError("Series vacías; nada que exportar.")

    if dst is None:
        dst = src.with_suffix(".csv")
    dst.parent.mkdir(exist_ok=True)

    city = infer_city(src)
    with dst.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time", "temperature_2m", "relative_humidity_2m", "city"])
        for i in range(n):
            w.writerow([t[i], temp[i], rh[i], city])

    print(f"CSV creado: {dst}  (filas: {n})")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Convierte JSON de Open-Meteo a CSV (data/).")
    ap.add_argument("--src", type=Path, help="Ruta al JSON de entrada (por defecto: el más reciente en data/).")
    ap.add_argument("--out", type=Path, help="Ruta CSV de salida (opcional).")
    args = ap.parse_args()

    src = args.src if args.src else pick_latest_json()
    if not src:
        print("No se encontró ningún JSON en data/openmeteo_*.json", file=sys.stderr); sys.exit(2)
    to_csv(src, args.out)
