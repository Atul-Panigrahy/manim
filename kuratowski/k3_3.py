from functools import reduce
import itertools as it
import operator as op

import numpy as np

from manimlib.constants import *
from manimlib.scene.scene import Scene
from manimlib.utils.rate_functions import there_and_back
from manimlib.utils.space_ops import center_of_mass
from manimlib.once_useful_constructs.graph_theory import Graph

class K33(Graph):
    """
    2 5
    1 4
    0 3  
    """
    
    def construct(self):
        self.vertices = [
            (x, y, 0)
            for x in (-2, 2)
            for y in (-2, 0, 2)
        ]
        self.edges = [
            (a, b)
            for a in (0, 1, 2)
            for b in (3, 4, 5)
        ]
