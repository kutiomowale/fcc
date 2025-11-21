#!/usr/bin/env python3

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
        percentages = [int(round((w/total_spent * 100), -1)) for w in w_p_c]
    else:
        percentages = (0) * len(categories)
    result = []
    result.append("Percentage spent by category")
    result.append(f"             0 10 20 30 40 50 60 70 80 90 100")
    for c, p in zip(categories, percentages):
        result.append(f"{c.name[:10]:<10} o {'o o ' * int(p/10)}")
    text = "\n".join(result)
    return text
