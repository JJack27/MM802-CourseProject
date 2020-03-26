import numpy as np

def distance_2d(loc1, loc2):
    return np.linalg.norm(loc1, loc2)

def sigmoid(x):
    return 1/(1 + np.exp(-x)) 