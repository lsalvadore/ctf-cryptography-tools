from .EuclideanAlgorithm import *
from .NthRoot import *

def Hastad(CypherTextsModuliTuple):
    '''
    Use the Håstad attack to retrieve a message M from the data in CypherTextsModuliTuple. It is assumed that:
    - e = len(CypherTextsModuliTuple);
    - CypherTextsModuliTuple is a tuple of pairs (C,N) such that M ** e = C (mod N).
    Return M.
    '''
    e = len(CypherTextsModuliTuple)
    Sum = 0
    ModuliProduct = 1
    for i in range(e):
        ModuliProduct = 1
        for j in range(e):
            if i != j:
                ModuliProduct *= CypherTextsModuliTuple[j][1]
        Sum += CypherTextsModuliTuple[i][0] * EuclideanAlgorithm(ModuliProduct, CypherTextsModuliTuple[i][1])[1] * ModuliProduct

    ModuliProduct *= CypherTextsModuliTuple[-1][1]

    return NthRoot(Sum % ModuliProduct, e)
