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
head = 0
if len(sys.argv) > 2 and sys.argv[2].startswith("--head="):
    try:
        head = int(sys.argv[2].split("=", 1)[1])
    except ValueError:
        print("Invalid --head value; expected integer")
        raise SystemExit(2)

if head > 0:
    print(f"Preview (first {head} rows):")
    for row in rows[:head]:
        print(row)
