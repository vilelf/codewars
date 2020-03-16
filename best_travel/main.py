from itertools import combinations

def choose_best_sum(t, k, ls):
    _tuple = combinations(ls, k)
    sums = [sum(i) for i in _tuple if sum(i) <= t]
    if sums:
        return max(sums)
    return None
