from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np

from manimlib.imports import *

class OurGraphTheory(Scene):
    def __init__(self, graph=None, *args, **kwargs):
        self.graph = graph
        Scene.__init__(self, *args, **kwargs)
        
    def construct(self):
        self.points = list(map(np.array, self.graph.vertices))
        if not hasattr(self.graph, 'vcolors'):
            self.vertices = self.dots = [Dot(p) for p in self.points]
        else:
            self.vertices = self.dots = [Dot(p, color=c) for (p,c) in zip(self.points, self.graph.vcolors)]
        self.edge_vertices = list(self.graph.edges)
        
        self.edges = self.lines = self.dashed = []

        if not hasattr(self.graph, 'eclasses'):
            for i, j in self.edge_vertices:
                if hasattr(self.graph, 'dashed') and (i, j) in self.graph.dashed:
                    l = DashedLine(self.points[i], self.points[j])
                else:
                    l = Line(self.points[i], self.points[j])
                self.edges.append(l)
        else:
            for (c, (i, j)) in zip(self.graph.eclasses, self.edge_vertices):
                l = c(self.points[i], self.points[j])
                self.edges.append(l)
        

    def shift_graph(self, amount):
        for v in self.vertices:
            v.shift(amount)
        for e in self.edges:
            e.shift(amount)

    def make_copies(self, mobjects):
        for i in range(len(self.vertices)):
            if self.vertices[i] in mobjects:
                self.vertices[i] = self.vertices[i].copy()
        for i in range(len(self.edges)):
            if self.edges[i] in mobjects:
                self.edges[i] = self.edges[i].copy()

    def draw(self, mobjects, play=True, run_time=1.0, reverse=False, **kwargs):
        if reverse:
            mobjects = [mobj.set_points(mobj.get_points()[::-1])
                        for mobj in mobjects]
        
        anims = [ShowCreation(mobj, run_time=run_time) 
                for mobj in mobjects]
        if play:
            self.play(*anims)

        return anims

    def draw_copy(self, mobjects, **kwargs):
        self.make_copies(mobjects)
        self.draw(mobjects, **kwargs)

    def erase_copy(self, mobjects, **kwargs):
        self.make_copies(mobjects)
        return self.erase(mobjects, **kwargs)

    def erase(self, mobjects, play=True, run_time=1.0, reverse=False, **kwargs):
        if reverse:
            mobjects = [mobj.set_points(mobj.get_points()[::-1])
                        for mobj in mobjects]
        
        anims = [Uncreate(mobj, run_time=run_time) 
                for mobj in mobjects]
        if play:
            self.play(*anims)

        return anims

    def draw_edges(self):
        self.play(*[
            ShowCreation(edge, run_time=1.0)
            for edge in self.edges
        ])

    def draw_vertices(self, verts = None, **kwargs):
        if not verts:
            verts = self.vertices
        #self.clear()
        self.play(*[ShowCreation(v, **kwargs)
                    for v in verts])

    def erase_vertices(self, verts = None, **kwargs):
        if not verts:
            verts = self.vertices
        self.play(*[Uncreate(v, **kwargs)
                    for v in verts])

    def accent_vertices(self, verts = None, color="lightgreen", **kwargs):
        if not verts:
            verts = self.vertices
        
        points = [d.get_center() for d in verts]
        
        self.remove(*verts)
        start = verts
        end = [Dot(point, radius=3 * DEFAULT_DOT_RADIUS,
                   color = color)
            for point in points
        ]
        self.play(*[Transform(
            s, e, rate_func=there_and_back,
            **kwargs
        )
            for (s, e) in zip(start, end)
        ])
        self.remove(*start)
        self.add(*verts)

    def accent_edges(self, color="lightgreen", **kwargs):
        self.remove(*self.edges)
        start = self.edges
        end = [
            Line(self.points[i], self.points[j],
                 stroke_width = 2 * DEFAULT_STROKE_WIDTH,
                 color = color)
            for i, j in self.edge_vertices
        ]
        print(len(start), len(end))
        self.play(*[Transform(
            s, e, rate_func=there_and_back,
            **kwargs
        )
            for (s, e) in zip(start, end)
        ])
        self.remove(*start)
        self.add(*self.edges)

        
    def trace_cycle(self, cycle=None, play=True,
                    color=RED, run_time=2.0):
        if cycle is None:
            cycle = self.graph.region_cycles[0]
        time_per_edge = run_time / len(cycle)
        next_in_cycle = it.cycle(cycle)
        next(next_in_cycle)  # jump one ahead
        self.traced_cycle = [
            Line(self.vertices[i].get_center(), self.vertices[j].get_center()).set_color(color)
            for i, j in zip(cycle, next_in_cycle)
        ]
        if play:
            for c in self.traced_cycle:
                self.play(ShowCreation(c),
                          run_time=run_time /
                          len(self.traced_cycle))
        return self.traced_cycle

    def annotate_edges(self, mobject, fade_in=True, **kwargs):
        angles = list(map(np.arctan, list(map(Line.get_slope, self.edges))))
        self.edge_annotations = [
            mobject.copy().rotate(angle).move_to(edge.get_center())
            for angle, edge in zip(angles, self.edges)
        ]
        if fade_in:
            self.play(*[
                FadeIn(ann, **kwargs)
                for ann in self.edge_annotations
            ])

    def remove_vertices(self, verts):
        self.play(*[Uncreate(vert) for vert in verts])

    def remove_edges(self, edges):
        self.play(*[Uncreate(edge) for edge in edges])
        
class K5(OurGraphTheory):
    def construct(self):
        self.graph = CompleteGraph(5)
        super().construct()

        # adding vertices not present in CompleteGraph(5)
        # in order to remove them later
        new_verts = [
            Dot(p) for p in
            [(0, 0, 0),
             (0, 1, 0)]
        ]
        
        self.draw_vertices(verts = self.vertices + new_verts)
        self.draw_edges()
        self.wait()
        self.trace_cycle([0, 4, 1, 3, 0])
        self.accent_vertices()
        self.accent_edges()
        # removing the extra vertices
        self.remove_vertices(new_verts)
        self.wait()
        
        
