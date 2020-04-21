import numpy as np
from itertools import combinations_with_replacement, combinations

number_of_iterations = 1100

def get_all_combinations():
  r = [i for i in range(22)]
  combs = combinations_with_replacement(r, 6)
  final = []
  for c in combs:
    if sum(c) == 21:
      final.append(c)
  return final

def battle(c1, c2):
  c1_score = 0
  c2_score = 0
  for i in range(number_of_iterations):
    index1 = np.random.randint(0, 6)
    index2 = np.random.randint(0, 6)
    if c1[index1] > c2[index2]:
      c1_score += 1
    elif c1[index1] < c2[index2]:
      c2_score += 1
  if c1_score > c2_score:
    return c1
  elif c1_score < c2_score:
    return c2
  return 'remi'

a = get_all_combinations()

def battle_all(combs):
  battle_combs = combinations(combs, 2)
  f = np.zeros(len(combs)).tolist()
  for c in battle_combs:
    result = battle(c[0], c[1])
    if result != 'remi':
      i = combs.index(result)
      f[i] += 1
  return f

f = battle_all(a)

m = max(f)

best = [i for i, j in enumerate(f) if j == m]

for b in best:
  print(a[b])
