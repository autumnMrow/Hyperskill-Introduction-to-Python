import math

tax_percent = 0
income = int(input())

tax_ranges = [
    (0, 15527, 0),
    (15528, 42707, 0.15),
    (42708, 132406, 0.25),
    (132407, math.inf, 0.28)
    ]

percent = next(tax_percent for min_income, max_income, tax_percent in tax_ranges if min_income <= income <= max_income)

calculated_tax = income * percent
display_percent = 100 * percent

print("The tax for {} is {}%. That is {} dollars!".format(income, (round(display_percent)), round(calculated_tax)))
