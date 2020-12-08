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
            " Prof. Bena Tshishiku: for mentorship.",
            " 3Blue1Brown: for the manim Python library.",
            " Mary Radcliffe: for the notes on Kuratowski's Theorem.",
            " Music from Ambient 1 by Brian Eno",
        ).scale(0.8)
        credit_links = TextMobject("https://github.com/3b1b/manim \\\\ http://www.math.cmu.edu/$\\sim$ mradclif/teaching/228F16/Kuratowski.pdf").next_to(credit_list, DOWN*4).scale(0.7)
        self.wait()
        self.play(Write(credit), Write(credit_list), Write(credit_links))
        self.wait(15)
        self.play(Uncreate(credit), Uncreate(credit_list), Uncreate(credit_links))
        self.wait()


class OutlineSlide(Scene):
    def construct(self):
        prelim_title = TextMobject("Outline:").to_edge(UP)

        prelim = BulletedList(
            " Statement of the Theorem",
            " Graph Theory Background",
            " Proof of the Theorem",
            " Related Topics",
        )#.next_to(prelim_title, DOWN * 4)
        self.play(Write(prelim_title), Write(prelim))
        self.wait(10)
        self.play(*[
            FadeOut(t)
            for t in [prelim, prelim_title]
            ])
        self.wait()