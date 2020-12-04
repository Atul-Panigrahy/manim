
from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *
from k3_3 import K33


class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Manim is fun")
        second_line = TextMobject("and useful")
        final_line = TextMobject("Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("Hope you like it too!")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)

        #Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)



class K33_Nonplanar(OurGraphTheory):
    def construct(self):
        self.graph = K33()
        super().construct()
        # 2 5
        # 1 4
        # 0 3
        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()
        a = TextMobject("a")
        # V - E + F = 2
        
        # V = 6
        self.accent_vertices()
        self.wait(1.5)

        # E = 9
        self.accent_edges()
        self.wait(1.5)

        # now we have 6 - 9 + f = 2 gives f = 5

        # no 3 edge cycles
        three_cycles = [
            [4, 1, 5, 2],
            [3, 2, 5, 1],
            [3, 0, 5, 2],
            [2, 3, 1, 4],
            [5, 0, 3, 2],
            [2, 5, 0, 3],
            [1, 5, 0, 3],
        ]
        for path in three_cycles:
            path = self.trace_path(path, run_time = 1.3)
            self.remove(*path)
            self.wait(0.5)
        self.wait()

        #thus 4f <= 2e gives f <= 3
        #gives 5 <= 3 contradiction
        
