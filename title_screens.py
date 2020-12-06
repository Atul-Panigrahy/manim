from manimlib.imports import *

class IntroSlide(Scene):
    def construct(self):
        title = TextMobject("Kurtowski's Theorem")
        title.scale(2)

        credit = TextMobject("by: David Cabatingan, Ken Cole, and Petar Peshev")
        credit.scale(0.8)
        credit.next_to(title, DOWN*2)
        
        self.play(Write(title))
        self.play(Write(credit))
        self.wait(5)
        self.play(Uncreate(title), Uncreate(credit))
        self.wait()

class OutroSlide(Scene):
    def construct(self):
        "here"