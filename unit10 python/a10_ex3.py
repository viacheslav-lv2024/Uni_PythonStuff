import numpy as np

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 1:
        raise ValueError(f"The function can work for 1D matrices, not {arr.ndim}D")

    # Sort unique values in the array
    unique_values = np.unique(arr)
    
    # Initialize an empty 2D array to store the one-hot encoding
    encoding_matrix = np.zeros((arr.size, unique_values.size), dtype=int)
    
    # Fill in the one-hot encoding matrix
    for i, value in enumerate(arr):
        #(np.where(unique_values == value)[0]) is a unique's element position stored in a one-element tuple 
        encoding_matrix[i][np.where(unique_values == value)[0]] = 1
    
    return encoding_matrix


