# DISCLAIMER: ESTA PORRA NAO FUNCIONA
def pesquisa(arr, l, r, x):
    if r >= l:
        meio = l + (r - l) // 2
        if arr[meio] == x:
            return meio
        elif arr[meio] > x:
            return pesquisa(arr, l, meio - 1, x)
        else:
            return pesquisa(arr, meio + 1, r, x)
    else:
        return -1


def seq_racaman(n):
    res = []
    for i in range(n):
        if i == 0:
            res.append(0)
        # elif res[i - 1] > i and pesquisa(res, 0, i - 1, res[i - 1] - i) == -1:
        elif res[i - 1] > i and (res[i - 1] - i) in res:
            res.append(res[i - 1] - i)
        else:
            res.append(res[i - 1] + i)
    return res
