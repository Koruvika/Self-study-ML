# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 06:11:47 2021

@author: Admin
"""

import pandas as pd
import numpy as np

x = np.arange(1, 10).reshape((3,3))

np.random.seed(20)

sales_amounts = np.random.randint(1,40, size = (7,4))
weekly_sales = pd.DataFrame(sales_amounts, index= ["Mon","Tues","Weds","Thur","Fri",
                                                   "Sat", "Sun"], columns=("Cake", "Milk", 
                                                   "Candy", "Butter"))

# print(weekly_sales)

price = np.array([8, 5, 2, 3])
good_price = pd.DataFrame(price.reshape((1,4)), index = ["Price"], columns=("Cake", "Milk", 
                                                   "Candy", "Butter" ))
print(good_price)

weekly_sales["Total Price"] = sales_amounts.dot(price)
print(weekly_sales)