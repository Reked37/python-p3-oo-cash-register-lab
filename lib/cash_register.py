#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.items=[]
    self.discount=discount
    self.total=0

  def add_item(self, item, price, quantity=1):
    n=quantity
    while n >0:
     self.items.append(item)
     n-=1
    self.total+=price*quantity

  def apply_discount(self):
    if self.discount !=0:
      self.total-=(self.discount/100.0)*self.total
      # old_price=self.total
      # new_price=old_price*(discount/100)
      # discount_price=(int(new_price))
      # self.total=discount_price
      print(f"After the discount, the total comes to ${self.total:g}.")
    else:
      print("There is no discount to apply.")
    
      