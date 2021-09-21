import os 
import tensorflow as tf
import json
 
import numpy as np
import matplotlib.pyplot as plt
import math


SAMLPES = 1000
SEED = 1337

np.random.seed(SEED)
tf.random.set_seed(SEED)