from manimlib.imports import *

class IntroSlide(Scene):
    def construct(self):
        title = TextMobject("Kuratowski's Theorem")
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
            " 3Blue1Brown: for the manim Python library",
            " Mary Radcliffe: for the notes on Kuratowski's Theorem",
            " Prof. Bena Tshishiku: for mentorship",
            " Artist: for Music",
        ).scale(0.8)
        credit_links = TextMobject("https://github.com/3b1b/manim \\\\ http://www.math.cmu.edu/$\\sim$ mradclif/teaching/228F16/Kuratowski.pdf").next_to(credit_list, DOWN*4).scale(0.7)
        self.play(Write(credit), Write(credit_list), Write(credit_links))
        self.wait(5)
        self.play(Uncreate(credit), Uncreate(credit_list), Uncreate(credit_links))
        self.wait()