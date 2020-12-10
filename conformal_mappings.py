from manimlib.imports import *

import mpmath
mpmath.mp.dps = 7

UNIT_DISTANCE = FRAME_Y_RADIUS/4
IMAG = complex(0,1)
POINT = lambda x,y: UNIT_DISTANCE*x*y

class SectorMapVisual(ComplexTransformationScene):
    CONFIG = {
        "num_anchors_to_add_per_line" : 100,
        "horiz_end_color" : GOLD,
        "y_min" : 0,
    }
    def construct(self):
        self.add_title()
        self.plug_in_specific_values()
        self.show_transformation()
        #self.comment_on_two_dimensions()

    def add_title(self):
        title = TexMobject("f(z) = \\frac{z^4 - i}{z^4 + i}")
        title.add_background_rectangle()
        title.scale(1.2)
        title.to_corner(UP+LEFT)
        self.play(Write(title))
        self.add_foreground_mobject(title)
        self.wait()
        self.title = title

    def plug_in_specific_values(self):
        inputs = list(map(complex, [2, complex(2, 2), complex(0.1, 0.1)]))
        input_dots  = VGroup(*[
            Dot(self.z_to_point(z), color = YELLOW)
            for z in inputs
        ])
        output_dots = VGroup(*[
            Dot(self.z_to_point((z**4-complex(0,1))/(z**4+complex(0,1))), color = BLUE)
            for z in inputs
        ])
        arrows = VGroup()
        VGroup(*[
            ParametricFunction(
                lambda t : self.z_to_point(z*(1-t) + t*(z**4-complex(0,1))/(z**4+complex(0,1)))
            )
            for z in inputs
        ])
        for z, dot in zip(inputs, input_dots):
            path = ParametricFunction(
                lambda t : self.z_to_point(z*(1-t) + t*(z**4-complex(0,1))/(z**4+complex(0,1)))
            )
            dot.path = path
            arrow = ParametricFunction(
                lambda t : self.z_to_point(z*(1-t) + t*(z**4-complex(0,1))/(z**4+complex(0,1)))
            )
            stand_in_arrow = Arrow(
                arrow.points[-2], arrow.points[-1],
                tip_length = 0.2
            )
            arrow.add(stand_in_arrow.tip)
            arrows.add(arrow)
        arrows.set_color(WHITE)

        for input_dot, output_dot, arrow in zip(input_dots, output_dots, arrows):
            input_dot.save_state()
            input_dot.move_to(self.title[1][1])
            input_dot.set_fill(opacity = 0)

            self.play(input_dot.restore)
            self.wait()
            self.play(ShowCreation(arrow))
            self.play(ShowCreation(output_dot))
            self.wait()
        self.add_foreground_mobjects(arrows, output_dots, input_dots)
        self.input_dots = input_dots
        self.output_dots = output_dots

    def add_transformable_plane(self, **kwargs):
        ComplexTransformationScene.add_transformable_plane(self, **kwargs)
        #self.plane.next_to(ORIGIN, UP, buff = 0.01)
        self.plane.add(self.plane.copy().rotate(np.pi, RIGHT))
        self.plane.add(
            Line(ORIGIN, FRAME_X_RADIUS*RIGHT, color = self.horiz_end_color),
            Line(ORIGIN, FRAME_Y_RADIUS*RIGHT + FRAME_Y_RADIUS*UP, color = self.horiz_end_color),
        )
        self.add(self.plane)

    def show_transformation(self):
        self.add_transformable_plane()
        self.play(ShowCreation(self.plane, run_time = 3))

        self.wait()
        self.apply_complex_homotopy(
            lambda z, t : z*(1-t) + t*(z**4 + complex(0,-1))/(z**4 + complex(0,1)),
            added_anims = [
                MoveAlongPath(dot, dot.path, run_time = 5)
                for dot in self.input_dots
            ],
            run_time = 5
        )
        self.wait(2)


