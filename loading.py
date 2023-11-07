import time
import curses
import random
from termcolor import colored

#Time conversion
one_minute = 600
one_hour = one_minute * 60
two_hours = one_hour * 2

#Sets up the screen and hides the cursor
curses.initscr()
curses.curs_set(0)

switch = 1
direction = 1
#Max length of "loading dots"
length = 30

#Color options
colors = ["red", "cyan", "grey", "green", "yellow", "magenta"]
color = colors[random.randint(0,5)]

#Opening message
print("Sleep timer running")
print(" " * 50, end="\r", flush=True)

#Loading dots loop
for i in range(two_hours): #Two hour timer
    print(" " * direction*3, end="\r", flush=True)
    print(colored("." * direction, color, attrs=["bold"]), end="\r", flush=True)
    time.sleep(0.1)
    #Change direction and color
    if((i+1)%length==0):
        switch*=(-1)
        color = colors[random.randint(0,5)]

    #Velocity
    if(switch == 1):
        direction+=1
    if(switch == (-1)):
        direction-=1


#Reset the screen
curses.curs_set(1)
curses.endwin()