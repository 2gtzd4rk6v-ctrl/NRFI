def edge_for_nrfi(model_probability, yes_bid=None, no_bid=None, buffer=0.005):
    """
    For a YES NRFI contract, use the effective buy price when available.
    If only bids are known, display bid-based reference and mark it non-tradable.
    """
    if yes_bid is not None:
        return {
            "model_probability":model_probability,
            "kalshi_yes_bid":yes_bid,
            "raw_edge":model_probability-yes_bid,
            "tradable":False
        }
    if no_bid is not None:
        # Buying YES at the complement of the NO bid is a reference ask only if
        # the order book actually supports that conversion.
        ref=1-no_bid
        return {
            "model_probability":model_probability,
            "kalshi_reference_yes":ref,
            "raw_edge":model_probability-ref,
            "tradable":False
        }
    return {"model_probability":model_probability,"raw_edge":None,"tradable":False}
