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
            # obstruction 4 (23:26), with vertex 12
            (12, 0),
            (12, 3),
            (12, 2),
            (12, 4),
            # complete path uv (27)
            (0,3)
        ]           

        self.eclasses = [CURVE_OUT]*6 + [CURVE_OUT_HUGE_RED] + [CURVE_OUT_HUGE]*2 + [CURVE_OUT_HUGE] + [Line]*17 + [CURVE_OUT]

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

        instr = TextMobject("Embed cycle $C$ \\\\ containing $u, v$.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*4)
        self.play(Write(instr, run_time=0.75))

        self.draw(self.edges[:6])
        #self.wait()

        self.wait()

        instr2 = TextMobject("Loop along upper \\\\ part of C?", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw upper vertices and the edge
        upper_vertices = [1,2,6,7]
        self.draw([self.vertices[i] for i in upper_vertices])
        self.draw(self.edges[7])

        instr2 = TextMobject("Contradiction: \\\\ larger cycle.", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # trace bad cycle
        cycle = self.trace_cycle([0,1,6,7,2,3,4,5])
        self.wait(0.5)

        # fadeout upper vertices and the edge
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        anims = self.erase_copy(self.edges[7], play=False)
        anims += self.erase_copy([self.vertices[i] for i in upper_vertices], play=False)
        self.play(*anims)
        self.wait()

        instr2 = TextMobject("Loop along lower \\\\ part of C?", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw lower vertices and the edge
        lower_vertices = [4,5,8,9]
        self.draw([self.vertices[i] for i in lower_vertices])
        self.draw(self.edges[9])

        instr2 = TextMobject("Contradiction: \\\\ larger cycle.", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # trace bad cycle
        cycle = self.trace_cycle([0,1,2,3,4,8,9,5])
        self.wait(0.5)

        # fadeout lower vertices and the edge
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        anims = self.erase_copy(self.edges[9], play=False)
        anims += self.erase_copy([self.vertices[i] for i in lower_vertices], play=False)
        self.play(*anims)
        self.wait()

        instr2 = TextMobject("Need obstruction \\\\ to $uv$ on outside", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw bad uv edge
        self.draw(self.edges[6])

        instr2 = TextMobject("There must exist \\\\ a path $v_i v_j$", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

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

        instr2 = TextMobject("Obstruction 1: \\\\ contains $K_{3,3}$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw obs1 vertices and edges
        obstruction_vertices = [13,15]
        obstruction_edges = range(14,15)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # highlight K33
        self.draw(self.edges[27])
        red_verts = [13,3,8]
        green_verts = [0,7,15]
        colors = [RED]*3 + [GREEN]*3
        self.accent_vertices([self.vertices[i] for i in red_verts + green_verts], colors=colors, run_time=2)

        # fadeout obs1 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        self.play(*anims)
        self.wait()

        instr2 = TextMobject("Obstruction 2: \\\\ contains $K_{3,3}$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw obs2 vertices and edges
        obstruction_vertices = [12,14,15]
        obstruction_edges = range(15,18)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # highlight K33
        self.draw(self.edges[27])
        red_verts = [12,8,3]
        green_verts = [0,14,15]
        self.accent_vertices([self.vertices[i] for i in red_verts + green_verts], colors=colors, run_time=2)

        # fadeout obs2 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        self.play(*anims)
        self.wait()

        instr2 = TextMobject("Obstruction 3: \\\\ contains $K_{3,3}$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw obs3 vertices and edges
        obstruction_vertices = [10,11]
        obstruction_edges = range(18,23)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # highlight K33
        self.draw(self.edges[27])
        red_verts = [0,11,8]
        green_verts = [10,7,3]
        self.accent_vertices([self.vertices[i] for i in red_verts + green_verts], colors=colors, run_time=2)

        # fadeout obs3 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        self.play(*anims)
        self.wait()

        instr2 = TextMobject("Obstruction 4: \\\\ contains $K_5$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        # draw obs4 vertices and edges
        obstruction_vertices = [12]
        obstruction_edges = range(23,27)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        # highlight K33
        self.draw(self.edges[27])

        # fadeout obs4 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        self.play(*anims)
        self.wait()