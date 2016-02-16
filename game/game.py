import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple
import random

class Agent:
    id = -1
    x = 10.0
    y = 10.0
    r = 1.0
    angle = 0.3 * np.pi

    def __init__(self):
        pass

    def __init__(self, id):
        self.id = id


Rect = namedtuple("Rect", ["x1", "x2", "y1", "y2"])
World = namedtuple("World", ["agents", "border"])


####################### utils ######################

def IsOverlap(a, b):
    """
    do two agents overlap with each other?
    """
    return (a.x - b.x)**2 + (a.y - b.y)**2 < (a.r + b.r)**2

def IsInRect(a, rect):
    return  rect.x1 < a.x - a.r and \
            a.x + a.r < rect.x2 and \
            rect.y1 < a.y - a.r and \
            a.y + a.r < rect.y2

##################### Algorithms ######################

def AllocateAgents(ags, rect):
    i = 0
    for t in range(max(1000, len(ags))):
        a.x = rect.x1 + random.random()*(rect.x2-rect.x1)
        a.y = rect.y1 + random.random()*(rect.y2-rect.y1)

        if not IsInRect(a, rect):
            continue

        isOverlapped = False
        for k in range(i):
            if IsOverlap(a, ags[k]):
                isOverlapped = True
                break
        if isOverlapped:
            continue

        ags[i].x = a.x
        ags[i].y = a.y
        ags[i].angle = random.random()*2*np.pi

        i += 1
        if i == len(ags):
            return True     # allocate all the agents successfully

    return False    # failed to allocate these agents

######################## Plot ######################

def PlotRect(rect, color, linewidth=1):
    plt.plot([rect.x1, rect.x2], [rect.y1, rect.y1], color, lw=linewidth)
    plt.plot([rect.x1, rect.x2], [rect.y2, rect.y2], color, lw=linewidth)
    plt.plot([rect.x1, rect.x1], [rect.y1, rect.y2], color, lw=linewidth)
    plt.plot([rect.x2, rect.x2], [rect.y1, rect.y2], color, lw=linewidth)

def PlotCircle(x, y, r, color):
    t = np.linspace(0, 2*np.pi, 36)
    xs = x + r * np.cos(t)
    ys = y + r * np.sin(t)
    plt.plot(xs, ys, color)

def PlotAgent(a):
    PlotCircle(a.x, a.y, a.r, 'b')
    plt.plot([a.x, a.x + a.r*np.cos(a.angle)], [a.y, a.y + a.r*np.sin(a.angle)], 'b')
    #plt.text(a.x, a.y, '%d' % a.id)


def PlotWorld(world):
    plt.clf()
    plt.hold(True)

    PlotRect(world.border, 'r', linewidth=2)

    for a in world.agents:
        PlotAgent(a)

    plt.axis(world.border)
    plt.axis('equal')


################ main ################
N = 10
rect = Rect(0.0, 50.0, 0.0, 50.0)

agents = []
for i in range(N):
    a = Agent(i + 1)
    agents.append(a)

world = World(agents=agents, border=rect)

AllocateAgents(agents, rect)
PlotWorld(world)


print "complete"