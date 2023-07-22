#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    # self.item=item
    self.discount=discount
    self.total=total

  def add_item(self, item, price, quantity=1):
    self.total+=price*quantity

  def apply_discount(self, discount=0.8):
    if discount == 0:
      print("There is no discount to apply.")
    else:
      old_price=self.total
      new_price=old_price*discount
      discount_price=(int(new_price))
      self.total=discount_price
      print(f"After the discount, the total comes to ${discount_price}.")