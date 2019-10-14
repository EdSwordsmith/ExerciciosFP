def junta_ordenados(t1, t2):
    i, j = 0, 0
    res = ()

    while len(res) < len(t1) + len(t2):
        if j == len(t2) or (i != len(t1) and t1[i] < t2[j]):
            res = res + (t1[i],)
            i = i + 1
        elif i == len(t1) or (j != len(t2) and t1[i] >= t2[j]):
            res = res + (t2[j],)
            j = j + 1

    return res
