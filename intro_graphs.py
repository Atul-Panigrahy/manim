from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *
    
class K33(Graph):
    def construct(self):
        self.vertices = [
            (0, 2, 0),
            (2, 1, 0),
            (2, -1, 0),
            (0, -2, 0),
            (-2, -1, 0),
            (-2, 1, 0)
        ]

        self.edges = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,0), (0,3), (1,4), (2,5)]
        self.eclasses = [Line]*7 + [lambda x,y: ArcBetweenPoints(x,y,angle=TAU/1.75)] + [DashedLine]
        self.vcolors = [WHITE, RED]*3

        
class IntroGraphScene(OurGraphTheory):
    def construct(self):
        self.graph = K33()
        super().construct()

        self.play(*(self.draw(self.edges[:-1], play=False) + self.draw(self.vertices, play=False)))
        planar = TextMobject("Planar Graph")
        planar.next_to(self.vertices[3], DOWN*2)
        self.play(Write(planar))
        self.wait(2)

        self.draw(self.edges[-1])

        nonplanar = TextMobject("Nonplanar Embedding", color=RED)
        nonplanar.next_to(self.vertices[3], DOWN*2)

        circle = Circle(radius=0.5, color=RED)
        self.play(ShowCreation(circle, run_time=0.5))
        self.play(Transform(planar, nonplanar))
        self.wait(0.5)
        self.play(FadeOut(circle, run_time=0.5))

        existence = Text("Are there any planar embeddings of this graph?", font='Consolas', size=0.5)
        #existence.scale(0.5)
        existence.next_to(nonplanar, DOWN)
        self.play(Write(existence, run_time=0.5))
        self.wait(2)
