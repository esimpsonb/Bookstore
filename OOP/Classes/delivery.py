import numpy as np
from Algorithms.tsp import TSP


class Delivery_Boy():
    
    def __init__(self):
        pass
    
    def tsp(self,addresses):
        tsp_solver = TSP()
        solution = tsp_solver.solve(addresses)
        return solution


        