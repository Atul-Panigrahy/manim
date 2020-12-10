
from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from kuratowski.our_discrete_graph_scene import *

class FlatCubeGraph(CubeGraph):
    """
     5  6
      12
      03
     4  7
    """
    def construct(self):
        super().construct()
        SCALE_FACTOR = 3
        self.vertices = [
            (v[0] * SCALE_FACTOR,
             v[1] * SCALE_FACTOR,
             v[2] * SCALE_FACTOR)
            for v in self.vertices
        ]
    


class CubeGraphOnSphere(CubeGraph):
    """
     5  6
      12
      03
     4  7
    """
    def construct(self):
        super().construct()
        self.vertices = [
            (-1, -1, -1),
            (-1,  1, -1),
            ( 1,  1, -1),
            ( 1, -1, -1),
        ]
        xshift = -0.6
        yshift = -0.4
        self.vertices += [
            (v[0], v[1], 1)
            for v in self.vertices
        ]
        SCALE_FACTOR = 1.5
        self.vertices = [
            (v[0] * SCALE_FACTOR,
             v[1] * SCALE_FACTOR,
             v[2] * SCALE_FACTOR)
            for v in self.vertices
        ]
"""
class SphereToPlaneScene(OurGraphTheory):
    def construct(self):
        self.graph = CubeGraphOnSphere()
        super().construct()

        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()

        cycle = self.trace_cycle(
            cycle = [4, 5, 6, 7],
            run_time = 1
        )
        self.wait(0.5)
        
        planar = OurGraphTheory(FlatCubeGraph())
        planar.construct()
        planar_cycle = planar.trace_cycle(
            cycle = [4, 5, 6, 7],
            play = False
        )
        
        graph_trans = zip(
            self.vertices + self.edges + cycle,
            planar.vertices + planar.edges + planar_cycle
        )
        self.play(*[
            Transform(mobj1, mobj2)
            for mobj1,mobj2 in graph_trans
        ])
        self.wait()
"""


class ThreeDSurfaceGraphScene(ThreeDScene):
    def __init__(self, graph=None, *args, **kwargs):
        self.graph = graph
        ThreeDScene.__init__(self, *args, **kwargs)
        
    def construct(self):
        self.points = list(map(np.array, self.graph.vertices))
        self.vertices = self.dots = [Dot(p) for p in self.points]
        self.edge_vertices = list(self.graph.edges)
        self.edges = self.lines = [
            Line(self.points[i], self.points[j])
            for i, j in self.edge_vertices
        ]

    def draw(self, mobjects, run_time = 1.0, **kwargs):
        self.play(*[ShowCreation(mobj, run_time=run_time) 
                    for mobj in mobjects])

    def erase(self, mobjects, **kwargs):
        self.play(*[Uncreate(mobj, run_time=1.0) 
                    for mobj in mobjects])

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
            Line(self.points[i], self.points[j]).set_color(color)
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






class SphereToPlaneScene(ThreeDSurfaceGraphScene):
    def construct(self):
        axes = ThreeDAxes()
        a=1.5
        trr = ParametricSurface(
            lambda u, v : np.array([
                 a * np.cos(TAU * u) * np.sin(TAU * v),
                 a * np.sin(TAU * u) * np.sin(TAU * v),
                 a * np.cos(TAU * v)
             ]),
            resolution=(32, 64)).fade(0.7) #Resolution of the surfaces
        def project_onto_unit_cube(x, y, z):
            return np.array([x, y, z]) / max(abs(x),
                                             abs(y),
                                             abs(z))
            
        trr2 = ParametricSurface(
            lambda u, v : a * project_onto_unit_cube(
                 np.cos(TAU * u) * np.sin(TAU * v),
                 np.sin(TAU * u) * np.sin(TAU * v),
                 np.cos(TAU * v)
             ),
            resolution=(32, 64)).fade(0.7) #Resolution of the surfaces

        self.set_camera_orientation(phi=60 * DEGREES,theta=-60*DEGREES)

        self.add(axes)

        self.play(Write(trr), run_time = 1)
        self.wait()
        self.play(ReplacementTransform(trr, trr2), run_time = 1)
        self.wait()
        self.graph = CubeGraphOnSphere()
        super().construct()

        self.draw(self.vertices, run_time = 0.00001)
        self.draw(self.edges)
        self.wait()

        
        cycle = self.trace_cycle(
            cycle = [4, 5, 6, 7],
            run_time = 1
        )
        self.wait(0.5)

        self.play(FadeOut(trr2), run_time = 0.5)
        self.remove(trr2)
        
        planar = OurGraphTheory(CubeGraph())
        planar.construct()
        planar_cycle = planar.trace_cycle(
            cycle = [4, 5, 6, 7],
            play = False
        )
        
        graph_trans = zip(
            self.vertices + self.edges + cycle,
            planar.vertices + planar.edges + planar_cycle
        )
        self.play(*[
            Transform(mobj1, mobj2)
            for mobj1,mobj2 in graph_trans
        ])
        self.wait(3)
        self.play(*[
            FadeOut(v) for v in \
            self.vertices + self.edges + cycle
            ])

