import matplotlib.pyplot as plt
import interpolation as intp

""" sx and sy arguments generator """
def t(n):
    for i in range (0, n+1):
        yield i/(n)

def show_plot(x,y):
    """ create interpolating functions to determine points on the Cartesian coordinate system """
    sx = intp.Interpolation(list(t(len(x)-1)), x)
    sy = intp.Interpolation(list(t(len(y)-1)), y)

    """ values of interpolating functions: sx and sy """
    xx = [sx(h) for h in t(1000)]
    yy = [sy(h) for h in t(1000)]

    """ create and show a new plot for points Ak = (xx[k], yy[k]) """
    fig = plt.figure(figsize=(4,6))
    pl = plt.plot(xx,yy)
    plt.show()

""" x : list of values that sx(t) should interpolate """
x1 = [15.5,12.5,8,10,7,4,8,10,9.5,14,18,17,22,25,19,24.5,23,17,16,12.5,16.5,21,17,11,5.5,7.5,10,12]

""" y : list of values that sy(t) should interpolate """
y1 = [32.5,28.5,29,33,33,37,39.5,38.5,42,43.5,42,40,41.5,37,35,33.5,29.5,30.5,32,19.5,24.5,22,15,10.5,2.5,8,14.5,20]

show_plot(x1,y1)