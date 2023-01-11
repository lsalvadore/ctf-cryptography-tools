def NthRoot(Base,N):
    '''
    Compute the N-th root of Base using bisection method.
    Result is the largest integer X such that X ** N <= Base.
    '''
    Left = 1
    Test = Base >> 1
    Right = Base
    while(Left < Right and Test != Left):
        Power = Test ** N
        if Power < Base:
            Left = Test
        elif Power > Base:
            Right = Test
        else:
            return Test
        Test = (Left + Right) >> 1
    return Test
