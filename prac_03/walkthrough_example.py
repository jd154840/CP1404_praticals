"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
from typing import Any


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_total = int(input("How many months? "))

    for month in range(1, month_total + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_income_statement(incomes, month_total)


def print_income_statement(incomes: list[Any], month_total: int):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_total + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {str(month)} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
