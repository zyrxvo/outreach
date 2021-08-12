# ***************************************************
# Objects in Motion
# Garett Brown, 14 May 2021
# Learning how to solve physics problems with computers.
# Python
# ***************************************************

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Open this code in Trinket
# https://trinket.io/library/trinkets/a2e31a1688

# ***************************************************
# Initial Conditions
# ***************************************************
x = -1
y = 0
t = 0.01
# ***************************************************

# Set the number of frames to animate
nframes = 628
data = np.zeros((nframes, 2))
for i in range(nframes):
# ***************************************************
# Code Solution Here
# ***************************************************

  x = x + (t * (-1) * y)
  y = y + (t * x)

# ***************************************************

# Save snapshot of data to Animate
  data[i] = [x,y]


# ***************************************************
# ***************************************************
# Animate Data
# Adapted from https://matplotlib.org/stable/api/animation_api.html
# ***************************************************

fig, ax = plt.subplots(1,1, figsize=(8,8))
xdata, ydata = [], []
ln, = plt.plot([], [], 'ko', ms=15)

def init():
    ax.set_xlim(np.min(data[:,0])*1.1, np.max(data[:,0])*1.1)
    ax.set_ylim(np.min(data[:,1])*1.1, np.max(data[:,1])*1.1)
    return ln,

def update(frame):
    xdata, ydata = data[frame]
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(nframes), init_func=init, interval=1)
plt.show()

# ***************************************************