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
        self.vcolors = [RED, BLUE]*3

        
class IntroGraphScene(OurGraphTheory):
    def construct(self):
        self.graph = K33()
        super().construct()
        self.wait(2)

        self.shift_graph(DOWN + LEFT*2)

        take_k4 = TextMobject("A graph is planar if some embedding of it \\\\ onto the plane has no edge intersections.")
        take_k4.shift(UP*3)
        self.play(Write(take_k4))

        self.wait(2)

        self.play(*(self.draw(self.edges[:-1], play=False) + self.draw(self.vertices, play=False)))
        planar = TextMobject("Planar Graph", alignment="\\justify")
        planar.shift(RIGHT*3)
        self.play(Write(planar))
        self.wait(3)

        self.draw(self.edges[-1])

        nonplanar = TextMobject("Nonplanar \\\\ Embedding", color=RED, alignment="\\justify")
        nonplanar.shift(RIGHT*3)


        circle = Circle(radius=0.5, color=RED).next_to(self.edges[-1], ORIGIN)
        self.play(ShowCreation(circle, run_time=0.5))
        self.play(Transform(planar, nonplanar))
        self.wait(2)
        self.play(FadeOut(circle, run_time=0.5))
        self.wait(2)

        existence = TextMobject("Are there any planar \\\\ embeddings of this graph?", alignment="\\justify")
        existence.scale(0.5)
        existence.next_to(nonplanar, DOWN)
        existence.shift(RIGHT*0.25)
        self.play(Write(existence, run_time=0.5))
        self.wait(2)

        erase_anims = self.erase(self.vertices, play=False)
        erase_anims += self.erase(self.edges, play=False)
        erase_anims += [FadeOut(existence), FadeOut(planar), FadeOut(take_k4)]
        
        self.play(*erase_anims)
        self.wait()
