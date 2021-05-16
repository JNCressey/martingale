# Introduction

Let ¤ be the symbol for a unit value of betting chip or a generic currency.

The basic martingale strategy concerns a betting game that pays out ¤2 per ¤1 of the bet. Bets are assumed to pay out twice your bet when you win (and pay out nothing when you lose).

The strategy asks you to start a series of bets with ¤1, and then double your bet after each losing round until you get a win. Upon winning, the payout will exactly match the total you have sunk into bets in this series, plus an extra ¤1 to take as winnings. You then start a new series after each win. The strategy "guarantees" a reward of ¤1 after every series of bets. 

**The strategy is not actually practical. It is likely to eventually produce a series with a cost that exceeds your capital.**

## See these:

- [Martingale (betting system) - Wikipedia](https://en.wikipedia.org/wiki/Martingale_%28betting_system%29)
- [Gambling with the Martingale Strategy - Numberphile - YouTube](https://www.youtube.com/watch?v=zTsRGQj6VT4)

# The function

The `martingale` function is an infinite generator for the amounts you would bet in each round in a series of losses.

The generalized strategy is to bet the minimum that a win would strictly exceed the cost of the current series. It is assumed that all bets must be whole multiples of ¤1. 

The function takes 3 arguments.

- `payout_value` [`float`]. This is the ratio of the payout for a win to the amount placed as a bet.  i.e., on a win, the payout is `payout_value` multiplied by your bet (and the payout is nothing on a loss).
- `inital_sunk_cost` [`int`] (optional). Use to control where the generator starts. The first bet will aim for a payout that strictly exceeds this sunk cost, and will continue from there. Default `0`.
- `include_total_sunk_cost` [`bool`] (optional). If left as false, the output of the generator will just be the integer bet amounts. If set to true, the output will be a tuple of the bet and the running total sunk cost: `(next_bet,sunk_cost)`. Default `False`.

# Example

`example.py` prints the sequence where the payoff value is ¤36 per ¤1 of the bet. This is the payout for "straight up" (betting on a specific number) in roulette.

<details>
    <summary>Output of <code>example.py</code></summary>
    <pre># The sequence when the payoff value is ¤36, as in roulette straight up.
Round 1: You bet ¤1. Total sunk = ¤1.
Round 2: You bet ¤1. Total sunk = ¤2.
Round 3: You bet ¤1. Total sunk = ¤3.
Round 4: You bet ¤1. Total sunk = ¤4.
Round 5: You bet ¤1. Total sunk = ¤5.
Round 6: You bet ¤1. Total sunk = ¤6.
Round 7: You bet ¤1. Total sunk = ¤7.
Round 8: You bet ¤1. Total sunk = ¤8.
Round 9: You bet ¤1. Total sunk = ¤9.
Round 10: You bet ¤1. Total sunk = ¤10.
Round 11: You bet ¤1. Total sunk = ¤11.
Round 12: You bet ¤1. Total sunk = ¤12.
Round 13: You bet ¤1. Total sunk = ¤13.
Round 14: You bet ¤1. Total sunk = ¤14.
Round 15: You bet ¤1. Total sunk = ¤15.
Round 16: You bet ¤1. Total sunk = ¤16.
Round 17: You bet ¤1. Total sunk = ¤17.
Round 18: You bet ¤1. Total sunk = ¤18.
Round 19: You bet ¤1. Total sunk = ¤19.
Round 20: You bet ¤1. Total sunk = ¤20.
Round 21: You bet ¤1. Total sunk = ¤21.
Round 22: You bet ¤1. Total sunk = ¤22.
Round 23: You bet ¤1. Total sunk = ¤23.
Round 24: You bet ¤1. Total sunk = ¤24.
Round 25: You bet ¤1. Total sunk = ¤25.
Round 26: You bet ¤1. Total sunk = ¤26.
Round 27: You bet ¤1. Total sunk = ¤27.
Round 28: You bet ¤1. Total sunk = ¤28.
Round 29: You bet ¤1. Total sunk = ¤29.
Round 30: You bet ¤1. Total sunk = ¤30.
Round 31: You bet ¤1. Total sunk = ¤31.
Round 32: You bet ¤1. Total sunk = ¤32.
Round 33: You bet ¤1. Total sunk = ¤33.
Round 34: You bet ¤1. Total sunk = ¤34.
Round 35: You bet ¤1. Total sunk = ¤35.
Round 36: You bet ¤1. Total sunk = ¤36.
Round 37: You bet ¤2. Total sunk = ¤38.
Round 38: You bet ¤2. Total sunk = ¤40.
Round 39: You bet ¤2. Total sunk = ¤42.
Round 40: You bet ¤2. Total sunk = ¤44.
Round 41: You bet ¤2. Total sunk = ¤46.
Round 42: You bet ¤2. Total sunk = ¤48.
Round 43: You bet ¤2. Total sunk = ¤50.
Round 44: You bet ¤2. Total sunk = ¤52.
Round 45: You bet ¤2. Total sunk = ¤54.
Round 46: You bet ¤2. Total sunk = ¤56.
Round 47: You bet ¤2. Total sunk = ¤58.
Round 48: You bet ¤2. Total sunk = ¤60.
Round 49: You bet ¤2. Total sunk = ¤62.
Round 50: You bet ¤2. Total sunk = ¤64.
Round 51: You bet ¤2. Total sunk = ¤66.
Round 52: You bet ¤2. Total sunk = ¤68.
Round 53: You bet ¤2. Total sunk = ¤70.
Round 54: You bet ¤2. Total sunk = ¤72.
Round 55: You bet ¤3. Total sunk = ¤75.
Round 56: You bet ¤3. Total sunk = ¤78.
Round 57: You bet ¤3. Total sunk = ¤81.
Round 58: You bet ¤3. Total sunk = ¤84.
Round 59: You bet ¤3. Total sunk = ¤87.
Round 60: You bet ¤3. Total sunk = ¤90.
Round 61: You bet ¤3. Total sunk = ¤93.
Round 62: You bet ¤3. Total sunk = ¤96.
Round 63: You bet ¤3. Total sunk = ¤99.
Round 64: You bet ¤3. Total sunk = ¤102.
Round 65: You bet ¤3. Total sunk = ¤105.
Round 66: You bet ¤3. Total sunk = ¤108.
Round 67: You bet ¤4. Total sunk = ¤112.
Round 68: You bet ¤4. Total sunk = ¤116.
Round 69: You bet ¤4. Total sunk = ¤120.
Round 70: You bet ¤4. Total sunk = ¤124.
Round 71: You bet ¤4. Total sunk = ¤128.
Round 72: You bet ¤4. Total sunk = ¤132.
Round 73: You bet ¤4. Total sunk = ¤136.
Round 74: You bet ¤4. Total sunk = ¤140.
Round 75: You bet ¤4. Total sunk = ¤144.
Round 76: You bet ¤5. Total sunk = ¤149.
Round 77: You bet ¤5. Total sunk = ¤154.
Round 78: You bet ¤5. Total sunk = ¤159.
Round 79: You bet ¤5. Total sunk = ¤164.
Round 80: You bet ¤5. Total sunk = ¤169.
Round 81: You bet ¤5. Total sunk = ¤174.
Round 82: You bet ¤5. Total sunk = ¤179.
Round 83: You bet ¤5. Total sunk = ¤184.
Round 84: You bet ¤6. Total sunk = ¤190.
Round 85: You bet ¤6. Total sunk = ¤196.
Round 86: You bet ¤6. Total sunk = ¤202.
Round 87: You bet ¤6. Total sunk = ¤208.
Round 88: You bet ¤6. Total sunk = ¤214.
Round 89: You bet ¤6. Total sunk = ¤220.
Round 90: You bet ¤7. Total sunk = ¤227.
Round 91: You bet ¤7. Total sunk = ¤234.
Round 92: You bet ¤7. Total sunk = ¤241.
Round 93: You bet ¤7. Total sunk = ¤248.
Round 94: You bet ¤7. Total sunk = ¤255.
Round 95: You bet ¤8. Total sunk = ¤263.
Round 96: You bet ¤8. Total sunk = ¤271.
Round 97: You bet ¤8. Total sunk = ¤279.
Round 98: You bet ¤8. Total sunk = ¤287.
Round 99: You bet ¤8. Total sunk = ¤295.
Round 100: You bet ¤9. Total sunk = ¤304.</pre>
</details>
