# GlowScript 3.1 VPython
# This Python code can be copied into a Trinket project.
# It can also be copied into a Jupyter Notebook, presuming the correct packages are installed.

# Open this code in Trinket
# https://trinket.io/library/trinkets/a2e31a1688

from vpython import * # Delete this line for Trinket

x = -100
y = 0
t = 0.1
cat = sphere(pos=vector(x,y,0), radius=10)
for i in range(500):
  rate(100)
  x = x + (t * (-1) * y)
  y = y + (t * x)
  cat.pos = vector(x,y,0)