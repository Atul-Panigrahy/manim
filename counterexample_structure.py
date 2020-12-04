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

        self.shift_graph(2*LEFT)

        self.draw(self.vertices)
        self.draw(self.edges)

        desc1 = TextMobject("Counterexample \\\\ is not \\\\ $2$-connected.", alignment="\\justify")
        desc1.scale(0.75)
        desc1.shift(RIGHT*3)
        self.play(Write(desc1, run_time=0.75))

        circle = Circle(radius=0.5, color=RED)
        circle.next_to(self.vertices[6], ORIGIN) 
        self.play(ShowCreation(circle, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(circle, run_time=0.5))

        self.erase([self.vertices[6]] + self.edges[5:7])

        desc2 = TextMobject("Smaller \\\\ counterexample.", alignment="\\justify")
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

class NoDegree2Case1Scene(OurGraphTheory):
    def construct(self):
        self.graph = NoDegree2GraphCase1()
        super().construct()

        base_case = TextMobject("Case 1: $u,w$ are adjacent")
        base_case.shift(UP*3)
        base_case.scale(0.8)
        self.play(Write(base_case))

        self.shift_graph(2*LEFT)

        self.draw(self.vertices[1:])
        self.draw(self.edges[:-2])
        v, u, w = self.vertices[0], self.vertices[1], self.vertices[2]
        v_label, u_label, w_label = (TextMobject("$v$").scale(0.5).next_to(v, DR*0.5),
                            TextMobject("$u$").scale(0.5).next_to(u, DL*0.5),
                            TextMobject("$w$").scale(0.5).next_to(w, UP*0.5))
        self.play(Write(u_label), Write(w_label))

        instr = TextMobject("Embed \\\\ $H = G - v$.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*4)
        self.play(Write(instr, run_time=0.75))

        self.wait(2)

        self.play(*(self.draw(self.vertices[0], play=False) + [Write(v_label)]))
        self.draw(self.edges[-2:])

        instr2 = TextMobject("Result: \\\\ an embedding \\\\ for $G$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.wait(2)

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

class NoDegree2Case2Scene(OurGraphTheory):
    def construct(self):
        self.graph = NoDegree2GraphCase2()
        super().construct()

        base_case = TextMobject("Case 2: $u,w$ are not adjacent")
        base_case.shift(UP*3)
        base_case.scale(0.8)
        self.play(Write(base_case))

        self.shift_graph(2*LEFT)

        self.draw(self.vertices[1:])
        self.draw(self.edges[:-2])
        v, u, w = self.vertices[0], self.vertices[1], self.vertices[2]
        v_label, u_label, w_label = (TextMobject("$v$").scale(0.5).next_to(v, DR*0.5),
                            TextMobject("$u$").scale(0.5).next_to(u, DL*0.5),
                            TextMobject("$w$").scale(0.5).next_to(w, UP*0.5))
        self.play(Write(u_label), Write(w_label))

        instr = TextMobject("Embed \\\\ $H = G - v + uw$.", alignment="\\justify")
        instr.scale(0.75)
        instr.shift(RIGHT*4)
        self.play(Write(instr, run_time=0.75))

        self.wait(2)

        self.erase(self.edges[0])

        self.play(*(self.draw(self.vertices[0], play=False) + [Write(v_label)]))
        self.draw(self.edges[-2:])

        instr2 = TextMobject("Result: \\\\ an embedding \\\\ for $G$", alignment="\\justify", color=RED)
        instr2.scale(0.75)
        instr2.shift(RIGHT*4)
        self.play(Transform(instr, instr2))

        self.wait(2)


class NoDegree2Scene(OurGraphTheory):
    def construct(self):
        self.graph = NoDegree2GraphCase1()
        super().construct()
        self.shift_graph(2*LEFT)

        c1 = TextMobject("Case 1: $u,w$ are adjacent")
        c1.shift(UP*3)
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
        c2.shift(UP*3)
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

class RemovableEdgeScene(OurGraphTheory):
    def construct(self):

        # not sure how this proof goes.

        self.graph = RemovableEdgeGraph()
        super().construct()

        self.shift_graph(2*LEFT)

        self.draw(self.vertices)
        self.draw(self.edges)