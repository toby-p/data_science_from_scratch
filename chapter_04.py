#!/usr/bin/env/ python
import math

def vector_add(vector1, vector2):
    """Adds corresponding elements."""
    return [v_i + w_i for v_i, w_i in zip(vector1, vector2)]

def vector_subtract(vector1, vector2):
    """Subtracts corresponding elements."""
    return [v_i - w_i for v_i, w_i in zip(vector1, vector2)]

def vector_sum(vectors):
    """Sums all corresponding elements."""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def scalar_multiply(scalar, vector):
    return [scalar * v_i for v_i in vector]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """ v_1 * w_1 + ...... + v_n * w_n """
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(vector):
    """v_1 * v_1 + ...... v_n * v_n """
    return dot(vector, vector)

def vector_length(vector):
    return math.sqrt(sum_of_squares(vector))

def squared_distance(vector1, vector2):
    return sum_of_squares(vector_subtract(vector1, vector2))

def distance(vector1, vector2):
    return math.sqrt(squared_distance(vector1, vector2))

def shape(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    return num_rows, num_cols

def get_row(matrix, row):
    return matrix[row]

def get_column(matrix, col):
    return [row[col] for row in matrix]

def make_matrix(num_rows, num_cols, entry_fn):
    """Returns a num_rows by num_cols matrix 
    whose (i, j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)
            for j in range(num_cols)]
           for i in range(num_rows)]

# Function to create an identity matrix
def is_diagonal(i, j):
    """1s on diagonal, 0s elsewhere"""
    return 1 if i == j else 0