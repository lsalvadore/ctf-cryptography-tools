def EuclideanAlgorithm(A,B):
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
    X = 1
    Y = - QuotientsList[-2]
    for K in range(len(QuotientsList) - 2, 0, -1):
        NewX = Y
        NewY = X - Y * QuotientsList[K - 1]
        X = NewX
        Y = NewY
    return (GCD, X, Y)
