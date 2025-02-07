import numpy as np

def solve_linear_system(coefficients, constants):
    """
    Solves a system of linear equations using Gaussian elimination with recursion.
    :param coefficients: List of lists representing the coefficient matrix (e.g., [[a11, a12], [a21, a22]])
    :param constants: List representing the constants vector (e.g., [b1, b2])
    :return: Solution vector (e.g., [x1, x2]) or error message if no solution exists
    """
    n = len(coefficients)

    # Convert inputs to NumPy arrays for easier manipulation
    A = np.array(coefficients, dtype=float)
    B = np.array(constants, dtype=float)

    def gaussian_elimination(matrix, vector, row=0):
        """Recursive Gaussian elimination."""
        if row == n:
            return vector

        # Find the pivot row
        max_row = row + np.argmax(np.abs(matrix[row:, row]))
        if matrix[max_row, row] == 0:
            raise ValueError("No unique solution exists (inconsistent or dependent system).")

        # Swap rows if necessary
        if max_row != row:
            matrix[[row, max_row]] = matrix[[max_row, row]]
            vector[[row, max_row]] = vector[[max_row, row]]

        # Eliminate below the pivot
        for i in range(row + 1, n):
            factor = matrix[i, row] / matrix[row, row]
            matrix[i] -= factor * matrix[row]
            vector[i] -= factor * vector[row]

        # Recursive call for the next row
        return gaussian_elimination(matrix, vector, row + 1)

    try:
        # Perform Gaussian elimination
        gaussian_elimination(A, B)

        # Back-substitution to find the solution
        solution = np.zeros(n)
        for i in range(n - 1, -1, -1):
            solution[i] = (B[i] - np.dot(A[i, i + 1:], solution[i + 1:])) / A[i, i]

        return solution
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    # Example usage
    coefficients = [
        [2, 1],
        [1, -1]
    ]
    constants = [4, 1]

    result = solve_linear_system(coefficients, constants)
    print("Solution:", result)