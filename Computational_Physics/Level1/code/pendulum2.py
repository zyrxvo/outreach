########################################################
# Mass on a Spring
# Garett Brown, 14 May 2021
# Learning how to solve physics problems with computers.
# Inspired by Daniel Shiffman (https://thecodingtrain.com/CodingChallenges/093-double-pendulum.html)
########################################################

# This script was designed to run locally using Matplotlib instead of Glowscript.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

g = 9.8 # Gravity
L = 1 # Length of the massless rod
theta = np.pi*0.95 # Starting angle (0 < theta < pi)
omega = -1  # Starting angular velocity
alpha = -(g/L)*np.sin(theta) # Initial angular acceleration
dt = 0.001 # Integrator timestep
t = 0 # Elapsed time

# ***********************************

# Set the number of frames to animate so that it repeats after one period, 
#   assuming the inital angular velocity is zero.
# Calculate the number of frames by computing the period of the pendulum based 
#   on L and theta using Taylor Series expansion, see https://en.wikipedia.org/wiki/Pendulum#Period_of_oscillation
def f(n):
    n0 = np.math.factorial(2*n)
    n1 = 2**(2*n)
    n2 = (np.math.factorial(n))**2
    n3 = (((n0)/(n1*n2))**2)
    n4 = (np.sin(theta/2.))**(2*n)
    return n3 * n4
F = np.vectorize(f)
nterms = 1000 # 1000 terms is sufficient for starting angles up to theta = pi*0.95
nframes = int(np.ceil((2.*np.pi * np.sqrt(L/g)/dt) * np.sum(F(np.arange(nterms)))))
data = np.zeros((nframes,2,2))
for i in range(nframes):
  
# ***********************************
#        Code Solution Here:
# ***********************************
  
  
  alpha = -(g/L)*np.sin(theta)
  omega += alpha*dt
  theta += omega*dt
  t += dt
  
  
# ***********************************

# Save snapshot of data to Animate the massless rod and the pendulum bob.
  data[i] = np.array([[0, L*np.sin(theta)], [0, -np.cos(theta)]])


########################################################
########################################################
# Animate Data
# Adapted from https://matplotlib.org/stable/api/animation_api.html
########################################################

fig, ax = plt.subplots(1,1, figsize=(8,8))
plt.title('Simple Pendulum')
xdata, ydata = [], []
massless_rod, = plt.plot([], [], 'k.-')
pendulum_bob, = plt.plot([], [], 'ko', ms=15)

def init():
    ax.set_xlim(-1.1*L, 1.1*L)
    ax.set_ylim(-1.1*L, 1.1*L)
    return pendulum_bob, massless_rod,

def update(frame):
    xdata,ydata = data[frame]
    massless_rod.set_data(xdata, ydata)
    pendulum_bob.set_data(xdata[1], ydata[1])
    return pendulum_bob, massless_rod,

ani = FuncAnimation(fig, update, frames=np.arange(nframes), init_func=init, interval=1)
plt.show()

########################################################
########################################################