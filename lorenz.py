import matplotlib.pyplot as plt
import numpy as np

num_steps = 10000  
dt = 0.01  #

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0


x, y, z = 1.0, 1.0, 1.0


xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)


xs[0] = x
ys[0] = y
zs[0] = z


for i in range(num_steps):
  
  dx = sigma * (y - x)
  dy = x * (rho - z) - y
  dz = x * y - beta * z

  x += dx * dt
  y += dy * dt
  z += dz * dt

  
  xs[i + 1] = x
  ys[i + 1] = y
  zs[i + 1] = z

 
fig = plt.figure()
ax = fig.add_subplot(projection='3d')


ax.plot(xs, ys, zs, lw=0.6, color='purple')

ax.set_title('Lorentz attractor(butterfly effect)')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


plt.show()