from pathlib import Path
import argparse, sqlite3, pandas as pd

BASE = Path(__file__).parent
DATA = BASE / "data"; EXP = BASE / "exports"
DATA.mkdir(exist_ok=True); EXP.mkdir(exist_ok=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DATA / "clima.db"))
    ap.add_argument("--table", default="mediciones")
    ap.add_argument("--desde", required=True)
    ap.add_argument("--hasta", required=True)
    ap.add_argument("--out", help="ruta CSV salida (opcional)")
    args = ap.parse_args()

    out = Path(args.out) if args.out else EXP / f"stats_{args.table}_{args.desde}_{args.hasta}.csv"

    with sqlite3.connect(args.db) as con:
        q = f"""
        SELECT 
          substr(time,1,10) AS fecha,
          COUNT(*)                  AS n,
          MIN(temperature_2m)       AS temp_min,
          MAX(temperature_2m)       AS temp_max,
          ROUND(AVG(temperature_2m),2) AS temp_avg,
          ROUND(AVG(relative_humidity_2m),2) AS rh_avg
        FROM {args.table}
        WHERE substr(time,1,10) >= ? AND substr(time,1,10) <= ?
        GROUP BY substr(time,1,10)
        ORDER BY fecha;
        """
        df = pd.read_sql(q, con, params=[args.desde, args.hasta])

    df.to_csv(out, index=False, encoding="utf-8")
    print("✅ Stats diarias exportadas:", out.resolve(), "Días:", len(df))

if __name__ == "__main__":
    main()
