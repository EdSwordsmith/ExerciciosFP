def amigas(str1, str2):
    if len(str1) != len(str2):
        return False

    c = 0
    for a, b in zip(str1, str2):
        if a != b:
            c = c + 1

    return c / len(str1) <= 0.1
