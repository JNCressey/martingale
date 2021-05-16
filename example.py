from martingale import martingale

print("# The sequence when the payoff value is ¤36, \
as in roulette straight up.")
gen = martingale(36.0,include_total_sunk_cost=True)
for i in range(1,101):
    (bet,sunk_cost) = next(gen)
    print(f"Round {i}: You bet ¤{bet}. Total sunk = ¤{sunk_cost}.")
