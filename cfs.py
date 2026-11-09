import numpy as np

x1 = np.array([1, 2, 3, 7, 8, 9])
x2 = np.array([2, 3, 4, 6, 7, 8])
x3 = np.array([5, 4, 3, 3, 2, 1])
y = np.array([0, 0, 0, 1, 1, 1])

data = {'x1': x1, 'x2': x2, 'x3': x3, 'y': y}


def f(n, x, y):
    return abs(
        (n * sum(x * y) - sum(x) * sum(y)) /
        ((n * sum(x**2) - sum(x)**2) *
         (n * sum(y**2) - sum(y)**2))**0.5
    )


def CFSmerit(k, x1, x2, y, n):
    avgf = (f(n, x1, y) + f(n, x2, y)) / 2
    rff = f(n, x1, x2)

    den_term = k + k * (k - 1) * rff

    if den_term == 0:
        return 0

    return (k * avgf) / (den_term**0.5)


def best_merit(data):
    all_cols = list(data.keys())
    cols = [k for k in all_cols if k != 'y']

    feat_pairs = [
        (cols[i], cols[j])
        for i in range(len(cols))
        for j in range(i + 1, len(cols))
    ]

    n = len(data[cols[0]])
    res = {}

    for x, y in feat_pairs:
        k = 2
        res[(x, y)] = CFSmerit(k, data[x], data[y], data['y'], n)

    best_pair = max(res, key=res.get)
    best_score = res[best_pair]

    print("The best CFS Merit data pair is", best_pair)
    print("Best pair score =", best_score)

    return res


res = best_merit(data)