class HalfPlaneMapVisual(ComplexTransformationScene):
    CONFIG = {
        "num_anchors_to_add_per_line" : 100,
        "horiz_end_color" : GOLD,
        "y_min" : 0,
    }
    def construct(self):
        self.add_title()
        self.plug_in_specific_values()
        self.show_transformation()
        #self.comment_on_two_dimensions()

    def add_title(self):
        title = TexMobject("f(z) = \\frac{z - i}{z + i}")
        title.add_background_rectangle()
        title.scale(1.2)
        title.to_corner(UP+LEFT)
        self.play(Write(title))
        self.add_foreground_mobject(title)
        self.wait()
        self.title = title

    def plug_in_specific_values(self):
        inputs = list(map(complex, [-1, complex(0.5, 0.5), complex(2,2), complex(0,3)]))
        input_dots  = VGroup(*[
            Dot(self.z_to_point(z), color = YELLOW)
            for z in inputs
        ])
        output_dots = VGroup(*[
            Dot(self.z_to_point((z-complex(0,1))/(z+complex(0,1))), color = BLUE)
            for z in inputs
        ])
        arrows = VGroup()
        VGroup(*[
            ParametricFunction(
                lambda t : self.z_to_point(z*(1-t) + t*(z-complex(0,1))/(z+complex(0,1)))
            )
            for z in inputs
        ])
        for z, dot in zip(inputs, input_dots):
            path = ParametricFunction(
                lambda t : self.z_to_point(z*(1-t) + t*(z-complex(0,1))/(z+complex(0,1)))
            )
            dot.path = path
            arrow = ParametricFunction(
                lambda t : self.z_to_point(z*(1-t) + t*(z-complex(0,1))/(z+complex(0,1)))
            )
            stand_in_arrow = Arrow(
                arrow.points[-2], arrow.points[-1],
                tip_length = 0.2
            )
            arrow.add(stand_in_arrow.tip)
            arrows.add(arrow)
        arrows.set_color(WHITE)

        for input_dot, output_dot, arrow in zip(input_dots, output_dots, arrows):
            input_dot.save_state()
            input_dot.move_to(self.title[1][1])
            input_dot.set_fill(opacity = 0)

            self.play(input_dot.restore)
            self.wait()
            self.play(ShowCreation(arrow))
            self.play(ShowCreation(output_dot))
            self.wait()
        self.add_foreground_mobjects(arrows, output_dots, input_dots)
        self.input_dots = input_dots
        self.output_dots = output_dots

    def add_transformable_plane(self, **kwargs):
        ComplexTransformationScene.add_transformable_plane(self, **kwargs)
        #self.plane.next_to(ORIGIN, UP, buff = 0.01)
        self.plane.add(self.plane.copy().rotate(np.pi, RIGHT))
        self.plane.add(
            Line(ORIGIN, FRAME_X_RADIUS*RIGHT, color = self.horiz_end_color),
            Line(ORIGIN, FRAME_X_RADIUS*LEFT, color = self.horiz_end_color),
        )
        self.add(self.plane)

    def show_transformation(self):
        self.add_transformable_plane()
        self.play(ShowCreation(self.plane, run_time = 3))

        self.wait()
        self.apply_complex_homotopy(
            lambda z, t : z*(1-t) + t*(z + complex(0,-1))/(z + complex(0,1)),
            added_anims = [
                MoveAlongPath(dot, dot.path, run_time = 5)
                for dot in self.input_dots
            ],
            run_time = 5
        )
        self.wait(4)

