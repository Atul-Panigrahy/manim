from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *      

class CounterExample2CGraph(Graph):
    def construct(self):
        self.vertices = [
            (0, 1, 0),
            (1, .5, 0),
            (1, -.5, 0),
            (0, -1, 0),
            (-1, -0.5, 0),
            (-1, 0.5, 0),
            (-2, 0.5, 0),
            (-2, -0.5, 0)
        ]

        self.edges = [(i, i+1) for i in range(len(self.vertices) - 1)]
        self.edges += [(5,0), (1,4), (2,5), (0,3)]

class Counter2ConnectedScene(OurGraphTheory):
    def construct(self):
        self.graph = CounterExample2CGraph()
        super().construct()

        f1 = TextMobject("Fact 1: $G$ is $2$-connected.")
        f1.shift(UP*3)
        f1.scale(1)
        self.play(Write(f1))

        self.shift_graph(2*LEFT)

        self.draw(self.vertices)
        self.draw(self.edges)

        desc1 = TextMobject("Suppose \\\\ counterexample is \\\\ not $2$-connected.", alignment="\\justify")
        desc1.scale(0.75)
        desc1.shift(RIGHT*3)
        self.play(Write(desc1, run_time=0.75))

        circle = Circle(radius=0.5, color=RED)
        circle.next_to(self.vertices[6], ORIGIN) 
        self.play(ShowCreation(circle, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(circle, run_time=0.5))

        self.erase([self.vertices[6]] + self.edges[5:7])

        desc2 = TextMobject("Smaller \\\\ counterexample.", color=RED, alignment="\\justify")
        desc2.scale(0.75)
        desc2.shift(RIGHT*3)
        self.play(Transform(desc1, desc2))

        self.wait(2)

class NoDegree2GraphCase1(Graph):
    def construct(self):
        self.vertices = [
            (.25,-.25,0),
            (-1,-1,0),
            (1,1,0),
            (-2,0,0),
            (-1,-2,0),
            (2,0,0),
            (2,1,0),
        ]

        self.edges = [
            (1,2),
            (1,3),
            (1,4),
            (2,5),
            (2,6),
            (0,1),
            (0,2)
        ]

        self.dashed = [
            (1,3),
            (1,4),
            (2,5),
            (2,6)
        ]

class NoDegree2GraphCase2(Graph):
    def construct(self):
        self.vertices = [
            (0,0,0),
            (-1,-1,0),
            (1,1,0),
            (-2,0,0),
            (-1,-2,0),
            (2,0,0),
            (2,1,0),
        ]

        self.edges = [
            (1,2),
            (1,3),
            (1,4),
            (2,5),
            (2,6),
            (0,1),
            (0,2)
        ]

        self.dashed = [
            (1,3),
            (1,4),
            (2,5),
            (2,6)
        ]

class NoDegree2Scene(OurGraphTheory):
    def construct(self):
        self.graph = NoDegree2GraphCase1()
        super().construct()
        self.shift_graph(2*LEFT)

        f1 = TextMobject("Fact 2: $\\deg{v} > 2$ for all $v \\in G$.")
        f1.shift(UP*3)
        f1.scale(1)
        self.play(Write(f1))

        f2 = TextMobject("Proof by contradiction: \\\\ assume some degree $v \\in G$ \\\\ has $\\deg{v} = 2$.")
        self.play(Write(f2))
        self.wait()
        self.play(FadeOut(f2))

        c1 = TextMobject("Case 1: $u,w$ are adjacent")
        c1.shift(DOWN*3)
        c1.scale(0.8)
        self.play(Write(c1))

        instr = TextMobject("Embed \\\\ $H = G - v$.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*4)
        self.play(Write(instr, run_time=0.75))

        self.draw(self.vertices[1:])
        self.draw(self.edges[:-2])
        v, u, w = self.vertices[0], self.vertices[1], self.vertices[2]
        v_label, u_label, w_label = (TextMobject("$v$").scale(0.5).next_to(v, DR*0.5),
                            TextMobject("$u$").scale(0.5).next_to(u, DL*0.5),
                            TextMobject("$w$").scale(0.5).next_to(w, UP*0.5))
        self.play(Write(u_label), Write(w_label))

        self.wait()

        instr2 = TextMobject("Draw $uv$, $vw$ \\\\ along $uw$", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.play(*(self.draw(self.vertices[0], play=False) + [Write(v_label)]))
        self.draw(self.edges[-2:])

        instr2 = TextMobject("Result: \\\\ an embedding \\\\ for $G$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.wait()

        erase_anims = [FadeOut(t) for t in (instr, v_label, u_label, w_label)]
        erase_anims += self.erase(self.vertices, play=False)
        erase_anims += self.erase(self.edges, play=False)

        self.play(*erase_anims)

        # CASE 2

        self.graph = NoDegree2GraphCase2()
        super().construct()
        self.shift_graph(2*LEFT)

        c2 = TextMobject("Case 2: $u,w$ are not adjacent")
        c2.shift(DOWN*3)
        c2.scale(0.8)
        self.play(Transform(c1, c2))

        instr = TextMobject("Embed \\\\ $H = G - v + uw$.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*4)
        self.play(Write(instr, run_time=0.75))

        self.draw(self.vertices[1:])
        self.draw(self.edges[:-2])
        v, u, w = self.vertices[0], self.vertices[1], self.vertices[2]
        v_label, u_label, w_label = (TextMobject("$v$").scale(0.5).next_to(v, DR*0.5),
                            TextMobject("$u$").scale(0.5).next_to(u, DL*0.5),
                            TextMobject("$w$").scale(0.5).next_to(w, UP*0.5))
        self.play(Write(u_label), Write(w_label))

        self.wait()

        instr2 = TextMobject("Remove $uw$ and \\\\ replace with $uv$, $vw$", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.erase(self.edges[0])

        self.play(*(self.draw(self.vertices[0], play=False) + [Write(v_label)]))
        self.draw(self.edges[-2:])

        instr2 = TextMobject("Result: \\\\ an embedding \\\\ for $G$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.wait(2)

class RemovableEdgeGraph(Graph):
    def construct(self):
        self.vertices = [
            (0, 1, 0),
            (1, 0, 0),
            (0, -1, 0),
            (-1, 0, 0),
            (1, 2, 0),
            (2, 1, 0),
        ]

        self.edges = [
            (0,1),
            (1,2),
            (2,3),
            (3,0),
            (3,4),
            (0,4),
            (5,4),
            (0,5),
            (1,5),
            (0,2),
            (2,5),
            (1,3)
        ]

        curve_out = lambda x,y: ArcBetweenPoints(x,y,angle=-TAU/6)
        curve_out_big = lambda x,y: ArcBetweenPoints(x,y,angle=-TAU/3)
        curve_in = lambda x,y: ArcBetweenPoints(x,y,angle=TAU/6)
        curve_in_big = lambda x,y: ArcBetweenPoints(x,y,angle=TAU/3)

        self.eclasses = [curve_out]*4 + [curve_out_big] + [curve_out] + [curve_in] + [curve_out] + [curve_in] + [Line] + [curve_in_big] + [lambda x,y: ArcBetweenPoints(x,y,angle=-TAU/1.5)]

class RemovableEdgeScene(OurGraphTheory):
    def construct(self):

        # not sure how this proof goes.

        self.graph = RemovableEdgeGraph()
        super().construct()

        f1 = TextMobject("Fact 3: for some $uv \\in G$, $G - uv$ is 2-connected.")
        f1.shift(UP*3)
        f1.scale(1)
        self.play(Write(f1))

        self.shift_graph(2*LEFT + DOWN)

        instr = TextMobject("Draw \\\\ $G$ as a cycle \\\\ with `ears'.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*4)
        self.play(Write(instr, run_time=0.75))

        self.draw(self.vertices)
        self.draw(self.edges[:4])

        self.wait()

        self.draw(self.edges[4:])

        instr2 = TextMobject("Can erase \\\\ edges on \\\\ outer paths.", alignment="\\justify")
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.erase_copy(self.edges[5])
        self.wait(0.5)
        self.draw(self.edges[5])

        self.erase_copy(self.edges[6])
        self.wait(0.5)
        self.draw(self.edges[6])