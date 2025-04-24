import numpy as np

def max_product_composition(relation_a, relation_b):
    """
    Performs max-product composition of two fuzzy relations (matrices).
    
    The max-product composition R = A ○ B is defined as:
    R(x,z) = max_y [A(x,y) * B(y,z)]
    
    Parameters:
    relation_a (numpy.ndarray): First fuzzy relation matrix of shape (m, n)
    relation_b (numpy.ndarray): Second fuzzy relation matrix of shape (n, p)
    
    Returns:
    numpy.ndarray: Result of composition with shape (m, p)
    """
    # Validate input dimensions
    if relation_a.shape[1] != relation_b.shape[0]:
        raise ValueError(f"Matrix dimensions mismatch: {relation_a.shape} and {relation_b.shape} cannot be composed")
    
    m, n = relation_a.shape
    _, p = relation_b.shape
    
    # Initialize result matrix with zeros
    result = np.zeros((m, p))
    
    # Perform max-product composition
    for i in range(m):
        for j in range(p):
            # Calculate the product for each corresponding element
            products = np.array([relation_a[i, k] * relation_b[k, j] for k in range(n)])
            # Take the maximum value
            result[i, j] = np.max(products)
    
    return result

# Example usage
if __name__ == "__main__":
    # Get dimensions from user
    print("Enter dimensions for matrix A (m x n):")
    m = int(input("m = "))
    n = int(input("n = "))
    
    print("Enter dimensions for matrix B (n x p):")
    n_check = int(input("n = "))
    p = int(input("p = "))
    
    # Validate dimensions
    if n != n_check:
        print("Error: The number of columns in A must equal the number of rows in B.")
        exit()
    
    # Get values for matrix A
    print(f"\nEnter values for matrix A ({m}x{n}):")
    A = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            A[i, j] = float(input(f"A[{i+1},{j+1}] = "))
    
    # Get values for matrix B
    print(f"\nEnter values for matrix B ({n}x{p}):")
    B = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            B[i, j] = float(input(f"B[{i+1},{j+1}] = "))
    
    # Compute the max-product composition
    C = max_product_composition(A, B)
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nMax-Product Composition (A ○ B):")
    print(C)