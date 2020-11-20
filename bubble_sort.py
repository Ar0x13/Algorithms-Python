#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Bubble sorting in python3
"""

import random

numbers_list = [random.randint(1, 15) for x in range(1,15)]

print("my_start_list: \n",  numbers_list)
for i in range(len(numbers_list) - 1):
  for j in range(len(numbers_list) - 1):
    if numbers_list[j] > numbers_list[j+1]:
      numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
print("my_final_list: \n", numbers_list)
