from cap5.exe5 import print_matriz


def soma_mat(m1, m2):
    res = []
    for i in range(len(m1)):
        res.append([])
        for e1, e2 in zip(m1[i], m2[i]):
            res[i].append(e1 + e2)
    return res
