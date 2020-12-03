from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *



class TwoConnectedLemmaBase(Graph):
    def construct(self):

        u = (-2, 0, 0)
        v = (2, 0, 0)

        self.vertices = [u,v]
        
        upper_arc = [u]
        for i in range(4):
            angle = (PI/5)*(4-i)
            upper_arc.append((2*np.cos(angle), 2*np.sin(angle), 0))
        upper_arc.append(v)

        self.vertices = upper_arc 

        self.edges = [(0,5)] + [(i,i+1) for i in range(5)]

        self.dashed = [(2,3)]


class TwoConnectedLemma(OurGraphTheory):

    def construct(self):
        self.graph = TwoConnectedLemmaBase()
        super().construct()
        
        u, v = self.vertices[0], self.vertices[5]
        u_label, v_label = (TextMobject("$u$").next_to(u, DL),
                            TextMobject("$v$").next_to(v, DR))
        self.play(Write(u_label), Write(v_label), *self.draw([u,v], play=False))
        #self.wait(2)


        self.draw([self.edges[0]])
        #self.wait()
        self.erase_copy([self.edges[0]], run_time=0.2)

        path_v = self.draw(self.vertices[1:-1], play=False, run_time=1)
        path_e = self.draw(self.edges[1:], play=False, run_time=1/3)
        self.play(
            AnimationGroup(
                AnimationGroup(*path_v, lag_ratio=0.2),
                AnimationGroup(*path_e, lag_ratio=0.8),
                lag_ratio=0.5)
        )
        #self.wait()

        self.draw(self.edges[0], reverse=True)
        #self.wait()

        self.trace_cycle([0,1,2,3,4,5,0], run_time=1)
        self.wait()
    


