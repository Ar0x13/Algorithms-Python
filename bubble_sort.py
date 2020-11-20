#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Bubble sorting in python3
"""

import random

numbers_list = [random.randint(1, 15) for x in range(1,15)]
print("start_list:", numbers_list)

for counter in range(1, len(numbers_list) - 1):
  i = 0
  for i in range(i, len(numbers_list) - 1):
    if numbers_list[i] > numbers_list[i+1]:
      numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
      i += 1
    elif numbers_list[i] <= numbers_list[i+1]:
      continue
    else:
      break

print("final_list:", numbers_list)
