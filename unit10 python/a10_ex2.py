import numpy as np

def elements_wise(arr: np.ndarray, f):
   vectorized_func = np.vectorize(f)
   arr[:] = vectorized_func(arr)

def func(x):
    return x*x + 3*x + 2

