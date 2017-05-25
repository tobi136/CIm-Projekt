from math import inf


def generate_roc(l, f, p, n):
    #Liste muss hier schon sortiert sein!
    fp = tp = 0
    r = []
    f_prev = -inf
    i = 0
    while i < len(l):
        if f[i] != f_prev:
            r.append((fp / n, tp / p))
            f_prev = f[i]
        if l[i]:  # l ist eine boolean-Liste!
            tp += 1
        else:
            fp += 1
        i += 1
    r.append((fp / n, tp / p))  # sollte am Ende immer (1,1) sein
    return r


# Test stuff
test_set = [(0.84, True), (0.71, True), (0.92, True), (0.39, True), (0.44, True), (0.79, False), (0.28, False),
            (0.11, False), (0.52, False), (0.31, False), (0.49, False), (0.42, False)]
#Hier wird sortiert, und zwar absteigend nach der ersten Komponente
#TODO: Das erst in der Methode machen
test_set = list(reversed(sorted(test_set)))
examples = [y for (x, y) in test_set]
scores = [x for (x, y) in test_set]
roc_points = generate_roc(examples, scores, 5, 7)
print(roc_points)