class HStripMapVisual(ComplexTransformationScene):
    CONFIG = {
        "num_anchors_to_add_per_line" : 100,
        "horiz_end_color" : GOLD,
        "y_min" : 0,
    }

    def construct(self):
        self.phi = lambda z: (
                lambda t : (
                    self.z_to_point(
                        z*(1-t) + t*((mpmath.exp(PI*z/2) - 1)/(mpmath.exp(PI*z/2) + 1))
                    )
                )
            )
        self.add_title()
        self.plug_in_specific_values()
        self.show_transformation()
        #self.comment_on_two_dimensions()

    def add_title(self):
        title = TexMobject("f(z) = \\frac{e^{\pi z / 2} - 1}{e^{\pi z / 2} + 1}")
        title.add_background_rectangle()
        title.scale(1.1)
        title.to_corner(UP+LEFT)
        self.play(Write(title))
        self.add_foreground_mobject(title)
        self.wait()
        self.title = title

    def plug_in_specific_values(self):
        inputs = list(map(complex, [1, -1, complex(4,-0.5), complex(0,0.5)]))
        input_dots  = VGroup(*[
            Dot(self.z_to_point(z), color = YELLOW)
            for z in inputs
        ])
        output_dots = VGroup(*[
            Dot(self.phi(z)(1), color = BLUE)
            for z in inputs
        ])
        arrows = VGroup()
        VGroup(*[
            ParametricFunction(
                self.phi(z)
            )
            for z in inputs
        ])
        for z, dot in zip(inputs, input_dots):
            path = ParametricFunction(
                self.phi(z)
            )
            dot.path = path
            arrow = ParametricFunction(
                self.phi(z)
            )
            stand_in_arrow = Arrow(
                arrow.points[-2], arrow.points[-1],
                tip_length = 0.2
            )
            arrow.add(stand_in_arrow.tip)
            arrows.add(arrow)
        arrows.set_color(WHITE)

        for input_dot, output_dot, arrow in zip(input_dots, output_dots, arrows):
            input_dot.save_state()
            input_dot.move_to(self.title[1][1])
            input_dot.set_fill(opacity = 0)

            self.play(input_dot.restore)
            self.wait()
            self.play(ShowCreation(arrow))
            self.play(ShowCreation(output_dot))
            self.wait()
        self.add_foreground_mobjects(arrows, output_dots, input_dots)
        self.input_dots = input_dots
        self.output_dots = output_dots

    def add_transformable_plane(self, **kwargs):
        ComplexTransformationScene.add_transformable_plane(self, **kwargs)
        #self.plane.next_to(ORIGIN, UP, buff = 0.01)
        self.plane.add(self.plane.copy().rotate(np.pi, RIGHT))
        self.plane.add(
            Line(UNIT_DISTANCE*RIGHT*8 + UNIT_DISTANCE*UP*1, UNIT_DISTANCE*LEFT*8 + UNIT_DISTANCE*UP*1, color = self.horiz_end_color),
            Line(UNIT_DISTANCE*RIGHT*8 + UNIT_DISTANCE*DOWN*1, UNIT_DISTANCE*LEFT*8 + UNIT_DISTANCE*DOWN*1, color = self.horiz_end_color),
        )
        self.add(self.plane)

    def show_transformation(self):
        self.add_transformable_plane()
        self.play(ShowCreation(self.plane, run_time = 3))

        self.wait()
        self.apply_complex_homotopy(
            lambda z, t : z*(1-t) + t*((mpmath.exp(PI*z/2) - 1)/(mpmath.exp(PI*z/2) + 1)),
            added_anims = [
                MoveAlongPath(dot, dot.path, run_time = 5)
                for dot in self.input_dots
            ],
            run_time = 5
        )
        self.wait(2)

L = mpmath.exp(5*PI*IMAG/6)

