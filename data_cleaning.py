# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:15:53 2020

@author: Benjamen Underwood
"""

import pandas as pd

df = pd.read_csv('cars.csv')
df['MSRP'] = [29125, 35200, 39200, 29125,
              28800, 28750, 25000, 59900,
              63570, 73570, 73570, 27495,
              28495, 