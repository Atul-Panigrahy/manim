from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *

class ForwardGraph(Graph):
    def construct(self):
        self.vertices = [
            (-2,-1,0),
            (1,-2,0),
            (2,1,0),
            (2,-1,0),
            (-1,-2,0),
            (-2,1,0),
            (0,0,0),
            (-1,2,0),
            (1,2,0),
            (-1,2,0),
        ]

        self.edges = [
            (0,6),
            (6,3),
            (0,4),
            (0,5),
            (1,3),
            (1,4),
            (1,5),
            (2,3),
            (2,4),
            (2,5),
            (5,7),
            (7,8),
            (8,2),
            (6,8)
        ]

class K33TargetGraph(Graph):
    """
    2 5
    1 4
    0 3  
    """
    
    def construct(self):
        self.vertices = [
            (-1,1,0),
            (-1,0,0),
            (-1,-1,0),
            (1,1,0),
            (1,0,0),
            (1,-1,0),
            (0,1,0),
        ]
        SCALE = 1.6
        self.vertices = [
            (v[0] * SCALE,
             v[1] * SCALE,
             v[2] * SCALE)
            for v in self.vertices
        ]
        self.edges = [
            (0,6),
            (6,3),
            (0,4),
            (0,5),
            (1,3),
            (1,4),
            (1,5),
            (2,3),
            (2,4),
            (2,5)
        ]

class K33TargetScene(OurGraphTheory):
    def construct(self):
        self.graph = K33TargetGraph()
        super().construct()
        self.shift_graph(RIGHT*2 + DOWN * 0.5)
        for i in [0, 1, 2]:
            self.vertices[i].set_color(RED)
        for i in [3, 4, 5]:
            self.vertices[i].set_color(GREEN)

class KuratowskiStatementForwardScene(OurGraphTheory):
    def construct(self):
        self.graph = ForwardGraph()
        super().construct()

        self.shift_graph(LEFT*3+0.5*DOWN)

        f1 = TextMobject("Kuratowski's Theorem: \\\\ A graph is nonplanar $\\Longleftrightarrow$ it has a subgraph \\\\ which is a subdivision of $K_5$ or $K_{3,3}$")
        f1.shift(UP*2.5)
        f1.scale(1)
        self.play(Write(f1))
        self.wait(5)

        self.draw(self.edges)
        self.draw(self.vertices)
        self.wait()

        f2 = TextMobject("Nonplanar graph $G$")
        f2.shift(DOWN*3)
        f2.scale(1)
        self.play(Write(f2), run_time = 0.5)
        self.wait(3)
        
        red_verts = [0,1,2]
        green_verts = [3,4,5]

        # for v in red_verts:
        #     self.vertices[v].set_color(RED)

        # for v in green_verts:
        #     self.vertices[v].set_color(GREEN)
        
        self.play(
            *[Transform(
                self.vertices[i], 
                Dot(self.vertices[i].get_center(), color=RED),
                run_time=0.3) for i in red_verts],
            *[Transform(
                self.vertices[i], 
                Dot(self.vertices[i].get_center(), color=GREEN),
                run_time=0.3) for i in green_verts]
        )
        #self.play(*[Transform(self.vertices[i], self.vertices[i]) for i in red_verts + green_verts])

        self.wait(4)

        old_verts = self.vertices[:7]
        old_edges = self.edges[:10]

        remove_edges = self.edges[10:]
        remove_verts = self.vertices[7:]  

        erasures = self.erase(remove_edges + remove_verts, play = False)

        f3 = TextMobject("Subgraph of $G$")
        f3.shift(DOWN*3)
        f3.scale(1)
        self.play(*([Transform(f2,f3)] + erasures))
        self.wait(2)
        new_graph_scene = K33TargetScene()

        v_transforms = [Transform(v1,v2, run_time=2) for (v1, v2) in zip(old_verts, new_graph_scene.vertices)]
        e_transforms = [Transform(e1,e2, run_time=2) for (e1, e2) in zip(old_edges, new_graph_scene.edges)]

#        self.play(*(v_transforms + e_transforms))

        f3 = TextMobject("Subgraph is a subdivision of $K_{3,3}$")
        f3.shift(DOWN*3)
        f3.scale(1)
        self.play(*(v_transforms + e_transforms + [Transform(f2,f3)]))
        self.wait(6)

        self.erase(old_verts+old_edges+[f2])

        prelim_title = TextMobject("Preliminaries:").next_to(f1, DOWN*3)

        prelim = BulletedList(
            "Planar Graphs and their Properties",
            "Subgraphs and Subdivisions",
            "2-Connected Graphs and their Properties"
        ).next_to(prelim_title, DOWN * 1.5)
        self.play(Write(prelim_title), Write(prelim))
        self.wait(5.5)
        self.play(*[
            FadeOut(t)
            for t in [prelim, prelim_title, f1]
            ])
        self.wait()




