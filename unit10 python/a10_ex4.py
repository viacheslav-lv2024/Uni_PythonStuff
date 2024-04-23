import numpy as np

def moving_average_2D(arr: np.ndarray, size: int) -> np.ndarray:
    # Check if the input array is 2D
    if arr.ndim != 2:
        raise ValueError(f"apply for 2D array, not {arr.ndim}D")
    
    # Check if elements in arr are numbers
    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("Invalid data type")
    
    # Check if the window size is valid
    if size < 1 or size > min(arr.shape):
        raise ValueError("Invalid window size")

    # Calculate the shape of the output array
    output_shape = (arr.shape[0] - size + 1, arr.shape[1] - size + 1)
    
    # Initialize the output array
    result = np.zeros(output_shape, dtype=float)
    
    # Calculate moving average
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            window = arr[i:i+size, j:j+size]
            result[i, j] = np.mean(window)
    
    return result


