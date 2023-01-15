def EuclideanAlgorithm(A,B):
    '''
    Compute the GCD of A and B and two coeffiecients X and Y satisfying
    a Bézout identity for A and B, i.e. such that XA + YB = GCD, using
    the Euclidean algorithm.
    Return the 3 elements list (GCD, X, Y).
    '''
    Dividend = A
    Divisor = B
    Remainder = 1
    QuotientsList = []
    RemaindersList = []
    while Remainder:
        Quotient = Dividend // Divisor
        Remainder = Dividend % Divisor
        QuotientsList += [Quotient]
        Dividend = Divisor
        Divisor = Remainder
    GCD = Dividend
    if len(QuotientsList) == 1:
        return (GCD, 0, 1)
    X = 1
    Y = - QuotientsList[-2]
    for K in range(len(QuotientsList) - 2, 0, -1):
        NewX = Y
        NewY = X - Y * QuotientsList[K - 1]
        X = NewX
        Y = NewY
    return (GCD, X, Y)
