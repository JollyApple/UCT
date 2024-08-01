import numpy as np
import math
from matplotlib import pyplot as plt

oofpez = 8.988e9         #Coulomb's constant

#charge of interest
qsys = -1.6e-19             #charge on electron in Coulombs
m = 9.1093837e-31               #mass of electron
vsys = np.array([3.0e5, 0, 0])             #initial velocity of electron
rsys = np.array([0,0,0])             #initial position of electron
efield = np.array([0, 5e3, 0])    #strength of uniform electric field

dt = 1.0e-16
t = 0
tf = 3.0e-14

x_arr = []
y_arr = []

while t < tf:
    print(t, '      ', rsys)
    x = rsys[0] + vsys[0]*t
    y = rsys[1] + (qsys*efield[1]*(t**2))/(2*m)
    rsys = np.array([x, y, 0])
    x_arr.append(x)
    y_arr.append(y)

    t = t + dt                          #calculate next time.

plt.plot(x_arr,y_arr, color='red')
plt.xlim(0, 1.5e-6)
plt.ylim(-5e-11, 5e-11)
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.title('Trajectory of electron in uniform electric field (WPS 13)')
plt.show()
