# MCTS Benchmarks

Benchmarks for a minimal MCTS implementations in Python, to investigate the feasability of all-Python MCTS for research.

MCTS implementation based on [MuZero pseudocode](https://arxiv.org/abs/1911.08265).

Run with

```sh
python3 mcts.py
```

Results from a recent run on my machine (AMD Ryzen 3950X), single thread:

```
num_actions =  18
  5 sims / move: 10265.5 ±  74.2 searches, 51327.5 ± 370.8 sims per second
 10 sims / move:  5013.8 ±  13.8 searches, 50138.2 ± 137.7 sims per second
 20 sims / move:  2306.9 ±   7.6 searches, 46138.4 ± 151.2 sims per second
 50 sims / move:   788.6 ±   1.8 searches, 39428.7 ±  88.6 sims per second
100 sims / move:   363.6 ±   1.1 searches, 36363.2 ± 110.9 sims per second
200 sims / move:   168.6 ±   0.4 searches, 33712.7 ±  88.7 sims per second
500 sims / move:    59.3 ±   0.1 searches, 29641.7 ±  62.0 sims per second

num_actions =  82
  5 sims / move: 10051.0 ±  28.5 searches, 50255.2 ± 142.5 sims per second
 10 sims / move:  5023.7 ±   8.2 searches, 50237.0 ±  81.7 sims per second
 20 sims / move:  2505.2 ±   9.0 searches, 50103.4 ± 180.6 sims per second
 50 sims / move:   952.0 ±   1.0 searches, 47600.8 ±  51.0 sims per second
100 sims / move:   433.3 ±   0.7 searches, 43325.9 ±  69.8 sims per second
200 sims / move:   194.5 ±   0.3 searches, 38890.9 ±  54.8 sims per second
500 sims / move:    70.5 ±   0.2 searches, 35254.1 ± 120.3 sims per second

num_actions =  362
  5 sims / move:  7972.7 ±  15.0 searches, 39863.4 ±  75.0 sims per second
 10 sims / move:  4014.3 ±  12.6 searches, 40143.5 ± 125.9 sims per second
 20 sims / move:  2007.9 ±   5.4 searches, 40157.6 ± 108.7 sims per second
 50 sims / move:   797.3 ±   1.2 searches, 39864.1 ±  58.1 sims per second
100 sims / move:   397.1 ±   0.6 searches, 39709.2 ±  61.4 sims per second
200 sims / move:   183.9 ±   0.4 searches, 36786.2 ±  82.0 sims per second
500 sims / move:    67.4 ±   0.2 searches, 33691.9 ±  80.8 sims per second
```

To profile on a function level, use

```sh
pyinstrument mcts.py
```