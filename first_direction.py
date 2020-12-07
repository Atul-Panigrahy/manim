from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *


class FirstDirection(Scene):
    def construct(self):

        t1 = TextMobject("The first direction of Kuratowski's theorem states:").to_edge(UP)
        LHS = TextMobject("$G$ contains a subdivision of $K_5$ or $K_{3,3}$").shift(UP)
        down_imply = TextMobject("$\\Leftarrow$").rotate_in_place(PI/2).next_to(LHS,DOWN)
        RHS = TextMobject("$G$ is non-planar").next_to(down_imply,DOWN)
        self.wait(2)
        self.play(Write(t1))
        self.play(Write(LHS))
        self.play(Write(down_imply))
        self.play(Write(RHS))
        self.wait(2.5)
        self.play(*[
            FadeOut(v) for v in [t1, LHS, down_imply, RHS]])
        prelim = BulletedList(
            "Subdivision of Nonplanar is Nonplanar",
            "If a Subgraph is Nonplanar then the Graph is Nonplanar",
        ).shift(UP * 2.5)
        self.play(Write(prelim))
        self.wait(10.5)
        self.play(*[
            FadeOut(t)
            for t in [prelim]
            ])


