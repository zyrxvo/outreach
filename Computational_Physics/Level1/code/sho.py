########################################################
# Mass on a Spring
# Garett Brown, 14 May 2021
# Learning how to solve physics problems with computers.
# Inspired by Daniel Shiffman (https://thecodingtrain.com/CodingChallenges/093-double-pendulum.html)
########################################################

# Open this code in Trinket
# https://trinket.io/library/trinkets/04931fe5c8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

m = 1
k = 1
x = 1
v = 0
a = 0
dt = 0.01
t = 0

# ***********************************

# Set the number of frames to animate
nframes = 628
data = np.zeros(nframes)
for i in range(nframes):
  
# ***********************************
#        Code Solution Here:
# ***********************************
  
  
  a = -(k/m)*x
  v = v + a*dt
  x  = x + v*dt
  
  
# ***********************************

# Save snapshot of data to Animate
  data[i] = x


########################################################
########################################################
# Animate Data
# Adapted from https://matplotlib.org/stable/api/animation_api.html
########################################################

fig, ax = plt.subplots(1,1, figsize=(8,8))
xdata, ydata = [], []
ln, = plt.plot([], [], 'ko', ms=15)

def init():
    ax.set_xlim(np.min(data)*1.1, np.max(data)*1.1)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata = data[frame]
    ydata = 0
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(nframes), init_func=init, interval=1)
plt.show()

########################################################
########################################################