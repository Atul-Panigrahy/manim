
from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from kuratowski.our_discrete_graph_scene import *
from kuratowski.k3_3 import K33

def edge_to_two_edges(edge):
    start, end = edge.get_start_and_end()
    mid = (start + end) / 2
    return [
        Line(start, mid),
        Line(end, mid)
    ]

INSTANT = 0.000001

c1 = 2*np.cos(2*PI / 5)
c2 = 2*np.cos(PI / 5)
s1 = 2*np.sin(2*PI / 5)
s2 = 2*np.sin(4*PI / 5)

class K5ForTorus(Graph):
    """
    2 5
    1 4
    0 3  
    """

    def construct(self):
        self.vertices = [
            (0,2,0),
            (s1,c1,0),
            (s2,-1*c2,0),
            (-1*s2,-1*c2,0),
            (-1*s1,c1,0)
        ]
        self.edges = [
            (a, b)
            for a in range(5)
            for b in range(a+1,5)
        ]

class K5OnTorus(OurGraphTheory):
    def construct(self):
        self.graph = K5ForTorus()
        super().construct()

        f2 = TextMobject("So can $K_{5}$!")
        self.play(Write(f2))
        self.wait(1)
        self.play(FadeOut(f2))

        # 2 5
        # 1 4
        # 0 3
        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()

        torus_creation_time = 1.5
        
        l1 = Line((-3, 0, 0), (-3, 3, 0), color=PINK)
        l2 = Line((-3, 0, 0), (-3,-3, 0), color=PINK)
        l3 = Line((-3, 3, 0), (3, 3, 0), color=PINK)
        l4 = Line((-3,-3, 0), (3,-3, 0), color=PINK)
        l5 = Line((3, 3, 0), (3, 0, 0), color=PINK)
        l6 = Line((3,-3, 0), (3, 0, 0), color=PINK)

        self.play(*[
            ShowCreation(l1),
            ShowCreation(l2)
            ], run_time = torus_creation_time / 6)
        self.play(*[
            ShowCreation(l3),
            ShowCreation(l4)
            ], run_time = 2 * torus_creation_time / 6)
        self.play(*[
            ShowCreation(l5),
            ShowCreation(l6)
            ], run_time = torus_creation_time / 6)
        arrows = [ArrowTip() for x in range(4)]
        [arr.set_color(PINK) for arr in arrows]
        
        for i in range(3):
            for arr, shift in zip(arrows,
                                [UP, DOWN, LEFT, RIGHT]):
                arr.shift(shift)

        [arrows[i].rotate(PI / 2) for i in [2, 3]]
        [arrow.shift(0.25 * RIGHT) for arrow in arrows]

        self.play(*[
            Write(arrow) for arrow in arrows
            ], run_time = 2 * torus_creation_time / 6)

        def replace_edge_with_two(e):
            e1, e2 = edge_to_two_edges(self.edges[e])
            self.draw(e1, run_time = INSTANT)
            self.draw(e2, run_time = INSTANT)
            self.remove(self.edges[e])
            return [e1, e2]
            
        """
        straight_across = [6]

        replacements = [
            replace_edge_with_two(e)
            for e in straight_across
        ]
        """

        def horizontal_new_line(line, color=WHITE):
            start = line.start.copy()
            end = line.end.copy()
            if start[0] < 0:
                end[0] = -3
            else:
                end[0] = 3
            return Line(start, end, color=color)

        """
        self.play(*[
            Transform(edge, horizontal_new_line(edge))
            for edge in sum(replacements, [])
        ], run_time = 2)
        """

        replacements = [replace_edge_with_two(6)]

        self.play(*[
            Transform(edge, horizontal_new_line(edge, RED))
            for edge in sum(replacements, [])
        ], run_time = 1.3)

        added_edges = replacements
        replacements = [replace_edge_with_two(8)]

        self.play(*[
            Transform(edge, horizontal_new_line(edge, BLUE))
            for edge in sum(replacements, [])
        ], run_time = 1.3)

        def vertical_new_line(line, color=WHITE):
            start = line.start.copy()
            end = line.end.copy()
            if start[1] < 0:
                end[1] = -3
            else:
                end[1] = 3
            return Line(start, end, color=color)

        added_edges += replacements
        replacements = [replace_edge_with_two(5)]

        self.play(*[
            Transform(edge, vertical_new_line(edge, GREEN))
            for edge in sum(replacements, [])
        ], run_time = 1.3)        
                
        self.wait(3)

        added_edges += replacements

        erase_anims = self.erase(op.itemgetter(0,1,2,3,4,7,9)(self.edges), play=False)
        erase_anims += self.erase(self.vertices, play=False)
        erase_anims += [Uncreate(e) for e in sum(added_edges, [])]
        erase_anims += [Uncreate(e) for e in arrows]
        erase_anims += [Uncreate(e) for e in [l1, l2, l3, l4, l5, l6]]
        self.play(*erase_anims)
        self.wait(2)

class TopologicalMinorScene(Scene):
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