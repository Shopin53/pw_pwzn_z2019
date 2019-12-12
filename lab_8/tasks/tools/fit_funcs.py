def least_sq(xy):

    x = xy[0]
    y = xy[1]
    N = xy.shape[1]
    Sumx=x.sum()
    Sumx2=(x**2).sum()
    Delta = N * Sumx2 - Sumx*Sumx
    Sumy=y.sum()
    Sumxy=(x*y).sum()
    A = (Sumx2 * Sumy - Sumx * Sumxy)/Delta
    B = (N * Sumxy - Sumx * Sumy)/Delta
    
    return A, B