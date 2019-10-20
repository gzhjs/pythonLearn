#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串

#字符串
for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)
#序列
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果 :', fruit)
#元组
tupleExamp = (1, "hello", 2, "world")
for tulp in tupleExamp:
    print("当前元素：", tulp)
#字典
dict1 = {1: "hello", 2: "world"}
for dictEle in dict1:
    print("当前字典元素：" + dict1[dictEle])