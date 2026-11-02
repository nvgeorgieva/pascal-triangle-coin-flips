"""
# Author: Nina Georgieva
Pascal's triangle and coin flips.

Two small building blocks for the project:
  1. build_pascal_triangle(n)  -> builds the triangle row by row (just additions)
  2. flip_coins(n_coins, n_trials) -> simulates flipping coins and counts heads

The connection: row n of Pascal's triangle gives the counts of how many
ways you can get 0, 1, 2, ... heads when flipping n coins. Dividing each
number by the row total turns those counts into probabilities.
"""

import random


def build_pascal_triangle(n_rows):
    """Build Pascal's triangle with `n_rows` rows (row 0 is just [1]).

    Each row starts and ends with 1, and every middle number is the sum
    of the two numbers directly above it.

    Returns a list of lists, e.g. for n_rows=4:
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    triangle = []
    for row_index in range(n_rows):
        row = [1]  # every row starts with 1
        if triangle:
            previous = triangle[-1]
            for i in range(len(previous) - 1):
                row.append(previous[i] + previous[i + 1])
            row.append(1)  # every row ends with 1
        triangle.append(row)
    return triangle


def row_probabilities(row):
    """Turn a triangle row (counts) into probabilities that sum to 1.

    Example: [1, 3, 3, 1] -> [0.125, 0.375, 0.375, 0.125]
    """
    total = sum(row)
    return [count / total for count in row]


def flip_coins(n_coins, n_trials):
    """Flip `n_coins` coins `n_trials` times and count how often we see
    exactly 0, 1, 2, ... heads.

    Returns a list of length (n_coins + 1): index k holds the number of
    trials that produced exactly k heads.
    """
    counts = [0] * (n_coins + 1)
    for _ in range(n_trials):
        heads = 0
        for _ in range(n_coins):
            if random.random() < 0.5:  # 0.5 chance of heads
                heads += 1
        counts[heads] += 1
    return counts


def counts_to_frequencies(counts, n_trials):
    """Turn raw counts from flip_coins into frequencies (fractions)."""
    return [c / n_trials for c in counts]


def text_bar_chart(predicted, simulated):
    """Print a simple side-by-side bar chart using text only.

    No external libraries needed. Each bar is drawn with '#' characters,
    where the bar length is proportional to the probability.
    """
    scale = 50  # a probability of 1.0 would be 50 characters wide
    print(f"{'heads':>5} | {'predicted':<28} | simulated")
    print("-" * 70)
    for k in range(len(predicted)):
        p_bar = "#" * round(predicted[k] * scale)
        s_bar = "#" * round(simulated[k] * scale)
        print(f"{k:>5} | {p_bar:<28} | {s_bar}")
        print(f"{'':>5} | {predicted[k]:<28.4f} | {simulated[k]:.4f}")


if __name__ == "__main__":
    # Quick manual check so you can run `python pascal.py` and see output.
    triangle = build_pascal_triangle(6)
    print("Pascal's triangle:")
    for row in triangle:
        print(row)

    n_coins = 5
    row = build_pascal_triangle(n_coins + 1)[n_coins]
    print(f"\nRow for {n_coins} coins (counts): {row}")
    print(f"Predicted probabilities: {row_probabilities(row)}")

    n_trials = 10000
    counts = flip_coins(n_coins, n_trials)
    print(f"\nSimulated counts over {n_trials} trials: {counts}")
    print(f"Simulated frequencies: {counts_to_frequencies(counts, n_trials)}")
