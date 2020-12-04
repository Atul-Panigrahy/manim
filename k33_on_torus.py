
from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *
from k3_3 import K33

def edge_to_two_edges(edge):
    start, end = edge.get_start_and_end()
    mid = (start + end) / 2
    return [
        Line(start, mid),
        Line(end, mid)
    ]

INSTANT = 0.000001

class K33OnTorus(OurGraphTheory):
    def construct(self):
        self.graph = K33()
        super().construct()
        # 2 5
        # 1 4
        # 0 3
        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()

        torus_creation_time = 1.5
        
        self.play(*[
            ShowCreation(Line((-3, 0, 0), (-3, 3, 0), color=PINK)),
            ShowCreation(Line((-3, 0, 0), (-3,-3, 0), color=PINK))
            ], run_time = torus_creation_time / 6)
        self.play(*[
            ShowCreation(Line((-3, 3, 0), (3, 3, 0), color=PINK)),
            ShowCreation(Line((-3,-3, 0), (3,-3, 0), color=PINK))
            ], run_time = 2 * torus_creation_time / 6)
        self.play(*[
            ShowCreation(Line((3, 3, 0), (3, 0, 0), color=PINK)),
            ShowCreation(Line((3,-3, 0), (3, 0, 0), color=PINK))
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
            
        
        straight_across = [0, 4, 8]

        replacements = [
            replace_edge_with_two(e)
            for e in straight_across
        ]

        def horizontal_new_line(line):
            start = line.start.copy()
            end = line.end.copy()
            if abs(start[0] - (-2)) < 0.1:
                end[0] = -3
            else:
                end[0] = 3
            return Line(start, end)

        self.play(*[
            Transform(edge, horizontal_new_line(edge))
            for edge in sum(replacements, [])
        ], run_time = 2)

        replacements = [replace_edge_with_two(5)]

        self.play(*[
            Transform(edge, horizontal_new_line(edge))
            for edge in sum(replacements, [])
        ], run_time = 1.3)

        replacements = [replace_edge_with_two(1)]

        self.play(*[
            Transform(edge, horizontal_new_line(edge))
            for edge in sum(replacements, [])
        ], run_time = 1.3)

        def vertical_new_line(line):
            start = line.start.copy()
            end = line.end.copy()
            if abs(start[0] - (-2)) < 0.1:
                end[1] = -3
            else:
                end[1] = 3
            return Line(start, end)

        replacements = [replace_edge_with_two(2)]

        self.play(*[
            Transform(edge, vertical_new_line(edge))
            for edge in sum(replacements, [])
        ], run_time = 1.3)        
                
            
        self.wait()
        self.wait()
