from HeatMap import HeatMap
import random
import numpy as np


heat_map = np.random.uniform(low=0,high=50,size=(105,92))
ke1 = np.array([[random.randint(50,55),random.randint(70,73)]])
for k in range (0,92):
    for h in range (0,105):
        cor = np.array([[h,k]])
        rad1 = np.linalg.norm(ke1-cor)
        if rad1 < 6:
            pm_val1 = ((6-rad1)/6)*255
            heat_map[h,k] += pm_val1

hm = HeatMap('IMG_1249_s.jpg',heat_map,gaussian_std=2)

hm.plot(transparency=0.4,color_map='seismic')