from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *      

class CutVertexGraph(Graph):
    def construct(self):
        self.vertices = [
            (-2, -2, 1),
            (-2, 2, 0),
            (0, 0, 0),
            (2, 2, 0),
            (2, -2, 0)
        ]

        self.edges = [(1,0), (2,1), (2,0), (2,3), (3,4), (2,4)]

class CutVertexScene(OurGraphTheory):
    def construct(self):
        self.graph = CutVertexGraph()
        super().construct()

        self.shift_graph(2*LEFT)

        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()

        words = TextMobject("Not 2-connected.")
        words.next_to(self.edges[4], RIGHT*5)
    
        self.accent_vertices([self.vertices[2]])

        self.erase([self.vertices[2], self.edges[1], self.edges[2], self.edges[3], self.edges[5]])
        self.play(Write(words))
        self.wait()