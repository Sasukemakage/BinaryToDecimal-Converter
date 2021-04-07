def convert(l):
    intNumber = 0
    l.reverse()
    if len(l) == 0:
        return None
    for i in range(len(l)):
        if l[i] == 0:
            nbr = 0
        if l[i] == 1:
            nbr = 2**i
        intNumber += nbr
    return intNumber
