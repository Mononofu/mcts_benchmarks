# MCTS Benchmarks

Benchmarks for a minimal MCTS implementations in Python, to investigate the feasability of all-Python MCTS for research.

Run with

```sh
python3 mcts.py
```

Results from a recent run on my machine (AMD Ryzen 3950X):

```
num_actions =  18
  5 sims / move: 8677.2 ±  36.8 searches, 43385.9 ± 184.0 sims per second
 10 sims / move: 4292.0 ±  11.6 searches, 42920.2 ± 116.1 sims per second
 20 sims / move: 2012.7 ±  16.9 searches, 40254.7 ± 338.8 sims per second
 50 sims / move:  686.5 ±   1.2 searches, 34327.0 ±  60.1 sims per second
100 sims / move:  314.1 ±   0.8 searches, 31413.1 ±  82.8 sims per second
200 sims / move:  146.5 ±   0.5 searches, 29309.6 ±  91.8 sims per second
500 sims / move:   52.2 ±   0.2 searches, 26095.5 ± 123.5 sims per second

num_actions =  82
  5 sims / move: 4316.1 ±  18.9 searches, 21580.5 ±  94.6 sims per second
 10 sims / move: 2217.7 ±   6.8 searches, 22177.1 ±  67.8 sims per second
 20 sims / move: 1135.4 ±   2.6 searches, 22708.1 ±  51.7 sims per second
 50 sims / move:  439.6 ±   1.3 searches, 21981.3 ±  63.3 sims per second
100 sims / move:  206.8 ±   0.4 searches, 20680.1 ±  42.2 sims per second
200 sims / move:   94.1 ±   1.7 searches, 18825.5 ± 335.6 sims per second
500 sims / move:   32.7 ±   0.6 searches, 16335.2 ± 280.7 sims per second

num_actions =  362
  5 sims / move: 1297.0 ±   8.7 searches, 6485.1 ±  43.7 sims per second
 10 sims / move:  692.3 ±   3.3 searches, 6923.0 ±  32.7 sims per second
 20 sims / move:  350.7 ±   1.6 searches, 7015.0 ±  31.5 sims per second
 50 sims / move:  137.9 ±   0.5 searches, 6895.0 ±  22.7 sims per second
100 sims / move:   63.4 ±   0.4 searches, 6342.6 ±  41.0 sims per second
200 sims / move:   26.8 ±   0.3 searches, 5355.6 ±  60.0 sims per second
500 sims / move:    8.2 ±   0.3 searches, 4122.2 ± 139.8 sims per second
```

To profile on a function level, use

```sh
pyinstrument mcts.py
```