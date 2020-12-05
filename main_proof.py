from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *


class MainGraph(Graph):
    def construct(self):
        self.vertices = [
            # main cycle
            (-2, 0, 0),
            (-1, 1.5, 0),
            (1, 1.5, 0),
            (2, 0, 0),
            (1, -1.5, 0),
            (-1, -1.5, 0),
            # hacky extras
            (-1, 1.5, 0),
            (1, 1.5, 0),
            (1, -1.5, 0),
            (-1, -1.5, 0),
            # inner 
            (-1, 0, 0),
            (1, 0, 0),
            (0, 0, 0),
            # obstructions
            (-1.5, 1.15, 0),
            (1.5, 1.15, 0),
            (1.5, -1.15, 0)
        ]

        self.edges = [
            # inner loop (0:6)
            (0,1),
            (1,2),
            (2,3),
            (3,4),
            (4,5),
            (5,0),
            # outer loops (6:10)
            (0,3),
            (6,7),
            (7,8),
            (8,9),
            # hacky lines (10:14)
            (1,6),
            (2,7),
            (4,8),
            (5,9),
            # obstruction 1 (14), with vertices 13,15
            (13, 15),
            # obstruction 2 (15:18), with vertices 12,14,15
            (0, 12),
            (12, 14),
            (12, 15),
            # obstruction 3 (18:23), with vertices 10,11
            (0, 10),
            (10, 11),
            (11, 3),
            (11, 2),
            (10, 4),
            # obstruction 4 (23:), with vertex 12
            (12, 0),
            (12, 3),
            (12, 2),
            (12, 4),
            #
        ]           

        self.eclasses = [CURVE_OUT]*6 + [CURVE_OUT_HUGE_RED] + [CURVE_OUT_HUGE]*2 + [CURVE_OUT_HUGE] + [Line]*17

class MainProofScene(OurGraphTheory):
    def construct(self):
        self.graph = MainGraph()
        super().construct()

        self.shift_graph(3*LEFT)

        u,v = self.vertices[0], self.vertices[3]

        self.draw([u,v])
        v_label, u_label = (TextMobject("$v$").scale(0.8).next_to(v, RIGHT*0.5),
                            TextMobject("$u$").scale(0.8 ).next_to(u, LEFT*0.5))
        self.play(Write(u_label), Write(v_label))
        self.draw(self.edges[:6])
        #self.wait()

        self.wait()

        # draw upper vertices and the edge
        upper_vertices = [1,2,6,7]
        self.draw([self.vertices[i] for i in upper_vertices])
        self.draw(self.edges[7])

        # trace bad cycle
        cycle = self.trace_cycle([0,1,6,7,2,3,4,5])
        self.wait(0.5)

        # fadeout upper vertices and the edge
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        anims = self.erase_copy(self.edges[7], play=False)
        anims += self.erase_copy([self.vertices[i] for i in upper_vertices], play=False)
        self.play(*anims)
        self.wait()

        # draw lower vertices and the edge
        lower_vertices = [4,5,8,9]
        self.draw([self.vertices[i] for i in lower_vertices])
        self.draw(self.edges[9])

        # trace bad cycle
        cycle = self.trace_cycle([0,1,2,3,4,8,9,5])
        self.wait(0.5)

        # fadeout lower vertices and the edge
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        anims = self.erase_copy(self.edges[9], play=False)
        anims += self.erase_copy([self.vertices[i] for i in lower_vertices], play=False)
        self.play(*anims)
        self.wait()

        # draw bad uv edge
        self.draw(self.edges[6])

        p_vertices = [2,7,4,8]
        vi, vj = self.vertices[2], self.vertices[4]
        self.draw([self.vertices[i] for i in p_vertices])
        vi_label, vj_label = (TextMobject("$v_i$").scale(0.8).next_to(vi, UP*0.5),
                            TextMobject("$v_j$").scale(0.8 ).next_to(vj, DOWN*0.5))
        self.play(Write(vi_label), Write(vj_label))
        self.draw(self.edges[8])
        self.erase_copy(self.edges[6])

        self.wait(2)

        # ---------------- OBSTRUCTIONS ------------------------------------------

        # draw obs1 vertices and edges
        obstruction_vertices = [13,15]
        obstruction_edges = range(14,15)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # fadeout obs1 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        self.play(*anims)
        self.wait()

        # draw obs2 vertices and edges
        obstruction_vertices = [12,14,15]
        obstruction_edges = range(15,18)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # fadeout obs2 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        self.play(*anims)
        self.wait()

        # draw obs3 vertices and edges
        obstruction_vertices = [10,11]
        obstruction_edges = range(18,23)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # fadeout obs3 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        self.play(*anims)
        self.wait()

        # draw obs4 vertices and edges
        obstruction_vertices = [12]
        obstruction_edges = range(23,27)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # fadeout obs4 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        self.play(*anims)
        self.wait()

