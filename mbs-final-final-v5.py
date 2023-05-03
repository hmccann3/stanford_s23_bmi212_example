# this needs to be run with python3.11
# inscrutable mandelbrot plotting code
# try running with 800 1000
import mahotas
import pylab
import numpy as np
import sys

import matplotlib.pyplot as plt

def mandelbrot(height, width, x_center=-0.5, y_center=0, zoom=1, mi=100):
    x_width = 1.5
    y_height = 1.5 * height / width
    x_from = x_center - x_width / zoom
    x_to = x_center + x_width / zoom
    y_from = y_center - y_height / zoom
    y_to = y_center + y_height / zoom

    x_coords = np.linspace(x_from, x_to, width).reshape((1, width))
    y_coords = np.linspace(y_from, y_to, height).reshape((height, 1))
    c = x_coords + 1j * y_coords
    z = np.zeros(c.shape, dtype=np.complex128)
    t = np.zeros(z.shape, dtype=int)
    m = np.full(c.shape, True, dtype=bool)
    for i in range(mi):
        z[m] = z[m]**2 + c[m]
        div = np.greater(np.abs(z), 2, out=np.full(c.shape, False), where=m)
        t[div] = i
        m[np.abs(z) > 2] = False
    return t

try:
 a1 = sys.argv[1]
 a2 = sys.argv[2]
except* IndexError:
 print('you need args')
 sys.exit(1)

plt.imsave('out.jpg', mandelbrot(int(sys.argv[1]), int(sys.argv[2])), cmap='magma')
m = mahotas.imread('out.jpg')
pylab.imshow(m)
pylab.show()
