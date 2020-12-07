
from functools import reduce
import itertools as it
import operator as op
import copy
import numpy as np
import random

from manimlib.imports import *
from our_discrete_graph_scene import *
from k3_3 import K33


class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Manim is fun")
        second_line = TextMobject("and useful")
        final_line = TextMobject("Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("Hope you like it too!")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)

        #Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)



class K33_Nonplanar(OurGraphTheory):
    def construct(self):
        self.graph = K33()
        super().construct()
        # 2 5
        # 1 4
        # 0 3

        removals = []

        lemma = TextMobject("Lemma: $K_{3, 3}$ is Nonplanar")
        lemma.shift(UP * 3.5)
        self.play(Write(lemma))
        removals.append(lemma)
        
        self.draw(self.vertices)
        self.draw(self.edges)
        self.wait()
        # V - E + F = 2
 #       removals.extend(self.vertices)
 #       removals.append(self.edges)

        eulers_form = TextMobject("$V - E + F = 2$")
        eulers_form.shift(LEFT * 4.5 + UP * 2.5)
        self.play(Write(eulers_form))
        self.wait(2.5)
        removals.append(eulers_form)
        
        # V = 6
        self.accent_vertices()
        eulers_form = TextMobject("$6 - E + F = 2$")
        eulers_form.shift(LEFT * 4.5 + UP * 1.5)
        self.play(Write(eulers_form))
        self.wait(2.5)
        removals.append(eulers_form)

        # E = 9
        self.accent_edges()
        eulers_form = TextMobject("$6 - 9 + F = 2$")
        eulers_form.shift(LEFT * 4.5 + UP * 0.5)
        self.play(Write(eulers_form))
        self.wait(2.5)
        removals.append(eulers_form)
        
        # F = 5
        eulers_form = TextMobject("$F = 5$")
        eulers_form.shift(LEFT * 4.5 + DOWN * 0.5)
        self.play(Write(eulers_form))
        self.wait(2.5)
        removals.append(eulers_form)
        
        
        eulers_form = TextMobject("No 3 Edge Faces")
        eulers_form.shift(RIGHT * 4.5 + UP * 2.5)
        self.play(Write(eulers_form))
        removals.append(eulers_form)
        
        # no 3 edge cycles
        three_cycles = [
            [4, 1, 5, 2],
            [3, 2, 5, 1],
            [3, 0, 5, 2],
            [2, 3, 1, 4],
            [5, 0, 3, 2],
            [2, 5, 0, 3],
            [1, 5, 0, 3],
        ]
        for path in three_cycles:
            path = self.trace_path(path, run_time = 1.3)
            self.remove(*path)
            self.wait(0.5)

        edges_faces = TextMobject("No 3 Edge Faces")
        edges_faces.shift(RIGHT * 4.5 + UP * 2.5)
        self.play(Write(edges_faces))    
        self.wait(2.5)
        removals.append(edges_faces)

        edges_faces = TextMobject("$4F \leq 2E$")
        edges_faces.shift(RIGHT * 4.5 + UP * 1.5)
        self.play(Write(edges_faces))    
        self.wait(1.5)
        removals.append(edges_faces)
        
        # E = 9
        self.accent_edges()
        edges_faces = TextMobject("$4F \leq 2*9$")
        edges_faces.shift(RIGHT * 4.5 + UP * 0.5)
        self.play(Write(edges_faces))
        self.wait(1.5)
        removals.append(edges_faces)

        edges_faces = TextMobject("$F \leq 4.5$")
        edges_faces.shift(RIGHT * 4.5 + DOWN * 0.5)
        self.play(Write(edges_faces))
        self.wait(2.5)
        removals.append(edges_faces)

        #thus 4f <= 2e gives f <= 3
        #gives 5 <= 3 contradiction

        contradiction = TextMobject("$5 = F \leq 4.5$")
        contradiction.shift(DOWN * 2.5)
        self.play(Write(contradiction))
        self.wait(1.5)
        removals.append(contradiction)

        contradiction2 = TextMobject("$5 \leq 4.5$")
        contradiction2.shift(DOWN * 2.5)
        self.play(Transform(contradiction, contradiction2))
        self.wait(4.5)
        removals.append(contradiction2)

        self.play(*[FadeOut(v) for v in removals + self.vertices + self.edges])
        
