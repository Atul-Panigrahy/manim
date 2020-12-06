from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *

class ForwardGraph(Graph):
    def construct(self):
        self.vertices = [
            (0,0,0),
            (1,2,0),
            (2,1,0),
            (2,-1,0),
            (1,-2,0),
            (-1,-2,0),
            (-2,-1,0),
            (-2,1,0),
            (-1,2,0),
        ]

        self.edges = [
            (0,1),
            (0,3),
            (6,0),
            (1,2),
            (2,3),
            (4,3),
            (4,5),
            (6,5),
            (6,7),
            (7,8),
            (8,1),
            (2,7),
            (4,7),
            (2,5)
        ]

class K33TargetGraph(Graph):
    """
    2 5
    1 4
    0 3  
    """
    
    def construct(self):
        self.vertices = [
            (-1,1,0),
            (-1,0,0),
            (-1,-1,0),
            (1,1,0),
            (1,0,0),
            (1,-1,0),
            (0,-1,0),
        ]
        self.edges = [
            (0,3),
            (0,4),
            (0,5),
            (1,3),
            (1,4),
            (1,5),
            (2,3),
            (2,4),
            (2,6),
            (6,5)
        ]

class K33TargetScene(OurGraphTheory):
    def construct(self):
        self.graph = K33TargetGraph()
        super().construct()
        self.shift_graph(RIGHT*4)

class KuratowskiStatementForwardScene(OurGraphTheory):
    def construct(self):
        self.graph = ForwardGraph()
        super().construct()

        self.shift_graph(LEFT*4)

        self.play(*(self.draw(self.vertices, play=False) + self.draw(self.edges, play=False)))
        self.wait()

        blue_verts = [2,6,4]
        green_verts = [3,5,7]

        for v in blue_verts:
            self.vertices[v].set_color(BLUE)

        for v in green_verts:
            self.vertices[v].set_color(GREEN)

        self.play(*[Transform(self.vertices[i], self.vertices[i]) for i in blue_verts + green_verts])

        self.wait()

        self.wait(2)

        old_verts = [self.vertices[i] for i in blue_verts + green_verts + [0]]
        old_edges = [self.edges[i] for i in [4,13,11,2,1,7,8,5,6,12]]

        remove_edges = [self.edges[i] for i in [0,3,9,10]]
        remove_verts = [self.vertices[i] for i in [1,8]]  

        self.erase(remove_edges + remove_verts)

        new_graph_scene = K33TargetScene()

        v_transforms = [Transform(v1,v2) for (v1, v2) in zip(old_verts, new_graph_scene.vertices)]
        e_transforms = [Transform(e1,e2) for (e1, e2) in zip(old_edges, new_graph_scene.edges)]

        self.play(*(v_transforms + e_transforms))

        self.wait()
