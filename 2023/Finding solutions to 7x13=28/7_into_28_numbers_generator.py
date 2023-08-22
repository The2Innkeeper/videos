def format_solution(solution):
    return f"""Division: {solution['factor1']} into {solution['product']} ({solution['product']}/{solution['factor1']}). {solution['factor1']} into {solution['product_units_digit']}: drop {solution['subtracted_number']} down, {solution['product_units_digit']}-{solution['subtracted_number']}={solution['dividend_units_digit']}. {solution['product']}/{solution['factor1']}={solution['answer']}.
Product: {solution['factor1']} times {solution['factor2']}={solution['factor1']}({solution['tens_digit']}+{solution['units_digit']})={solution['product']}. True product: {solution['true_product']}"""

def find_number_sets():
    solutions = []

    for factor1 in range(2, 10):
        for factor2 in range(10, 100):
            tens_digit = factor2 // 10
            units_digit = factor2 % 10
            product = factor1 * (tens_digit + units_digit)
            if product < 10: continue

            product_tens_digit = product // 10
            product_units_digit = product % 10
            if not product_tens_digit < factor1 and not product_units_digit >= factor1: continue

            integer_quotient = product_units_digit // factor1

            subtracted_number = factor1 * integer_quotient
            dividend = product - subtracted_number
            dividend_units_digit = product_units_digit % factor1
            answer = 10 * integer_quotient + dividend // factor1
            if factor2 != answer: continue

            true_product = factor1 * factor2
            solution = {
                    "factor2": factor2,
                    "factor1": factor1,
                    "answer": answer,
                    "tens_digit": tens_digit,
                    "units_digit": units_digit,
                    "product_tens_digit": product_tens_digit,
                    "product_units_digit": product_units_digit,
                    "product": product,
                    "subtracted_number": subtracted_number,
                    "dividend": dividend,
                    "dividend_units_digit": dividend_units_digit,
                    "true_product": true_product
            }
            if solution not in solutions:
                solutions.append(solution)

    print("Number of solutions:", len(solutions))

    for solution in solutions:
        print(format_solution(solution))

if __name__ == '__main__':
    find_number_sets()
