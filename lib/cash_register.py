#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.items=[]
    self.discount=discount
    self.total=0

  def add_item(self, item, price, quantity=1):
    self.price=price
    n=quantity
    while n >0:
     self.items.append(item)
     n-=1
    self.total+=price*quantity

  def apply_discount(self):
    if self.discount !=0:
      self.total-=(self.discount/100.0)*self.total
      print(f"After the discount, the total comes to ${self.total:g}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    second_last_element=self.items[-2]
    print(second_last_element)
    last_element=self.items[-1]
    if last_element == second_last_element:
      second_total=self.items.remove(last_element), self.total-self.price
      subtract= self.total-self.price-self.price
      self.total=subtract
    else:
     new_total=self.items.remove(last_element), self.total-self.price
     sub=self.total-self.price
     self.total=sub
     loop_list=[item for item in self.items]
     print(loop_list)
   
 
      
    


      