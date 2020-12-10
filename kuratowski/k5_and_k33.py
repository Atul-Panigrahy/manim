
from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from kuratowski.our_discrete_graph_scene import *
from kuratowski.k3_3 import K33


class ShowBoth(OurGraphTheory):
    def construct(self):
        self.graph = CompleteGraph(5)
        for i in range(len(self.graph.vertices)):
            v = self.graph.vertices[i]
            self.graph.vertices[i] = (v[0] - 3,
                                      v[1] - 0.5,
                                      v[2])
            
        super().construct()

        f1 = TextMobject("$K_5$")
        f1.shift(UP * 3 + LEFT * 4)
        self.play(Write(f1))
        self.wait(1)
        self.draw(self.vertices)
        self.draw(self.edges)
        self.accent_vertices()
        self.wait()
        storage = self.vertices[:] + self.edges[:]
        self.graph = K33()
        for i in range(len(self.graph.vertices)):
            v = self.graph.vertices[i]
            self.graph.vertices[i] = (v[0] + 3.5,
                                      v[1] - 0.5,
                                      v[2])
            
        super().construct()

        f2 = TextMobject("$K_{3,3}$")
        f2.shift(UP * 3 + RIGHT * 4)
        self.play(Write(f2))
        self.wait(1)

        self.draw(self.vertices)
        self.draw(self.edges)
        self.accent_vertices()
        self.wait(8)
        self.play(*[
            FadeOut(v)
            for v in [f1, f2] + self.vertices + self.edges + storage
            ])
