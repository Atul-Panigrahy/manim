from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *


class K4(Graph):
    def construct(self):
        self.vertices = [v0, v1, v2, v3] = [
            (-2, -2, 0),
            (-2, 2, 0),
            (2, 2, 0),
            (2, -2, 0)
        ]

        self.edges = []
        for vj in range(4):
            for vi in range(vj):
                self.edges.append((vi, vj))         


class PlanarK4(Graph):
    def construct(self):
        self.vertices = [v0, v1, v2, v3] = [
            (-2, -2, 0),
            (0, 2, 0),
            (0, -0.5, 0),
            (2, -2, 0)
        ]

        self.edges = []
        for vj in range(4):
            for vi in range(vj):
                self.edges.append((vi, vj))         


class PlanarSubgraphScene(OurGraphTheory):
    def construct(self):
        self.graph = K4()
        super().construct()

        self.draw(self.vertices)
        self.draw(self.edges)
        #self.wait()


        circle = Circle(radius=0.5, color=RED)
        self.play(ShowCreation(circle, run_time=0.5))
        self.play(FadeOut(circle, run_time=0.5))
        #self.wait()

        planar = OurGraphTheory(PlanarK4())
        planar.construct()
        graph_trans = zip(self.vertices + self.edges, planar.vertices+planar.edges)
        self.play(*[Transform(mobj1, mobj2) for mobj1,mobj2 in graph_trans])
        #self.wait()

        subgraph_words = TextMobject("Subgraphs of a planar graph are planar.")
        subgraph_words.next_to(self.vertices[1], UP*2)
        self.play(Write(subgraph_words))

        to_delete = [self.vertices[2]]
        to_delete += [self.edges[i] for i in range(1,len(self.edges))]
        self.erase_copy(to_delete)
        #self.wait()
        to_return = [self.edges[4], self.edges[3]]
        self.draw(to_return)
        #self.wait()
        
        to_return = [self.vertices[2], self.edges[1], self.edges[2]]
        anims = self.draw(to_return, play=False)
        anims += self.erase_copy([self.edges[3]], play=False)
        self.play(*anims)
        self.wait(2)

        subdivision_words = TextMobject("Subdivisions of a planar graph are planar.")
        subdivision_words.next_to(self.vertices[1], UP*2)

        anims = self.draw([self.edges[3], self.edges[5]], play=False)
        anims += [Transform(subgraph_words, subdivision_words)]
        self.play(*anims)

        self.wait()

        new_points = [
            random.uniform(0.15,0.85)*(planar.points[i]-planar.points[j]) + planar.points[j]
            for i, j in planar.edge_vertices
        ]
        new_verts = [Dot(p, color=RED) for p in new_points]
        
        self.draw(new_verts)
        self.wait()
        self.erase(new_verts)
        self.wait()

        self.play(*(self.erase(self.vertices, play=False) + self.erase(self.edges, play=False)))

        return

        nonplanar = OurGraphTheory(CompleteGraph(5))
        nonplanar.construct()

        anims = self.draw(nonplanar.edges, play=False)
        anims += self.draw(nonplanar.vertices, play=False)

        np_subdivision_words = TextMobject("Subdivisions of a \\textbf{non}planar graph are \\textbf{not} planar.")
        np_subdivision_words.next_to(nonplanar.vertices[1], UP*2)
        self.play(*(anims + [Transform(subdivision_words, np_subdivision_words)]))

        self.wait()

        new_points = [
            random.uniform(0.15,0.85)*(nonplanar.points[i]-nonplanar.points[j]) + nonplanar.points[j]
            for i, j in nonplanar.edge_vertices
        ]
        new_verts = [Dot(p, color=RED) for p in new_points]
        
        self.draw(new_verts)
        self.wait()
        self.erase(new_verts)
        self.wait()





class SubdivisionGraph(Graph):
    def construct(self):
        v1 = (-2, 0, 0)
        v2 = (0, -2, 0)
        v3 = (0, 2, 0)
        v4 = (2, 0, 0)
        v5 = (4, 0, 0)
        self.vertices = [v1, v2, v3, v4, v5]

        self.edges = [
            (0, 1), 
            (1, 3), 
            (3, 2), 
            (2, 0), 
            (1, 4), 
            (2, 4), 
            (1, 2)
        ]



class PlanarSubdivisions(OurGraphTheory):
    def construct(self):
        self.graph = SubdivisionGraph()
        super().construct()
        self.draw(self.vertices)
        self.draw(self.edges)

        new_points = [
            random.uniform(0.15,0.85)*(self.points[i]-self.points[j]) + self.points[j]
            for i, j in self.edge_vertices
        ]
        new_verts = [Dot(p, color=BLUE) for p in new_points]
        
        self.draw(new_verts)
        self.wait()
        self.erase(new_verts)
        self.wait()
        self.accent_vertices([self.vertices[4]])
        self.erase([self.vertices[4]])
        self.wait()
        print(self.vertices[4].get_center())