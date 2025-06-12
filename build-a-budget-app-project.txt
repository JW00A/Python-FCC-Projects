** start of main.py **

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(action['amount'] for action in self.ledger)
    
    def transfer(self, amount, other_category):
        if self.check_funds(amount):   
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __repr__(self):
        title = f"{'*' * 13}{self.name}{'*' * 13}\n"
        entries = '\n'.join(f"{action['description'][:23]:23}{action['amount']:>7.2f}" for action in self.ledger)
        return f"{title}{entries}\nTotal: {self.get_balance():.2f}"

food = Category('Food')
food.deposit(5000, 'Deposit')
food.withdraw(20, 'Groceries')
food.withdraw(100, 'Restaurant bill')
clothing = Category('Clothing')
clothing.deposit(1000, 'Deposit')
clothing.withdraw(100, 'apples')
food.transfer(1000, clothing)
print(food)

def create_spend_chart(categories):
    bar_chart_string = 'Percentage spent by category\n'

    total_spent = sum(sum(-action['amount'] for action in category.ledger if action['amount'] < 0) for category in categories)

    category_spent = {
        category.name: (sum(-action['amount'] for action in category.ledger if action['amount'] < 0) / total_spent * 100) // 10 * 10 for category in categories
    }

    for percent in range(100, -1, -10):
        bar_chart_string += f"{percent:>3}| " + "  ".join("o" if category_spent[category.name] >= percent else " " for category in categories) + "  \n"
 
    bar_chart_string += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    
    for length in range(max_length):
        bar_chart_string += "     " + "  ".join(category.name[length] if length < len(category.name) else " " for category in categories) + "  \n"
    
    return bar_chart_string.rstrip("\n")

print(create_spend_chart([food, clothing]))

** end of main.py **

