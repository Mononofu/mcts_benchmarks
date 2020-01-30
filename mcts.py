import math
import timeit

from typing import List

import numpy as np


class MuZeroConfig:
  def __init__(self):
    # UCB formula
    self.pb_c_base = 19652
    self.pb_c_init = 1.25

    self.discount = 0.997


class Node:
  def __init__(self):
    self.expanded = False

  def expand(self, prior, reward):
    self.prior = prior
    self.reward = reward
    self.child_visits = np.zeros_like(self.prior)
    self.child_values = np.zeros_like(self.prior)
    self.children = [Node() for _ in range(len(prior))]
    self.expanded = True

  def add_value(self, action, value):
    self.child_values[action] += value
    self.child_visits[action] += 1

  def __str__(self, indent=0):
    s = ' ' * indent
    s += 'Node'
    s += '\n'
    for child in self.children:
      if child.expanded:
        s += child.__str__(indent=indent + 2)
    return s

  def __repr__(self):
    return 'Node'


def run_mcts(config: MuZeroConfig, num_simulations: int, num_actions=18):
  root = Node()
  root.expand(np.random.rand(num_actions), reward=0)

  for _ in range(num_simulations):
    node = root
    search_path = []

    while node.expanded:
      parent = node
      action, node = select_child(config, node)
      search_path.append((parent, action, node))

    # print(search_path)

    node.expand(np.random.rand(num_actions), reward=np.random.rand())

    backpropagate(search_path,
                  value=np.random.rand(),
                  discount=config.discount)

  # print(root)


# Select the child with the highest UCB score.
def select_child(config: MuZeroConfig, node: Node):
  # Precompute constant part.
  visits = node.child_visits.sum() + 1
  pb_c = math.log(
      (visits + config.pb_c_base + 1) / config.pb_c_base) + config.pb_c_init
  pb_c *= math.sqrt(visits)

  min_v = node.child_values.min()
  max_v = node.child_values.max()
  if max_v > min_v:
    values = (node.child_values - min_v) / (max_v - min_v)
  else:
    values = node.child_values

  action = (values + pb_c / (node.child_visits + 1) * node.prior).argmax()

  return action, node.children[action]


# At the end of a simulation, we propagate the evaluation all the way up the
# tree to the root.
def backpropagate(search_path: List[Node], value: float, discount: float):
  for parent, action, node in search_path:
    parent.add_value(action, value)
    value = node.reward + discount * value


config = MuZeroConfig()
for _ in range(1):
  run_mcts(config, num_simulations=50)


def get_iterations_for_time(desired_time, timer):
  iterations, elapsed_time = timer.autorange()
  return int(iterations * (desired_time / elapsed_time))


def summarize(vs):
  return '%6.1f ± %5.1f' % (np.mean(vs), np.std(vs))


benchmark_time = 1.0
for num_sims in [5, 10, 20, 50, 100, 200, 500]:
  timer = timeit.Timer(lambda: run_mcts(config, num_sims), 'gc.enable()')
  iterations = get_iterations_for_time(benchmark_time, timer)
  times = timer.repeat(10, iterations)
  searches_per_second = [iterations / t for t in times]
  simulations_per_second = [s * num_sims for s in searches_per_second]

  print('%3d sims / move: %s searches, %s sims per second' %
        (num_sims, summarize(searches_per_second),
         summarize(simulations_per_second)))

# Most recent run:
#   5 sims / move: 7544.7 ± 122.8 searches, 37723.6 ± 613.8 sims per second
#  10 sims / move: 3957.1 ±  28.4 searches, 39570.9 ± 283.7 sims per second
#  20 sims / move: 1778.2 ±  11.6 searches, 35563.3 ± 231.1 sims per second
#  50 sims / move:  595.9 ±   2.8 searches, 29794.9 ± 140.5 sims per second
# 100 sims / move:  261.3 ±   5.7 searches, 26132.2 ± 574.3 sims per second
# 200 sims / move:  119.5 ±   2.1 searches, 23896.4 ± 415.1 sims per second
# 500 sims / move:   40.6 ±   0.5 searches, 20276.7 ± 233.4 sims per second