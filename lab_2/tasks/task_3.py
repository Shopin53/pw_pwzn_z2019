def unique(values):
    """
    Funkcja zwraca listę unikatowych wartości.
    Utrudnienie: Funkcja zwraca unikatowe wartości w kolejności wystąpienia.

    :param values: List of values to check.
    :type values: list
    :return: Unique values in order of appear.
    :rtype: list
    """
    pass
    q=values
    print(q)
    v=[]
    v.append(q[0])
    k=1
    while k<len(q):
        j=0
        w=0
        while w<len(v):
            if q[w]==q[k]:
                 j=1
            w+=1
        if j==0:
            v.append(q[k])
        k+=1
    return v


if __name__ == "__main__":
    assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])