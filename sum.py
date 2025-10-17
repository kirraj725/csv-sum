
import csv, sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "sample/people.csv")
if not p.exists():
    print("File not found:", p)
    raise SystemExit(1)

with p.open(newline="") as f:
    r = csv.DictReader(f)
    rows = list(r)
    print("File:", p)
    print("Columns:", ", ".join(r.fieldnames or []))
    print("Row count:", len(rows))
