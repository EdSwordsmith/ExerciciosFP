from cap5.exe5 import print_matriz


def multiplica_mat(m1, m2):
    res = []
    for i in range(len(m1)):
        res.append([])
        for j in range(len(m2[0])):
            res[i].append(0)
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res
