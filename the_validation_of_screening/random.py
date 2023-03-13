# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:17:20 2022

@author: dell
"""


import random
mylist = [line.strip() for line in open(r"C:\Users\dell\Desktop\毕设\数据分析\validity\ANX.csv").readlines()]
print('\n',random.sample(mylist, k=2))

# ['cherry', 'apple']
