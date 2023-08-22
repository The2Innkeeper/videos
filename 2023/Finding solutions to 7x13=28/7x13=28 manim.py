from manim import *

class Conditions(Scene):
    def construct(self):
        text_define_variables = Tex(
            r"""$f1$: $1$ digit\\
            $f2$: $2$ digits"""
        )
        text_product_definition = Tex(r"product $= f1 +$ digitSum$(f2)$")

        text_define_variables.to_edge(UP)
        text_product_definition.to_edge(UP)

        self.play(Write(text_define_variables))
        self.wait(2)
        self.play(ReplacementTransform(text_define_variables, text_product_definition))
        self.wait()

        condition_strings = [
            r"product $\geq 10$",
            r"units digit of product $>$ divisor",
            r"product $/ f1 = f2$"
        ]
        text_conditions = [Tex(string) for string in condition_strings]

        for i, text_condition in enumerate(text_conditions):
            if i == 0:
                text_condition.next_to(text_product_definition, DOWN)
            else:
                text_condition.next_to(text_conditions[i - 1], DOWN)

            self.play(Write(text_condition), run_time=0.75)
            self.wait()

        self.wait(0.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class DivisionAlgorithm(Scene):
    def construct(self):
        # Illustrate multiplication examples
        examples = [
            MathTex(r"7 \cdot 13 = 7 \cdot (1+3) = 28"),
            MathTex(r"7 \cdot 22 = 7 \cdot (2+2) = 28")
        ]
        for example in examples:
            example.next_to(ORIGIN, UP if example == examples[0] else DOWN, buff=0.2)
            self.play(Write(example))
        self.wait()

        # Clear the screen
        self.play(*[FadeOut(example) for example in examples])

        # Perform division steps
        dividend = MathTex(r"28")
        division_symbol = MathTex(r"\div")
        divisor = MathTex(r"7")
        minus_symbol = MathTex(r"-")
        equal_symbol = MathTex(r"=")
        zero = MathTex(r"0")
        one = MathTex(r"1")
        two = MathTex(r"2")
        three = MathTex(r"3")
        quotient = MathTex(r"13")
        remainder = MathTex(r"21")
        
        division = VGroup(dividend, division_symbol, divisor).arrange(RIGHT).move_to(UP*2)
        self.play(Write(division))
        self.wait()
        
        def align_vertically(object_to_align, reference_object, vertical_buffer=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.8):
            object_to_align.next_to(reference_object, DOWN, buff=vertical_buffer).align_to(reference_object, RIGHT)
            
        def animate_align_vertically(object_to_align, reference_object):
            return object_to_align.animate.next_to(reference_object, DOWN).align_to(reference_object, RIGHT)
        
        divisor_subtracted = divisor.copy()

        self.play(animate_align_vertically(divisor_subtracted, dividend))

        def get_width(mobject):
            return mobject.get_critical_point(RIGHT)[0] - mobject.get_critical_point(LEFT)[0]
        # Create a longer line that spans 2 digits to the left
        line_length = get_width(dividend) * 1.1
        subtraction_line = Line(ORIGIN, RIGHT * line_length)

        # Position the longer line underneath the digits
        align_vertically(subtraction_line, divisor_subtracted, vertical_buffer=0.1)

        subtract_symbol = minus_symbol.copy().next_to(VGroup(division, divisor_subtracted, subtraction_line), LEFT)
        
        self.play(Write(subtract_symbol))
        self.play(Create(subtraction_line))
        self.wait()
        
        quotient_tens = one.copy()
        division_result = VGroup(equal_symbol, quotient_tens).arrange(RIGHT)
        division_result.next_to(division, RIGHT)
        
        self.play(Write(division_result))
        
        remainder_units = one.copy()
        self.play(animate_align_vertically(remainder_units, subtraction_line))
        self.wait()
        
        two.align_to(dividend, LEFT)
        
        remainder_copy = remainder.copy()
        align_vertically(remainder_copy, subtraction_line)
        
        remainder_tens = two.copy()
        remainder_tens.next_to(remainder_units, LEFT, buff=0)
        align_vertically(remainder, remainder_units)
        
        subtraction_line_2 = subtraction_line.copy()
        align_vertically(subtraction_line_2, remainder, vertical_buffer=0.1)
        
        subtract_symbol_2 = subtract_symbol.copy()
        subtract_symbol_2.next_to(VGroup(remainder_tens, remainder, subtraction_line_2), LEFT)
        
        final_quotient = quotient.copy()
        final_quotient.align_to(quotient_tens, UL)
        
        remainder_final = zero.copy()
        align_vertically(remainder_final, subtraction_line_2)
        
        self.play(FadeOut(remainder_units))
        self.play(Transform(dividend.copy(), remainder_copy))
        self.play(Create(subtract_symbol_2))
        self.play(animate_align_vertically(remainder_copy.copy(), remainder_copy))
        self.play(Transform(quotient_tens, final_quotient))
        self.play(Create(subtraction_line_2))
        self.play(FadeIn(remainder_final))
        
        self.wait()
