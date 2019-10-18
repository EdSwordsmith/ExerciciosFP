def c(t, i):
    if not isinstance(t, tuple) or not isinstance(i, int):
        raise ValueError("c: bla bla bla")
    c = 0
    for e in t:
        if not isinstance(e, int):
            raise ValueError("bwdjiqj")
        elif e < i:
            c += 1
    return c
