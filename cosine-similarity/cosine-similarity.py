import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dotProduct = 0.0
    normA = 0.0
    normB = 0.0
    for i in range(len(a)):
        dotProduct += a[i] * b[i]
        normA += a[i] * a[i]
        normB += b[i] * b[i]
    normA = normA ** 0.5
    normB = normB ** 0.5
    if normA == 0 or normB == 0:
        return 0.0
    return dotProduct / (normA * normB)