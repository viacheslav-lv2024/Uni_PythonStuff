import numpy as np

def extend(arr: np.ndarray, rows: int, cols: int, fill=None) -> np.ndarray:
    if arr.ndim != 2:
        raise ValueError(f"can only extend 2D arrays, not {arr.ndim}D")
    if rows < arr.shape[0]:
        raise ValueError("invalid rows")
    if cols < arr.shape[1]:
        raise ValueError("invalid cols")
    if fill and not isinstance(fill, (int, float)):
        raise ValueError("invalid fill")
    
        
    if fill:
        new_array = np.zeros((arr.shape[0], cols), dtype=int)
        for row_i in range(0, arr.shape[0]):
            new_array[row_i] = np.append(arr[row_i], np.full((cols-arr.shape[0]-1,), fill))
        for row_i in range(arr.shape[0], rows):
            new_array = np.vstack((new_array, np.full((cols,), fill)))
    else:
        new_array = np.zeros((arr.shape[0], cols), dtype=int)
        n = rows - arr.shape[0] # Defining n for readability further
        m = cols - arr.shape[1] # Same with m
        for row_i in range(0, arr.shape[0]):
            a = np.mean(arr[row_i], axis=0)
            b = np.full((n,), a)
            new_array[row_i] = np.append(arr[row_i], b)
        for row_i in range(arr.shape[0], rows):
            mean_cols = arr.mean(axis=0, dtype=int) if arr.dtype == int else arr.mean(axis=0)
            mean_arr = np.full((m,), np.mean(arr.flatten(), dtype = int if arr.dtype == int else None, axis=0))
            new_array = np.vstack([new_array, np.concatenate(([mean_cols, mean_arr]), axis=0)])

    return new_array


