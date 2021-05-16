import math

def martingale(
    payout_value:float, # ie the payout per ¤1 bet
    inital_sunk_cost:int=0,
    include_total_sunk_cost:bool=False,
):
    sunk_cost = inital_sunk_cost
    while True:
        cover_sunk_cost = sunk_cost/payout_value
        minimum_whole_bet_covering_cost = math.ceil(cover_sunk_cost)
        next_bet = (
            minimum_whole_bet_covering_cost
            if (minimum_whole_bet_covering_cost > cover_sunk_cost)
            else (minimum_whole_bet_covering_cost + 1)
            )
        sunk_cost += next_bet
        yield (
            (next_bet,sunk_cost)
            if include_total_sunk_cost
            else next_bet
            )
