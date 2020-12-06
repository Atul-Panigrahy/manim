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
        credit = TextMobject("Credits").scale(1.5).to_edge(UP)
        credit_list = BulletedList(
            "3b1b/manim: https://github.com/3b1b/manim",
            "Mary Radcliffe: http://www.math.cmu.edu/~mradclif/teaching/228F16/Kuratowski.pdf",
            "Artist: Music",
            alignment="\\justify"
        )
        self.play(Write(credit), Write(credit_list))
        self.wait()