from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *


class MainGraph(Graph):
    def construct(self):
        self.vertices = [
            (0, 2, 0),
            (2, 0, 0),
            (0, -2, 0),
            (-2, 0, 0)
        ]

        self.edges = [
            (0,1),
            (1,2),
            (2,3),
            (3,0)
        ]           

        self.eclasses = [CURVE_OUT]*4

class PlanarSubgraphScene(OurGraphTheory):
    def construct(self):
        self.graph = MainGraph()
        super().construct()

        self.draw(self.vertices)
        self.draw(self.edges)
        #self.wait()

        self.trace_cycle([0,1,2,3])
        self.wait()