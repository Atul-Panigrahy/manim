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
            (0,3),
            # reverse of complete path vu (28)
            (3,0),
            # vivj drawn inside C
            (2,4)
        ]           

        self.eclasses = [CURVE_OUT]*6 + [CURVE_OUT_HUGE_RED] + [CURVE_OUT_HUGE]*2 + [CURVE_OUT_HUGE] + [Line]*17 + [CURVE_OUT] + [CURVE_OUT] + [Line]

class MainProofScene(OurGraphTheory):
    def construct(self):
        self.graph = MainGraph()
        super().construct()

        self.shift_graph(3*LEFT)

        self.wait(4)

        f1 = TextMobject("Take the edge $uv$ from the previous statement, \\\\ and consider the graph $G - uv$ obtained by removing it.")
        f1.scale(1).shift(UP*2)
        self.play(Write(f1))

        self.wait(3)

        f2 = TextMobject("$G - uv$ is planar by minimality.")
        f2.scale(1).next_to(f1, DOWN*3)
        self.play(Write(f2))

        self.wait(3)

        f3 = TextMobject("$G - uv$ is 2-connected, \\\\ so there is a cycle containing $u,v$.")
        f3.scale(1).next_to(f2, DOWN*3)
        self.play(Write(f3))

        self.wait(3)

        self.play(*[FadeOut(e) for e in [f1,f2,f3]])

        self.wait()


        u,v = self.vertices[0], self.vertices[3]

        self.draw([u,v])
        v_label, u_label = (TextMobject("$v$").scale(0.8).next_to(v, RIGHT*0.5),
                            TextMobject("$u$").scale(0.8 ).next_to(u, LEFT*0.5))
        self.play(Write(u_label), Write(v_label))

        instr = TextMobject("Embed maximal cycle $C$ \\\\ containing $u, v$.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*3.5)
        self.play(Write(instr, run_time=0.75))

        self.wait(4)

        self.draw(self.edges[:6])
        self.draw(self.edges[-3:-1])
        cycle = self.trace_arc_cycle_with_edges([self.edges[i] for i in [0,1,2,28]])
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        cycle = self.trace_arc_cycle_with_edges([self.edges[i] for i in [27,28]])
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        cycle = self.trace_arc_cycle_with_edges(self.edges[:6], color=GREEN)
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        self.erase_copy(self.edges[-3:-1])

        C_label = TextMobject("$C$").scale(0.8).next_to(self.edges[1], DOWN*.3)
        self.play(Write(C_label))

        self.wait(9)

        instr2 = TextMobject("Loop along upper \\\\ part of $C$?", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw upper vertices and the edge
        upper_vertices = [1,2,6,7]
        self.draw([self.vertices[i] for i in upper_vertices])
        self.draw(self.edges[7])

        instr2 = TextMobject("Contradiction: \\\\ larger cycle.", alignment="\\justify", color=RED)
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # trace bad cycle
        cycle = self.trace_cycle([0,1,6,7,2,3,4,5])
        self.wait(0.5)

        # fadeout upper vertices and the edge
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        anims = self.erase_copy(self.edges[7], play=False)
        anims += self.erase_copy([self.vertices[i] for i in upper_vertices], play=False)
        self.play(*anims)

        instr2 = TextMobject("Loop along lower \\\\ part of $C$?", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw lower vertices and the edge
        lower_vertices = [4,5,8,9]
        self.draw([self.vertices[i] for i in lower_vertices])
        self.draw(self.edges[9])

        instr2 = TextMobject("Contradiction: \\\\ larger cycle.", alignment="\\justify", color=RED)
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # trace bad cycle
        cycle = self.trace_cycle([0,1,2,3,4,8,9,5])
        self.wait(1.5)

        # fadeout lower vertices and the edge
        self.play(*[FadeOut(c, run_time=0.5) for c in cycle])
        anims = self.erase_copy(self.edges[9], play=False)
        anims += self.erase_copy([self.vertices[i] for i in lower_vertices], play=False)
        self.play(*anims)
        self.wait(1)

        instr2 = TextMobject("$G$ is nonplanar, \\\\ so we need an \\\\ obstruction to $uv$ \\\\ on the outside of $C$." , alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw bad uv edge
        self.draw(self.edges[6])

        self.wait(6)

        instr2 = TextMobject("There must exist \\\\ a path $v_i v_j$ \\\\ that blocks $uv$.", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        p_vertices = [2,7,4,8]
        vi, vj = self.vertices[2], self.vertices[4]
        self.draw([self.vertices[i] for i in p_vertices])
        vi_label, vj_label = (TextMobject("$v_i$").scale(0.8).next_to(vi, UP*0.5),
                            TextMobject("$v_j$").scale(0.8 ).next_to(vj, DOWN*0.5))
        self.play(Write(vi_label), Write(vj_label))
        self.draw(self.edges[8])
        self.erase_copy(self.edges[6])

        self.wait(8)

        # ---------------- OBSTRUCTIONS ------------------------------------------

        instr2 = TextMobject("The inside of $C$ must \\\\ contain an obstruction \\\\ to $uv$ and to $v_i v_j$.", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        self.wait(18)

        instr2 = TextMobject("Obstructions", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        self.wait(4)

        instr2 = TextMobject("Obstruction 1:", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw obs1 vertices and edges
        obstruction_vertices = [13,15]
        obstruction_edges = range(14,15)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        self.wait(2)
        self.draw(self.edges[27])
        self.wait(4)

        k33 = TextMobject("$G$ contains $K_{3,3}$.", alignment="\\justify", color=RED)
        k33.scale(0.75)
        k33.next_to(instr, DOWN)
        self.play(Write(k33))

        # highlight K33
        red_verts = [13,3,8]
        green_verts = [0,7,15]
        colors = [RED]*3 + [GREEN]*3
        self.accent_vertices([self.vertices[i] for i in red_verts + green_verts], colors=colors, run_time=3)

        self.wait(3)

        # fadeout obs1 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        anims += [FadeOut(k33)]
        self.play(*anims)

        self.wait()

        instr2 = TextMobject("Obstruction 2:", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw obs2 vertices and edges
        obstruction_vertices = [12,14,15]
        obstruction_edges = range(15,18)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        self.play(Write(k33))

        # highlight K33
        self.draw(self.edges[27])
        red_verts = [12,8,3]
        green_verts = [0,14,15]
        self.accent_vertices([self.vertices[i] for i in red_verts + green_verts], colors=colors, run_time=3)

        # fadeout obs2 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        anims += [FadeOut(k33)]
        self.play(*anims)

        instr2 = TextMobject("Obstruction 3:", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw obs3 vertices and edges
        obstruction_vertices = [10,11]
        obstruction_edges = range(18,23)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        self.play(Write(k33))

        # highlight K33
        self.draw(self.edges[27])
        red_verts = [0,11,8]
        green_verts = [10,7,3]
        self.accent_vertices([self.vertices[i] for i in red_verts + green_verts], colors=colors, run_time=3)

        # fadeout obs3 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        anims += [FadeOut(k33)]
        self.play(*anims)

        instr2 = TextMobject("Obstruction 4:", alignment="\\justify")
        instr2.scale(0.8)
        instr2.shift(RIGHT*3.5)
        self.play(Transform(instr, instr2))

        # draw obs4 vertices and edges
        obstruction_vertices = [12]
        obstruction_edges = range(23,27)
        self.draw([self.vertices[i] for i in obstruction_vertices])
        self.draw([self.edges[i] for i in obstruction_edges])

        k5 = TextMobject("$G$ contains $K_{5}$.", alignment="\\justify", color=RED)
        k5.scale(0.75)
        k5.next_to(instr, DOWN)
        self.play(Write(k5))

        # highlight K33
        self.draw(self.edges[27])

        self.wait(1)

        # fadeout obs4 vertices and edges
        anims = self.erase_copy([self.edges[i] for i in obstruction_edges], play=False)
        anims += self.erase_copy([self.vertices[i] for i in obstruction_vertices], play=False)
        anims += self.erase_copy(self.edges[27], play=False)
        anims += [FadeOut(k5)]
        self.play(*anims)
        self.wait(1)

        erase_anims = []
        erase_anims += self.erase(op.itemgetter(0,1,2,3,4,5,8)(self.edges), play=False)
        erase_anims += self.erase(op.itemgetter(0,2,3,4,7,8)(self.vertices), play=False)
        erase_anims += [FadeOut(e) for e in [instr, vi_label, vj_label, C_label, u_label, v_label]]
        self.play(*erase_anims)

        f1 = TextMobject("Result: $G$ always contains a subgraph \\\\ which is a subdivision of $K_5$ or $K_{3,3}$.")
        f1.scale(1).shift(UP*2)
        self.play(Write(f1))

        self.wait(3)

        f2 = TextMobject("Contradiction! We assumed that this was not the case.")
        f2.scale(1).next_to(f1, DOWN*3)
        self.play(Write(f2))

        self.wait(5)

        self.play(*[FadeOut(e) for e in [f1,f2]])

        self.wait(2)

class KuratowskiResultScene(Scene):
    def construct(self):
        super().construct()

        self.wait(3)

        f1 = TextMobject("Kuratowski's Theorem: \\\\ A graph is nonplanar $\\Longleftrightarrow$ it has a subgraph \\\\ which is a subdivision of $K_5$ or $K_{3,3}$")
        f1.shift(UP*2.5)
        f1.scale(1)
        self.play(Write(f1))

        f2 = TextMobject("This allows us to describe \\emph{exactly} which graphs \\\\ can and cannot be embedded in the plane!")
        f2.scale(1).next_to(f1, DOWN*4)
        self.play(Write(f2))

        self.wait(4)

        f3 = TextMobject("Which graphs can be embedded into \\\\ other topological spaces?")
        f3.scale(1).next_to(f2, DOWN*4)
        self.play(Write(f3))

        self.wait(14)

        self.play(*[FadeOut(e) for e in [f1,f2,f3]])

        self.wait(1)