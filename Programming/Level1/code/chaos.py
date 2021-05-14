# GlowScript 3.1 VPython

# Open this code in Trinket
# https://trinket.io/library/trinkets/065cd7ab36

# Daniel Shiffman
# https://thecodingtrain.com/CodingChallenges/093-double-pendulum.html
# https://youtu.be/uWzPe_S-RVE

# Modifications by Garett Brown

from vpython import * # Delete this line for Trinket

pi = 3.141592653589793238462643383279502884197

# ***********************************
#   Set Initial Conditions Here:
# ***********************************

# Double Pendulum A
r1_A = 10
r2_A = 10
m1_A = 10
m2_A = 10
theta1_A = pi/2
theta2_A = pi/2
omega1_A = 0
omega2_A = 0

# Double Pendulum B
r1_B = 10
r2_B = 10
m1_B = 10
m2_B = 10
theta1_B = pi/2
theta2_B = pi/2.001
omega1_B = 0
omega2_B = 0

g = 1
dt = 0.002
t = 0

# ***********************************

x1_A = r1_A * sin(theta1_A)
y1_A = -r1_A * cos(theta1_A)
x2_A = x1_A + r2_A * sin(theta2_A)
y2_A = y1_A - r2_A * cos(theta2_A)

x1_B = r1_B * sin(theta1_B)
y1_B = -r1_B * cos(theta1_B)
x2_B = x1_B + r2_B * sin(theta2_B)
y2_B = y1_B - r2_B * cos(theta2_B)

L = r1_A + r2_A
c1_A = curve(vector(0,0,0), vector(x1_A,y1_A,0))
p1_A = sphere(pos = vector(x1_A,y1_A,0), radius=1)
c2_A = curve(vector(x1_A,y1_A,0), vector(x2_A,y2_A,0))
p2_A = sphere(pos = vector(x2_A,y2_A,0), radius=1)
c1_B = curve(pos=[vector(0,0,0), vector(x1_B,y1_B,0)], color=color.red)
p1_B = sphere(pos = vector(x1_B,y1_B,0), radius=1, color=color.red)
c2_B = curve(pos=[vector(x1_B,y1_B,0), vector(x2_B,y2_B,0)], color=color.red)
p2_B = sphere(pos = vector(x2_B,y2_B,0), radius=1, color=color.red)
bx = box(pos = vector(0,0,0), length=L, height=0.1, width=L)
attach_trail(p2_A)
attach_trail(p2_B, color=color.red)

while t < 500:
  rate(10000)
  t += dt
  
  num1 = -g * (2 * m1_A + m2_A) * sin(theta1_A)
  num2 = -m2_A * g * sin(theta1_A - 2 * theta2_A)
  num3 = -2 * sin(theta1_A - theta2_A) * m2_A
  num4 = omega2_A * omega2_A * r2_A + omega1_A * omega1_A * r1_A * cos(theta1_A - theta2_A)
  den = r1_A * (2 * m1_A + m2_A - m2_A * cos(2 * theta1_A - 2 * theta2_A))
  alpha1_A = (num1 + num2 + num3 * num4) / den

  num1 = 2 * sin(theta1_A - theta2_A)
  num2 = (omega1_A * omega1_A * r1_A * (m1_A + m2_A))
  num3 = g * (m1_A + m2_A) * cos(theta1_A)
  num4 = omega2_A * omega2_A * r2_A * m2_A * cos(theta1_A - theta2_A)
  den = r2_A * (2 * m1_A + m2_A - m2_A * cos(2 * theta1_A - 2 * theta2_A))
  alpha2_A = (num1 * (num2 + num3 + num4)) / den

  num1 = -g * (2 * m1_B + m2_B) * sin(theta1_B)
  num2 = -m2_B * g * sin(theta1_B - 2 * theta2_B)
  num3 = -2 * sin(theta1_B - theta2_B) * m2_B
  num4 = omega2_B * omega2_B * r2_B + omega1_B * omega1_B * r1_B * cos(theta1_B - theta2_B)
  den = r1_B * (2 * m1_B + m2_B - m2_B * cos(2 * theta1_B - 2 * theta2_B))
  alpha1_B = (num1 + num2 + num3 * num4) / den

  num1 = 2 * sin(theta1_B - theta2_B)
  num2 = (omega1_B * omega1_B * r1_B * (m1_B + m2_B))
  num3 = g * (m1_B + m2_B) * cos(theta1_B)
  num4 = omega2_B * omega2_B * r2_B * m2_B * cos(theta1_B - theta2_B)
  den = r2_B * (2 * m1_B + m2_B - m2_B * cos(2 * theta1_B - 2 * theta2_B))
  alpha2_B = (num1 * (num2 + num3 + num4)) / den

  omega1_A += alpha1_A * dt
  omega2_A += alpha2_A * dt
  theta1_A += omega1_A * dt
  theta2_A += omega2_A * dt


  omega1_B += alpha1_B * dt
  omega2_B += alpha2_B * dt
  theta1_B += omega1_B * dt
  theta2_B += omega2_B * dt

  # omega1_A *= 0.99
  # omega2_A *= 0.99

  # omega1_B *= 0.99;
  # omega2_B *= 0.99;

  x1_A = r1_A * sin(theta1_A)
  y1_A = -r1_A * cos(theta1_A)
  x2_A = x1_A + r2_A * sin(theta2_A)
  y2_A = y1_A - r2_A * cos(theta2_A)

  x1_B = r1_B * sin(theta1_B)
  y1_B = -r1_B * cos(theta1_B)
  x2_B = x1_B + r2_B * sin(theta2_B)
  y2_B = y1_B - r2_B * cos(theta2_B)
  
  c1_A.modify(1, pos = vector(x1_A,y1_A,0))
  p1_A.pos = vector(x1_A,y1_A,0)
  c2_A.modify(0, pos = vector(x1_A,y1_A,0))
  c2_A.modify(1, pos = vector(x2_A,y2_A,0))
  p2_A.pos = vector(x2_A,y2_A,0)
  c1_B.modify(1, pos = vector(x1_B,y1_B,0))
  p1_B.pos = vector(x1_B,y1_B,0)
  c2_B.modify(0, pos = vector(x1_B,y1_B,0))
  c2_B.modify(1, pos = vector(x2_B,y2_B,0))
  p2_B.pos = vector(x2_B,y2_B,0)

