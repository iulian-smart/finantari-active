#!/usr/bin/env python3
"""finantari.json (intern) -> data.json (public: fără fișe). Usage: make_public_data.py <finantari.json> <data.json>"""
import json, sys, datetime
rows = json.load(open(sys.argv[1], encoding="utf-8"))
today = datetime.date.today().isoformat()
cutoff = (datetime.date.today() - datetime.timedelta(days=10)).isoformat()  # apelurile expirate rămân vizibile 10 zile
pub = [{k: r.get(k) for k in ("id", "program", "regiune", "titlu", "beneficiari", "suma", "descriere", "termen", "url")}
       for r in rows if r.get("titlu") and r.get("url") and (not r.get("termen") or r["termen"] >= cutoff)]
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).isoformat(timespec="seconds")
json.dump({"actualizat": now, "sursa": "Centrul de Dezvoltare SMART", "apeluri": pub},
          open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(pub), "apeluri publice")
