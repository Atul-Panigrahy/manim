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
        
        self.add(t1, LHS, down_imply, RHS)
        self.wait(3)