def stereographic_projection(X, Y, scale):
    X /= scale
    Y /= scale
    denom = 1 + X * X + Y * Y
    x = 2 * X / denom * scale
    y = 2 * Y / denom * scale
    z = (-1 + X * X + Y * Y) / denom * scale
    return (x, y, z)

                
class GraphForOnSphere_Planar(Graph):
    def construct(self):
        super().construct()
        self.vertices = [
            (-0.25, -0.25, 0),
            (-0.5,  1, 0),
            ( 1,  1, 0),
            ( 1, -1, 0),
            (3.5,  1, 0),
            (-2,  3, 0),
            (-2, -2, 0)
        ]
        self.edges = [
            (0, 1),
            (2, 3),
            (3, 0),
            (1, 2),
            (4, 5),
            (2, 4),
            (3, 4),
            (0, 5),
            (1, 5),
            (5, 6),
            (6, 3)
        ]
        SCALE_FACTOR = 1.3
        self.vertices = [
            (v[0] * SCALE_FACTOR,
             v[1] * SCALE_FACTOR,
             v[2] * SCALE_FACTOR)
            for v in self.vertices
        ]

STEREO_SCALE = 3
        
class GraphForOnSphere_OnSphere(GraphForOnSphere_Planar):
    def construct(self):
        super().construct()
        self.vertices = [
            stereographic_projection(v[0], v[1], STEREO_SCALE)
            for v in self.vertices
        ]

class IntroMessage(Scene):
    def construct(self):
        f1 = TextMobject("Euler's Formula: \\\\ $V - E + F = 2$ for convex polyhedra \\\\$ $ \\\\ We will generalize it to planar graphs \\\\ by using stereographic projection")
        f1.shift(UP*1)
        f1.scale(1)
        self.play(Write(f1))
        self.wait(6)
        self.play(FadeOut(f1))

        
class PlaneToSphereScene(ThreeDSurfaceGraphScene):
    def construct(self):
        axes = ThreeDAxes()

        self.graph = GraphForOnSphere_Planar()
        super().construct()
        self.set_camera_orientation(phi=60 * DEGREES,theta=-60*DEGREES)
        self.add(axes)
        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()
        a=STEREO_SCALE
        on_sphere = OurGraphTheory(GraphForOnSphere_OnSphere())
        on_sphere.construct()
        
        graph_trans = zip(
            self.vertices + self.edges,
            on_sphere.vertices + on_sphere.edges
        )
        self.wait(3)
        self.play(*[
            Transform(mobj1, mobj2)
            for mobj1,mobj2 in graph_trans
        ])
        self.wait()
        


        trr = ParametricSurface(
            lambda u, v : np.array([
                 a * np.cos(TAU * u) * np.sin(TAU * v),
                 a * np.sin(TAU * u) * np.sin(TAU * v),
                 a * np.cos(TAU * v)
             ]),
            resolution=(32, 64)).fade(0.7) #Resolution of the surfaces

        self.play(Write(trr))
        self.wait()
        self.play(*[
            FadeOut(v) for v in \
            [trr, axes] + self.vertices + self.edges
            ])


