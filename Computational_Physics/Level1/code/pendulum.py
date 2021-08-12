# GlowScript 3.1 VPython

# Open this code in Trinket
# https://trinket.io/library/trinkets/77ae8a6382

# Garett Brown
# Inspired by Daniel Shiffman (https://thecodingtrain.com/CodingChallenges/093-double-pendulum.html)

from vpython import * # Delete this line for Trinket

pi = 3.141592653589793238462643383279502884197

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

L = 10          # Length
m = 1           # mass
theta = pi/3    # Initial Angle
omega = 0       # Initial Angular Velocity 
alpha = 0       # Initial Angular Acceleration
b = 0.1         # Damping Coefficient
g = 9.8         # Strength of Gravity
dt = 0.001      # Time step
t = 0           # Current time

# ***********************************

# Used for drawing the Pendulum.
x = L * sin(theta)
y = -L * cos(theta)
c = curve(vector(0,0,0), vector(x,y,0))
p = sphere(pos = vector(x,y,0), radius=m)
bx = box(pos = vector(0,0,0), length=L, height=0.1, width=L)

while t < 100:
  rate(7500)
  t = t + dt
  
# ***********************************
#        Code Solution Here:
# ***********************************

  alpha = -(g/L)*sin(theta)
  omega = omega + alpha * dt
  theta = theta + omega * dt
  
# ***********************************
  
  # Animate the pendulum.
  x = L * sin(theta)
  y = -L * cos(theta)
  c.modify(1, pos = vector(x,y,0))
  p.pos = vector(x,y,0)
  