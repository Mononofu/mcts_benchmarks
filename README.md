# MCTS Benchmarks

Benchmarks for a minimal MCTS implementations in Python, to investigate the feasability of all-Python MCTS for research.

Run with

```sh
python3 mcts.py
```

Results from a recent run on my machine (AMD Ryzen 3950X):

```
  5 sims / move: 8675.5 ±  72.1 searches, 43377.4 ± 360.5 sims per second
 10 sims / move: 4326.2 ±  14.9 searches, 43261.7 ± 149.2 sims per second
 20 sims / move: 2015.2 ±   2.5 searches, 40304.4 ±  50.8 sims per second
 50 sims / move:  684.0 ±   1.2 searches, 34198.2 ±  59.7 sims per second
100 sims / move:  312.9 ±   0.8 searches, 31288.7 ±  76.6 sims per second
200 sims / move:  146.3 ±   0.3 searches, 29269.6 ±  51.0 sims per second
500 sims / move:   52.3 ±   0.2 searches, 26128.8 ± 124.9 sims per second
```

To profile on a function level, use

```sh
pyinstrument mcts.py
```