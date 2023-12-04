#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0): 
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0  

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.last_transaction_amount != 0:
            self.total -= self.last_transaction_amount
            self.items = self.items[:-1]  
            self.last_transaction_amount = 0

