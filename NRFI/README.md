# NRFI + Kalshi

This adds a Kalshi market scanner and an NRFI-vs-market edge display.

Kalshi's current baseball catalog includes first-inning-run markets for individual
MLB games. The scanner discovers markets from the API rather than assuming ticker
formats.

IMPORTANT: this code deliberately labels bid-derived edge as REFERENCE ONLY.
A real tradable edge must use the current order book/ask price and account for
spread, depth, fees, and whether the contract settles exactly as the model target
does.

For production:
1. Poll Kalshi markets/order books every 15-30 seconds on game days.
2. Match game by stable event/market metadata, not ticker string parsing.
3. Use the actual YES ask to evaluate buying YES NRFI.
4. Use the actual NO ask to evaluate buying NO NRFI.
5. Save snapshots before lineups, after lineups, and immediately pregame.
6. Store every price/model pair for later CLV and ROI analysis.
