import requests, re
from datetime import datetime, timezone

BASE="https://api.elections.kalshi.com/trade-api/v2"

def get_markets(status="open",limit=1000,cursor=None):
    p={"status":status,"limit":limit}
    if cursor:p["cursor"]=cursor
    r=requests.get(f"{BASE}/markets",params=p,timeout=30)
    r.raise_for_status(); return r.json()

def all_markets():
    out=[]; cursor=None
    while True:
        x=get_markets(cursor=cursor); out.extend(x.get("markets",[]))
        cursor=x.get("cursor")
        if not cursor: return out

def is_first_inning_run(m):
    s=(m.get("title") or m.get("subtitle") or "").lower()
    return ("first inning" in s or "1st inning" in s) and ("run" in s)

def yes_no_prices(m):
    # Kalshi API commonly exposes yes_bid/no_bid in cents.
    # Convert cents to probability.
    y=m.get("yes_bid")
    n=m.get("no_bid")
    return (y/100 if y is not None else None,
            n/100 if n is not None else None)

def match_game(m,away,home):
    s=" ".join(str(m.get(k,"")) for k in ["title","subtitle","ticker"]).lower()
    return away.lower() in s and home.lower() in s and is_first_inning_run(m)

def find_nrfi(away,home):
    candidates=[m for m in all_markets() if match_game(m,away,home)]
    return candidates[0] if candidates else None
