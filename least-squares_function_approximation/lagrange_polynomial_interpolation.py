
class Lagrange_Polynomial_Interpolation():

    def __init__(self, points):
        self._x = [p[0] for p in points]
        self._y = [p[1] for p in points]
        self._n = len(points)
    
    def __call__(self, x):
        return sum([self._lambda(i, x) * self._y[i] for i in range(0, self._n)])
    
    def _lambda(self, k, x):
        mult = 1
        for j in range(0, self._n):
            if not j==k:
                mult *= ( x - self._x[j] ) / ( self._x[k] - self._x[j] )
        return mult