class LunarMapVisual(ComplexTransformationScene):
    CONFIG = {
        "num_anchors_to_add_per_line" : 100,
        "horiz_end_color" : GOLD,
        "y_min" : 0,
    }

    def construct(self):
        self.phi = lambda z: (
            lambda t : self.z_to_point(
                z*(1-t) + t* (((L*z/(z-3))**6 - IMAG)/((L*z/(z-3))**6 + IMAG))
            )
        )
        self.add_title()
        self.plug_in_specific_values()
        self.show_transformation()
        #self.comment_on_two_dimensions()

    def add_title(self):
        title = TexMobject("f(z) = \\frac{(\\lambda z / (z - 3))^6 - i}{(\\lambda z / (z - 3))^6 + i}")
        title.set_color_by_tex("s", YELLOW)
        title.add_background_rectangle()
        title.scale(1.1)
        title.to_corner(UP+LEFT)
        self.play(Write(title))
        self.add_foreground_mobject(title)
        self.wait()
        self.title = title

    def plug_in_specific_values(self):
        inputs = list(map(complex, [0, 2.99, complex(1.5, .5)]))
        input_dots  = VGroup(*[
            Dot(self.z_to_point(z), color = YELLOW)
            for z in inputs
        ])
        output_dots = VGroup(*[
            Dot(self.phi(z)(1), color = BLUE)
            for z in inputs
        ])
        arrows = VGroup()
        VGroup(*[
            ParametricFunction(
                self.phi(z)
            )
            for z in inputs
        ])
        for z, dot in zip(inputs, input_dots):
            path = ParametricFunction(
                self.phi(z)
            )
            dot.path = path
            arrow = ParametricFunction(
                self.phi(z)
            )
            stand_in_arrow = Arrow(
                arrow.points[-2], arrow.points[-1],
                tip_length = 0.2
            )
            arrow.add(stand_in_arrow.tip)
            arrows.add(arrow)
        arrows.set_color(WHITE)

        for input_dot, output_dot, arrow in zip(input_dots, output_dots, arrows):
            input_dot.save_state()
            input_dot.move_to(self.title[1][1])
            input_dot.set_fill(opacity = 0)

            self.play(input_dot.restore)
            self.wait()
            self.play(ShowCreation(arrow))
            self.play(ShowCreation(output_dot))
            self.wait()
        self.add_foreground_mobjects(arrows, output_dots, input_dots)
        self.input_dots = input_dots
        self.output_dots = output_dots

    def add_transformable_plane(self, **kwargs):
        ComplexTransformationScene.add_transformable_plane(self, **kwargs)
        #self.plane.next_to(ORIGIN, UP, buff = 0.01)
        self.plane.add(self.plane.copy().rotate(np.pi, RIGHT))
        self.plane.add(
            ArcBetweenPoints(ORIGIN, UNIT_DISTANCE*RIGHT*3, angle=-TAU/6, color = self.horiz_end_color),
            ArcBetweenPoints(ORIGIN, UNIT_DISTANCE*RIGHT*3, angle=-TAU/3, color = self.horiz_end_color),
        )
        self.add(self.plane)

    def show_transformation(self):
        self.add_transformable_plane()
        self.play(ShowCreation(self.plane, run_time = 3))

        self.wait()
        self.apply_complex_homotopy(
            lambda z, t : z*(1-t) + t* (((L*z/(z-3))**6 - IMAG)/((L*z/(z-3))**6 + IMAG)),
            added_anims = [
                MoveAlongPath(dot, dot.path, run_time = 5)
                for dot in self.input_dots
            ],
            run_time = 5
        )
        self.wait(5)

class TranslationMapVisual(ComplexTransformationScene):
    CONFIG = {
        "num_anchors_to_add_per_line" : 100,
        "horiz_end_color" : GOLD,
        "y_min" : 0,
    }

    def construct(self):
        self.phi = lambda z: (
            lambda t : self.z_to_point(
                z*(1-t) + t*(z + complex(3,2))
            )
        )
        self.add_title()
        self.plug_in_specific_values()
        self.show_transformation()
        #self.comment_on_two_dimensions()

    def add_title(self):
        title = TexMobject("f(z) = z + (3 + 2i)")
        title.set_color_by_tex("s", YELLOW)
        title.add_background_rectangle()
        title.scale(1.1)
        title.to_corner(UP+LEFT)
        self.play(Write(title))
        self.add_foreground_mobject(title)
        self.wait()
        self.title = title

    def plug_in_specific_values(self):
        inputs = list(map(complex, [0]))
        input_dots  = VGroup(*[
            Dot(self.z_to_point(z), color = YELLOW)
            for z in inputs
        ])
        output_dots = VGroup(*[
            Dot(self.phi(z)(1), color = BLUE)
            for z in inputs
        ])
        arrows = VGroup()
        VGroup(*[
            ParametricFunction(
                self.phi(z)
            )
            for z in inputs
        ])
        for z, dot in zip(inputs, input_dots):
            path = ParametricFunction(
                self.phi(z)
            )
            dot.path = path
            arrow = ParametricFunction(
                self.phi(z)
            )
            stand_in_arrow = Arrow(
                arrow.points[-2], arrow.points[-1],
                tip_length = 0.2
            )
            arrow.add(stand_in_arrow.tip)
            arrows.add(arrow)
        arrows.set_color(WHITE)

        for input_dot, output_dot, arrow in zip(input_dots, output_dots, arrows):
            input_dot.save_state()
            input_dot.move_to(self.title[1][1])
            input_dot.set_fill(opacity = 0)

            self.play(input_dot.restore)
            self.wait()
            self.play(ShowCreation(arrow))
            self.play(ShowCreation(output_dot))
            self.wait()
        self.add_foreground_mobjects(arrows, output_dots, input_dots)
        self.input_dots = input_dots
        self.output_dots = output_dots

    def add_transformable_plane(self, **kwargs):
        ComplexTransformationScene.add_transformable_plane(self, **kwargs)
        #self.plane.next_to(ORIGIN, UP, buff = 0.01)
        self.plane.add(self.plane.copy().rotate(np.pi, RIGHT))
        # self.plane.add(
        #     ArcBetweenPoints(ORIGIN, UNIT_DISTANCE*RIGHT*3, angle=-TAU/6, color = self.horiz_end_color),
        #     ArcBetweenPoints(ORIGIN, UNIT_DISTANCE*RIGHT*3, angle=-TAU/3, color = self.horiz_end_color),
        # )
        self.add(self.plane)

    def show_transformation(self):
        self.add_transformable_plane()
        self.play(ShowCreation(self.plane, run_time = 3))

        self.wait()
        self.apply_complex_homotopy(
            lambda z, t : z*(1-t) + t*(z + complex(3,2)),
            added_anims = [
                MoveAlongPath(dot, dot.path, run_time = 5)
                for dot in self.input_dots
            ],
            run_time = 5
        )
        self.wait(5)

