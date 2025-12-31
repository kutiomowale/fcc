#!/usr/bin/env python3
import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, destination):
        if self.withdraw(amount, f"Transfer to {destination.name}"):
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = []
        result.append(self.name.center(30, '*'))
        for entry in self.ledger:
            text = (f"{entry['description'][:23]:<23}{entry['amount']:>7.2f}")
            result.append(text)
        result.append(f"Total: {self.get_balance()}")
        result = '\n'.join(result)
        return result

    def total_withdrawals(self):
        result = 0
        for trans in self.ledger:
            if trans['amount'] < 0:
                result += trans['amount']
        return abs(result)


def create_spend_chart(categories):
    w_p_c = [cat.total_withdrawals() for cat in categories]
    total_spent = sum(w_p_c)
    if total_spent > 0:
        percentages = [math.floor(w/total_spent * 100) for w in w_p_c]
    else:
        percentages = (0) * len(categories)
    lines = []
    lines.append("Percentage spent by category")
    bar_char = 'o'
    for level in range(100, -10, -10):
        row = [f'{level:>3}|']
        for n in percentages:
            if level <= n:
                row.append(bar_char)
            else:
                row.append(' ')
        line = '  '.join(row) + '  '
        lines.append(line)

    horizontal_line = (
        f"    "
        f"{'---'*len(categories)}"
        f"--"
    )
    lines.append(horizontal_line)

    names = [category.name for category in categories]
    heights = [len(name) for name in names]
    max_height = max(heights)
    for index in range(max_height):
        row = ['    ']
        for name, height in zip(names, heights):
            if index < height:
                row.append(name[index])
            else:
                row.append(' ')
        lines.append('  '.join(row) + '  ')

    return '\n'.join(lines)


def main():
    food = Category('Food')
    food.deposit(100, 'deposit')
    food.withdraw(60, 'groceries')
    clothing = Category('Clothing')
    clothing.deposit(100, 'deposit')
    clothing.withdraw(20, 'house-clothes')
    auto = Category('Auto')
    auto.deposit(100, 'deposit')
    auto.withdraw(10, 'oil')
    tv = Category('Television')
    tv.deposit(100, 'deposit')
    tv.withdraw(10, 'house-clothes')
    print(create_spend_chart([food, clothing, auto, tv]))


if __name__ == '__main__':
    main()
