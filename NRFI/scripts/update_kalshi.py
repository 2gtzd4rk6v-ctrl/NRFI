import json, os, datetime
from nrfi.kalshi import all_markets, is_first_inning_run

# This creates a raw market snapshot. The model/game join should call this module
# and match by normalized away/home team names + game date.
markets=[m for m in all_markets() if is_first_inning_run(m)]
os.makedirs("data",exist_ok=True)
with open("data/kalshi_markets.json","w") as f:
    json.dump({"retrieved_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "markets":markets},f)
print("saved",len(markets),"first-inning markets")
