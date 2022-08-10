import numpy as np
import matplotlib.pyplot as plt
import time
from IPython import display

#create a ball, the first item is the x position and the second item is the y position
ball = np.array([0.0,15.0])

#Set up the scene for the ball - don't worry about this part too much!
plt.title("Time of snapshot:  0.00 (wait...)")
plt.axis([-8,8,0,16])   #set x and y axis limits
plt.plot(ball[0],ball[1], marker='o',markersize=5, color='red' ) #plot the ball position with the appropriate marker
display.clear_output(wait=True) #clear the previous display
display.display(plt.gcf())  #display what's being plotted currently
plt.clf()   #clear the plot
time.sleep(0.75)  #pause updates by 0.5s

#define the ball's initial velocity, and acceleration due to gravity
ball_vel = np.array([0.0,0.0])
g = 9.8

#set the initial time=0 and set the time step and frame rate for snapshots
t = 0.0
dt = 0.01
frate = 10
frame = 0

##This "while" loop repeats the commands indented after it while the condition is true
while ball[1] >= 0.0: #ie while the y position of the ball is greater than 0
    t = t + dt   #take 1 time step

    ball_vel[1] = ball_vel[1] - g*dt    #v_f=v_i+a*dt

    ball[1] = ball[1] + ball_vel[1]*dt   #y_f=y_i+v*dt  Plots the ball at the new y value

    #Take a snapshot of the ball as it's falling - don't worry about this section for now.
    frame = frame + 1
    if (frame%frate == 0):
        plt.title("Time of snapshot: {0:5.2f}".format(t))
        plt.axis([-8,8,0,16])
        plt.plot(ball[0], ball[1], marker='o', markersize=5, color='red')
        display.clear_output(wait=True)
        display.display(plt.gcf())
        plt.clf()
        time.sleep(0.01)

print("Total falling time: " + repr(t) )