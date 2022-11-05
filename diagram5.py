#!/usr/bin/env python
# youtube link : https://www.youtube.com/watch?v=DOnY6eZi2E8&ab_channel=DavidCabatingan

from manimlib.imports import *
import numpy as np

class diagram5(Scene):
    def construct(self):
        DOT_RADIUS = 0.08
        WAIT_TIME = 0.7

        Dot1 = Dot(Color=WHITE, radius = DOT_RADIUS).shift(UL)
        Dot2 = Dot(color=WHITE, radius = DOT_RADIUS).shift(DL)
        Dot3 = Dot(color=WHITE, radius= DOT_RADIUS)
        Dot4 = Dot(color=WHITE, radius= DOT_RADIUS).shift(RIGHT*2)

        dottedLineFromDot1_Dot3 = DashedLine(start=ORIGIN, end=ORIGIN+UL)
        dottedLineFromDot2_Dot3 = DashedLine(start=ORIGIN, end=ORIGIN+DL)
        lineFromDot2_Dot4 = Line(start=ORIGIN, end=ORIGIN+RIGHT*2)
        
        Animations = []
        
        Animations.append(ShowCreation(Dot3))
        Animations.append(ShowCreation(Dot1))
        Animations.append(ShowCreation(Dot2))
        Animations.append(ShowCreation(Dot4))
        Animations.append(GrowFromPoint(dottedLineFromDot1_Dot3, ORIGIN))
        Animations.append(GrowFromPoint(dottedLineFromDot2_Dot3, ORIGIN))

        self.play(*Animations)

        self.wait(WAIT_TIME)

        self.play(GrowFromPoint(lineFromDot2_Dot4, ORIGIN))

        self.wait()
