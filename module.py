#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
 
print(Money)
AddMoney()
print(Money)

 
content = dir(math)
 
print(math.acosh)
# print("全局变量", globals().keys())
# print("局部变量", locals().keys())