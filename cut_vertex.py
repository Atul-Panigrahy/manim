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
            (2, -2, 0),
            (0, 2, 0)
        ]

        self.edges = [(1,0), (2,1), (2,0), (2,3), (3,4), (2,4), (5,1), (5,2), (5,3)]

class CutVertexScene(OurGraphTheory):
    def construct(self):
        self.graph = CutVertexGraph()
        super().construct()

        f1 = TextMobject("Definition: a graph is $2$-connected if it cannot be \\\\ disconnected by removing a single vertex.")
        f1.shift(UP*3)
        f1.scale(1)
        self.play(Write(f1))
        self.wait(2)

        self.shift_graph(2*LEFT + DOWN)

        self.draw(self.vertices)
        self.draw(self.edges)

        connected = TextMobject("2-connected.")
        connected.next_to(self.edges[4], RIGHT*8)
        self.play(Write(connected))
        self.wait(3)

        self.erase([self.vertices[-1]] + self.edges[-3:])

        not_connected = TextMobject("\\emph{Not} 2-connected.", color=RED)
        not_connected.next_to(self.edges[4], RIGHT*8)
        self.play(Transform(connected, not_connected))

        self.wait(3)
    
        self.accent_vertices([self.vertices[2]])

        self.erase([self.vertices[2], self.edges[1], self.edges[2], self.edges[3], self.edges[5]])

        self.wait(2)

        anims = self.erase(self.vertices+self.edges+[connected], play=False)
        anims += [FadeOut(f1)]
        self.play(*anims)
        self.wait()