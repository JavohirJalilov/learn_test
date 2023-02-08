import numpy as np


class Array1D:
    def check(self, solution):
        if len(solution.shape) == 1 and solution.__class__ == np.ndarray:
            print("Accepted")
        else:
            print("Incorrect, solution is not a 1D array")
        
q0 = Array1D()