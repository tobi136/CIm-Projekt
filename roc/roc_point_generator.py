from math import inf


# Algorithmus zum Berechnen der Punkte einer Roc-Kurve (Output: 2-Dimensionale Liste)
def generate_roc(example_set, p, n):
    # Absteigend Sortieren
    example_set = list(reversed(sorted(example_set)))
    # print(example_set)
    f = [x for (x, y) in example_set]  # 1. Element aus jedem Tupel rausholen
    l = [y for (x, y) in example_set]  # 2. Element...
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


# Hilfsfunktion für Berechnung von Trapezflächen
def trapezoid_area(x1, x2, y1, y2):
    base = abs(x1 - x2)
    height = (y1 + y2) / 2
    return base * height


def roc_area(example_set, p, n):
    # Absteigend Sortieren
    example_set = list(reversed(sorted(example_set)))
    f = [x for (x, y) in example_set]  # 1. Element aus jedem Tupel rausholen
    l = [y for (x, y) in example_set]  # 2. Element...
    fp = tp = 0
    fp_prev = tp_prev = 0
    a = 0
    f_prev = -inf
    i = 0
    while i < len(l):
        if f[i] != f_prev:
            a += trapezoid_area(fp, fp_prev, tp, tp_prev)
            f_prev = f[i]
            fp_prev = fp
            tp_prev = tp
        if l[i]:  # l ist eine boolean-Liste!
            tp += 1
        else:
            fp += 1
        i += 1
    a += trapezoid_area(n, fp_prev, n, tp_prev)  # Vllt müsste das zweite n ein p sein!
    return a / (p * n)


# Werte aus der Aufgabe
test_set = [(0.84, True), (0.71, True), (0.92, True), (0.39, True), (0.44, True), (0.79, False), (0.28, False),
            (0.11, False), (0.52, False), (0.31, False), (0.49, False), (0.42, False)]
roc_points = generate_roc(test_set, 5, 7)
print(roc_points)
# Schön formatieren, damit man's in R reinkopieren kann zum Plotten
print("x=c(" + ",".join(map(str, [x for (x, y) in roc_points])) + ")")  # x-Werte
print("y=c(" + ",".join(map(str, [y for (x, y) in roc_points])) + ")")  # y-Werte
print("AUC=" + str(roc_area(test_set, 5, 7)))
