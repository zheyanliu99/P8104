# %% import packages
import random
import math

# %%  First simulation
# function to generate y according to x
def generate_y(x):
    r = random.random()
    if r < 0.5:
        y = math.sqrt(1 - x**2)
    else:
        y = -math.sqrt(1 - x**2)
    return y

def Bertrand(n):
    c = math.sqrt(3)
    cnt = 0
    # randomly generate two Abscissas
    for _ in range(n):
        x1 = 2 * random.random() - 1 
        x2 = 2 * random.random() - 1
        y1 = generate_y(x1) 
        y2 = generate_y(x2) 
        # calculate distance between (x1,y1) and (x2,y2)
        dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if c < dist:
            cnt += 1
    return cnt/n


# %% Second simulation
def Bertrand2(n):
    c = math.sqrt(3)
    cnt = 0
    # randomly generate two degrees
    for _ in range(n):
        degree1 = 2*math.pi*random.random()
        degree2 = 2*math.pi*random.random()
        x1 = math.cos(degree1)
        x2 = math.cos(degree2)
        y1 = math.sin(degree1)
        y2 = math.sin(degree2)
        # calculate distance between (x1,y1) and (x2,y2)
        dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if c < dist:
            cnt += 1
    return cnt/n

# %% Simulation and compare
n = 1000000
delta = 0.02
Bertrand(n) - Bertrand2(n) < delta # Not Converge to same number
# The first one converged to 0.36 and the second one 0.33
