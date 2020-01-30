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


def format_vs(vs):
  return ['%.2f' % v for v in vs]


class Node:
  def __init__(self):
    self.expanded = False
    self.min_value = math.inf
    self.max_value = -math.inf
    self.visits = 0

  def expand(self, prior, reward):
    self.prior = prior
    self.reward = reward
    self.child_visits = np.zeros_like(self.prior)
    self._child_values = np.zeros_like(self.prior)
    self.children = [Node() for _ in range(len(prior))]
    self.expanded = True
    self.visits = 1

  def add_value(self, action, value):
    self.visits += 1

    # Maintain the running mean of the value.
    self.child_visits[action] += 1
    self._child_values[action] = self._child_values[action] + (
        value - self._child_values[action]) / self.child_visits[action]

    # Maintain min and max over the child values for normalization.
    self.min_value = min(self.min_value, value)
    self.max_value = max(self.max_value, value)

  def normalized_values(self):
    min_v = self.min_value
    max_v = self.max_value
    if max_v > min_v:
      values = np.subtract(self._child_values,
                           min_v,
                           out=np.full_like(self._child_values, 0),
                           where=self.child_visits != 0)
      return values / (max_v - min_v)
    else:
      return self._child_values

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
  pb_c = math.log((node.visits + config.pb_c_base + 1) /
                  config.pb_c_base) + config.pb_c_init
  pb_c *= math.sqrt(node.visits)

  action = (node.normalized_values() + pb_c /
            (node.child_visits + 1) * node.prior).argmax()

  return action, node.children[action]


# At the end of a simulation, we propagate the evaluation all the way up the
# tree to the root.
def backpropagate(search_path: List[Node], value: float, discount: float):
  for parent, action, node in search_path:
    parent.add_value(action, value)
    value = node.reward + discount * value


def get_iterations_for_time(desired_time, timer):
  iterations, elapsed_time = timer.autorange()
  return int(iterations * (desired_time / elapsed_time))


def summarize(vs):
  return '%6.1f ± %5.1f' % (np.mean(vs), np.std(vs))


def main():
  config = MuZeroConfig()
  for _ in range(1):
    run_mcts(config, num_simulations=50)

  # return

  benchmark_time = 0.3
  for num_actions in [18, 82, 362]:
    print()
    print('num_actions = ', num_actions)
    for num_sims in [5, 10, 20, 50, 100, 200, 500]:
      timer = timeit.Timer(
          lambda: run_mcts(
              config, num_simulations=num_sims, num_actions=num_actions),
          'gc.enable()')
      iterations = get_iterations_for_time(benchmark_time, timer)
      times = timer.repeat(10, iterations)
      searches_per_second = [iterations / t for t in times]
      simulations_per_second = [s * num_sims for s in searches_per_second]

      print('%3d sims / move: %s searches, %s sims per second' %
            (num_sims, summarize(searches_per_second),
             summarize(simulations_per_second)))


if __name__ == '__main__':
  main()

# benchmark with pyinstrument