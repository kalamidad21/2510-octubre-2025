from pathlib import Path
import argparse, sqlite3, pandas as pd

BASE = Path(__file__).parent
DATA = BASE / "data"; DATA.mkdir(exist_ok=True)
EXP = BASE / "exports"; EXP.mkdir(exist_ok=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DATA / "clima.db"))
    ap.add_argument("--table", default="mediciones")
    ap.add_argument("--desde", required=True, help="YYYY-MM-DD")
    ap.add_argument("--hasta", required=True, help="YYYY-MM-DD (inclusive)")
    ap.add_argument("--out", help="ruta CSV de salida (opcional)")
    args = ap.parse_args()

    out = Path(args.out) if args.out else EXP / f"{args.table}_{args.desde}_{args.hasta}.csv"

    with sqlite3.connect(args.db) as con:
        q = f"""
        SELECT * FROM {args.table}
        WHERE substr(time,1,10) >= ? AND substr(time,1,10) <= ?
        ORDER BY time;
        """
        df = pd.read_sql(q, con, params=[args.desde, args.hasta])

    if df.empty:
        print("⚠️ Sin datos para el rango:", args.desde, "→", args.hasta)
        return

    df.to_csv(out, index=False, encoding="utf-8")
    print("✅ Exportado:", out.resolve(), "Filas:", len(df))

if __name__ == "__main__":
    main()
