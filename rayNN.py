from math import sqrt, atan, pi
import sys,random, keyboard
import tkinter as tk
from tkinter import *
import tensorflow as tf
import keras
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import numpy as np
import h5py, random
from PIL import Image
from tqdm import tqdm
from glob import glob
tf.logging.set_verbosity(tf.logging.ERROR)

model = load_model("Sphere.h5")
#model.summary()
#keras.utils.plot_model(model, "model.png", show_shapes=True)

def dirToProp(dir):  #turns directions [-0.5*pi,0.5*pi] to propotion [0,1]
    return dir/pi+0.5
def propToDir(prop):  #turns propotion [0,1] to directions [-0.5*pi,0.5*pi]
    return (prop-0.5)*pi

def length(o,p):
    return sqrt((o[0]-p[0])**2+(o[1]-p[1])**2+(o[2]-p[2])**2)

def GetDistFromAngle(point):
    sphere     = [2.,3.,0.,0.5]
    sphereDist = length(point,sphere)-sphere[3]
    rX, rY, rZ = point[0]-sphere[0], point[1]-sphere[1], point[2]-sphere[2]
    aX, aY     = atan(rY/(rX+0.00001)), atan(rZ/(rX+0.00001))
    direction  = np.array([[dirToProp(aX), dirToProp(aY)]])
    position   = np.array([[rX, rY, rZ]])
    distance   = np.array([sphereDist+sphere[3]])
    arr = [direction,position,distance]
    sphereDistNN = model.predict(arr)[0][0]*(sphereDist+sphere[3])
    planeDist  = point[1]
    distance   = min(sphereDist,planeDist)
    return distance

#GetDistFromAngle([0,5,0])
