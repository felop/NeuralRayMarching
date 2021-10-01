# Ray marches throught the scene with:
# INPUT  --->  distance function of an object
# OUTPUT --->  distance map of the scene

from math import sqrt, atan, pi
import numpy as np
from rayNN import GetDistFromAngle

MAX_STEP = 100
MAX_DIST = 100
SURFACE_DIST = 0.01

distanceMapNN = np.zeros((45,80))

###################
# maths functions #
###################

def length(o,p):
    return sqrt((o[0]-p[0])**2+(o[1]-p[1])**2+(o[2]-p[2])**2)

def product(list0,list2):
    facteurs = []
    for num0, num2 in zip(list0, list2):
        facteurs.append(num0 * num2)
    return facteurs

def addition(list0,list2):
    termes = []
    for num0, num2 in zip(list0, list2):
        termes.append(num0 + num2)
    return termes

def normalize(v):
    v = np.array(v)
    v = v / np.sqrt(np.sum(v**2))
    return list(v)

###################
# maths functions #
###################

def GetDist(point):
    sphere      = [0.,3.,5.,0.5]
    sphereDist  = length(point,sphere)-sphere[3]
    planeDist   = point[1]
    distance    = min(sphereDist,planeDist)
    return distance

def RayMarch(ro, rd):
    global distanceMapNN
    dO = 0
    for i in range(MAX_STEP):
        p   = addition(ro, [rd[0]*dO,rd[1]*dO,rd[2]*dO] )
        dS  = GetDistFromAngle(p)
        dO += dS
        if dO>=MAX_DIST or dS<=SURFACE_DIST:
            break
    return dO

def ImageGen(x,y,resolution):
    uv = [(x-.5*resolution[0])/resolution[1],(y-.5*resolution[1])/resolution[1]]
    ro = [0,2.6,0]
    col = [0,0,0]
    rd = normalize((uv[0],uv[1],1))
    dist = RayMarch(ro,rd)/10
    col = [dist,dist,dist]
    return col
