import numpy as np

def max_min_composition(R,S):
    if R.shape[1] != S.shape[0]:
        raise ValueError("Number of columns in R must be equal to number of rows in S")
    
    m,n= R.shape
    _,p= S.shape
    T= np.zeros((m,p))
    for i in range(m):
        for k in range(p):
            T[i,k]=max(min(R[i,j],S[j,k]) for j in range(n))
    return T
# user input

def get_user_matrix(name):
    print(f"Enter {name} matrix dimensions:")
    rows = int(input(f"Number of rows for {name}: "))
    cols = int(input(f"Number of columns for {name}: "))
    
    print(f"Enter {name} matrix elements row by row:")
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        row_values = input(f"Enter {cols} values for row {i+1} (separated by spaces): ")
        values = list(map(float, row_values.split()))
        if len(values) != cols:
            raise ValueError(f"Expected {cols} values, got {len(values)}")
        matrix[i] = values
    
    return matrix

try:
    R = get_user_matrix("R")
    S = get_user_matrix("S")
    
    # Check if matrices can be composed
    if R.shape[1] != S.shape[0]:
        print(f"Error: Cannot compose matrices with shapes {R.shape} and {S.shape}")
    else:
        T = max_min_composition(R, S)
        print("\nResult of max-min composition:")
        print(T)
except ValueError as e:
    print(f"Error: {e}")


