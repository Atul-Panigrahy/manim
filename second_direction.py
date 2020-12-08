from manimlib.imports import *

class SecondDirectionScene(Scene):
    def construct(self):
        super().construct()

        self.wait()

        f1 = TextMobject("$G$ is nonplanar  $\\implies$  $G$ contains a subgraph \\\\ which is a subdivision of $K_{5}$ or $K_{3,3}.$")
        f1.scale(1).shift(UP*2)
        self.play(Write(f1))

        self.wait(5)

        self.play(*[FadeOut(e) for e in [f1]])

        self.wait()