class MultiplicationMapVisual(ComplexTransformationScene):
    CONFIG = {
        "num_anchors_to_add_per_line" : 100,
        "horiz_end_color" : GOLD,
        "y_min" : 0,
    }

    def construct(self):
        self.phi = lambda z: (
            lambda t : self.z_to_point(
                z*(1-t) + t*(z * complex(1,2))
            )
        )
        self.add_title()
        self.plug_in_specific_values()
        self.show_transformation()
        #self.comment_on_two_dimensions()

    def add_title(self):
        title = TexMobject("f(z) = z * (1 + 2i)")
        title.set_color_by_tex("s", YELLOW)
        title.add_background_rectangle()
        title.scale(1.1)
        title.to_corner(UP+LEFT)
        self.play(Write(title))
        self.add_foreground_mobject(title)
        self.wait()
        self.title = title

    def plug_in_specific_values(self):
        inputs = list(map(complex, [1, complex(0,1)]))
        input_dots  = VGroup(*[
            Dot(self.z_to_point(z), color = YELLOW)
            for z in inputs
        ])
        output_dots = VGroup(*[
            Dot(self.phi(z)(1), color = BLUE)
            for z in inputs
        ])
        arrows = VGroup()
        VGroup(*[
            ParametricFunction(
                self.phi(z)
            )
            for z in inputs
        ])
        for z, dot in zip(inputs, input_dots):
            path = ParametricFunction(
                self.phi(z)
            )
            dot.path = path
            arrow = ParametricFunction(
                self.phi(z)
            )
            stand_in_arrow = Arrow(
                arrow.points[-2], arrow.points[-1],
                tip_length = 0.2
            )
            arrow.add(stand_in_arrow.tip)
            arrows.add(arrow)
        arrows.set_color(WHITE)

        for input_dot, output_dot, arrow in zip(input_dots, output_dots, arrows):
            input_dot.save_state()
            input_dot.move_to(self.title[1][1])
            input_dot.set_fill(opacity = 0)

            self.play(input_dot.restore)
            self.wait()
            self.play(ShowCreation(arrow))
            self.play(ShowCreation(output_dot))
            self.wait()
        self.add_foreground_mobjects(arrows, output_dots, input_dots)
        self.input_dots = input_dots
        self.output_dots = output_dots

    def add_transformable_plane(self, **kwargs):
        ComplexTransformationScene.add_transformable_plane(self, **kwargs)
        #self.plane.next_to(ORIGIN, UP, buff = 0.01)
        self.plane.add(self.plane.copy().rotate(np.pi, RIGHT))
        # self.plane.add(
        #     ArcBetweenPoints(ORIGIN, UNIT_DISTANCE*RIGHT*3, angle=-TAU/6, color = self.horiz_end_color),
        #     ArcBetweenPoints(ORIGIN, UNIT_DISTANCE*RIGHT*3, angle=-TAU/3, color = self.horiz_end_color),
        # )
        self.add(self.plane)

    def show_transformation(self):
        self.add_transformable_plane()
        self.play(ShowCreation(self.plane, run_time = 3))

        self.wait()
        self.apply_complex_homotopy(
            lambda z, t : z*(1-t) + t*(z * complex(1,2)),
            added_anims = [
                MoveAlongPath(dot, dot.path, run_time = 5)
                for dot in self.input_dots
            ],
            run_time = 5
        )
        self.wait(5)