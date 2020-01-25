import math

"""
NIFS3 (pl. Naturalna Interpolacyjna Funkcja Sklejana 3-go stopnia)

Polynomial interpolating function using given points (x, f(x)) 

Spline : https://en.wikipedia.org/wiki/Spline_interpolation#Algorithm_to_find_the_interpolating_cubic_spline
"""

class Interpolation:
    def __init__(self,x,y):
        """ x, y : lists of coordinates """
        """ Moments :  s''(Xi) where s(x) is the interpolating polynomial"""
        """ needed to calculate s(x) """
        self.x = x # sorted with ascending order
        self.y = y # corresponding values ​​= f(x)
        self.Momoents = Interpolation.table_of_moments(x,y)

    """ make object callable """
    def __call__(self,xx):
        for i in range(1,len(self.x)):
            """ check which part of the function you should use """
            if xx <= self.x[i]:
                return Interpolation.s(i, self.x, self.y, self.Momoents,xx)
        return Interpolation.s(len(self.x)-1, self.x, self.y, self.Momoents,xx)

    @staticmethod
    def f_table(x,y):
        """ 
        returns 2d table 'f' contains differential quotients of the interpolated function 

        x  ||  y = f[i] |   f[i,j]   |   f[i,j,k]
        ---++-----------+------------+-------------
        x0 ||     y0    |   0        |   0
        x1 ||     y1    |   f[0,1]   |   0
        x2 ||     y2    |   f[1,2]   |   f[0,1,2]
        x3 ||     y3    |   f[2,3]   |   f[1,2,3]
        x4 ||     y4    |   f[3,4]   |   f[2,3,4]
        .. ||     ..    |   ...      |   ...

                  f[j] - f[i]                   f[j,k] - f[i,j]
        f[i,j] = ------------- ,    f[i,j,k] = ------------------
                    Xj - Xi                         Xk - Xi
  
        self._diff_quos[i][0] == f[i]
        self._diff_quos[i][1] == f[i-1, i]
        self._diff_quos[i][2] == f[i-2, i-1, i] 

        We will be interested in self._diff_quos[i][2].
        

        f[n], f[n-1, n], f[n-2, n-1, n] 

        | x    ||   y      |   f[i,j]    |     f[i,j,k]     |
        +------++----------+-------------+------------------+
        | ..   ||  ...     |    ...      |        ...       |
        | xn-1 ||  f[n-1]  | f[n-2, n-1] | f[n-3, n-2, n-1] |
        |      ||        \ |           \ |                  |
        |      ||          \             \                  | 
        |  xn  ||   f[n] --- f[n-1, n] --- f[n-2, n-1, n]   |

        To calculate f[i-1, i, i+1] we need f[i-1, i] ,  f[i, i+1] ,  x[i+1] and x[i],
        so we can calculate new rows in time O(1), because len(row) = 3

        Complexity of calculating the table is linear ( O(n) ).
        """
        n = len(x)
        f = []
        for i in range(0,n):
            f += [ [y[i], 0, 0] ]
        for i in range(1,n):
            f[i][1] = ( f[i][0] - f[i-1][0] ) / (x[i] - x[i-1])
        for i in range(2,n):
            f[i][2] = ( f[i][1] - f[i-1][1] ) / (x[i] - x[i-2])
        return f

    @staticmethod
    def table_of_moments(x,y):
        """
        create interpolation moments table after loading the set of interpolation nodes

        Interpolation Moments satisfies equality:

        l[k]*M[k-1] + 2*M[k] + (1-l[k])*M[k+1] = 6 * f[k-1, k, k+1]

        so they are expressed by the formula:

                D[k] - l[k]*M[k-1] - (1-l[k])*M[k+1]
        M[k] = ----------------------------------------
                                2

        But we can use the another algorithm!

        Solve system of equations (matrix form): A*M = D
        Where:                          
                                            A                                                 M                   D 

        |    2,  1-l[1],        0,        0,        0,        0,     ...,          0 |  |  M[1]  |         |  d[1]  |
        | l[2],       2,   1-l[2],        0,        0,        0,     ...,          0 |  |  M[2]  |         |  d[2]  |
        |    0,    l[3],        2,   1-l[3],        0,        0,     ...,          0 |  |  M[3]  |         |  d[3]  |
        |    0,       0,     l[4],        2,   1-l[4],        0,     ...,          0 |  |  ...   |  _____  |  ...   |
        |    0,       0,        0,      ...,      ...,      ...,       0,          0 |  |  ...   |  _____  |  ...   |
        |  ...,     ...,      ...,      ...,      ...,      ...,     ...,          0 |  |  ...   |         |  ...   |
        |  ...,     ...,      ...,      ...,      ...,      ...,     ...,          0 |  |  ...   |         |  ...   |
        |    0,       0,        0,        0,        0,   l[n-2],       2,   1-l[n-2] |  | M[n-2] |         | d[n-2] |
        |    0,       0,        0,        0,        0,        0,  l[n-1],          2 |  | M[n-1] |         | d[n-1] |

        We can find Moment's in linear time! ( O(n) )


        Algorithm to solve it:
        +-----
        |
        |  q[0] = 0
        |
        |  U[0] = 0
        |
        |  p[k] =  l[k]*q[k-1] + 2
        |
        |          l[k] - 1  
        |  q[k] = ----------
        |            p[k]
        |
        |
        |          d[k] - l[k]*U[k-1]  
        |  U[k] = ---------------------
        |                  p[k]
        |
        |
        |  M[n-1] = U[n-1]
        |
        |  M[k] = U[k] + q[k]*M[k+1]
        |
        +-----

        where: 
            M[0] = M[n] = 0
            d[k] = 6 * f[k-1, k, k+1]
            q[0] = U[0] = 0

                     x[k] - x[k-1]            h[k]
            l[k] = -----------------  =  ---------------
                    x[k+1] - x[k-1]       h[k+1] + h[k]


            h[k] = x[k] - x[k-1]
        
        M[i] == S''(Xi) 
        """
        n = len(x)
        Momoents = list(range(0,n))
        Momoents[n-1] = 0
        Momoents[0] = 0
        U,q = Interpolation.U_q_table(x,y)
        for i in range(n-2, 0, -1):
            Momoents[i] = U[i] + q[i]*Momoents[i+1] 
        return Momoents


    @staticmethod
    def U_q_table(x,y):
        """ returns lists U and q needed to calculate moments (Mi - ith moment = s''(Xi)) """
        n = len(x)-1
        f = Interpolation.f_table(x,y)
        U,q = [None],[None]
        U += [3 * f[2][2]]                             # U1
        q += [(1 - (x[1]-x[0]) / (x[2]-x[0])) / 2]     # q1
        for i in range(2,n):
            li = ( x[i]-x[i-1] ) / (x[i+1]-x[i-1])
            di = 6 * f[i+1][2]
            q += [( 1 - li ) / (2 + li*q[i-1])]
            U += [(di - li*U[i-1]) / ( 2 + li*q[i-1] )]
        return U,q
        

    @staticmethod
    def s(k, x, y, Momoents, xx):
        """ k-th part of the interpolating polynomial """
        h = x[k] - x[k-1]
        x_xk = xx - x[k-1]
        xk_x = x[k] - xx
        return 1/h*( 1/6 * Momoents[k-1] * xk_x**3  +  
                     1/6 * Momoents[k]   * x_xk**3  +  
                     ( y[k-1] - 1/6 * Momoents[k-1] * (h**2) ) * xk_x +
                     ( y[k]   - 1/6 * Momoents[k]   * (h**2) ) * x_xk )
