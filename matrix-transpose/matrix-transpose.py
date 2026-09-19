import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    n = len(A)
    m = len(A[0])
    transposed = np.zeros((m, n), dtype=type(A[0][0]))
    for i in range(n):
        for j in range(m):
            transposed[j][i] = A[i][j]
    return transposed