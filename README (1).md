# Pascal's Triangle and Coin Flips

A math + Python project which connects a simple number pattern — **Pascal's triangle** — to the
real behavior of **flipping coins**, and checks whether the triangle really
predicts how often each number of heads appears.
The notebook renders directly on GitHub — just click notebook.ipynb.

## The question

If I flip `n` coins many times, how often should I expect 0 heads, 1 head,
2 heads, and so on? Pascal's triangle claims to predict this. The question is if it is right?

## The idea in short

- Pascal's triangle is built row by row: each number is the sum of the two
  numbers above it.
- Row `n` gives the counts for flipping `n` coins. For 3 coins the row is
  `1 3 3 1` (total 8), so the probability of exactly one head is `3/8`.
- These triangle numbers are exactly the **binomial coefficients**
  `C(n, k) = n! / (k!(n-k)!)`.
- We test the prediction by simulating thousands of coin flips and comparing
  the simulated frequencies against the probabilities from the triangle.

## Results

In tests, flipping 5 coins 10,000 times produced head counts that matched
the probabilities from row 5 of Pascal's triangle very closely. As the number
of flips grew from 100 to 100,000, the total error shrank from about 0.12 to
about 0.009 — more flips gave a closer match.

## Files

- `notebook.ipynb` — the main deliverable: explanation, math, code, experiments, chart, conclusion.
- `pascal.py` — small helper functions (build the triangle, simulate coin flips, text chart).

## How to run

This project uses only the Python standard library, so there is nothing to install.

Open the notebook:

```bash
jupyter notebook notebook.ipynb
```

Or run the quick demo:

```bash
python pascal.py
```

## References

- Wikipedia, "Pascal's triangle": https://en.wikipedia.org/wiki/Pascal%27s_triangle
- Wikipedia, "Binomial distribution": https://en.wikipedia.org/wiki/Binomial_distribution
- Course materials, Math Concepts for Developers.
- Python standard library documentation, `random` module: https://docs.python.org/3/library/random.html
