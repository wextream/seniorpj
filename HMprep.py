import numpy as np
from PIL import  Image
import scipy.ndimage as ndimage
import random

def HM_matrix(image,gaussian_std=10):

    image = Image.open(image)
    width, height = image.size

    heat_map = np.random.uniform(low=20,high=110,size=(27,43))
    ke1 = np.array([[4,3]])
    ke2 = np.array([[6,3]])
    ke3 = np.array([[7,9]])
    ke4 = np.array([[4,7]])
    ke5 = np.array([[3,10]])

    el1 = np.array([[8,27]])
    a1 = 25
    b1 = 5

    for k in range (0,43):
        for h in range (0,24):
            cor = np.array([[h,k]])
            rad1 = np.linalg.norm(ke1-cor)
            rad2 = np.linalg.norm(ke2-cor)
            rad3 = np.linalg.norm(ke3-cor)
            rad4 = np.linalg.norm(ke4-cor)
            rad5 = np.linalg.norm(ke5-cor)
            el1 = ((k-27)**2)/a1 + ((h-8)**2)/b1 
            if rad1 < 2:
                pm_val1 = ((2-rad1)/2)*255
                heat_map[h,k] += pm_val1
            if rad2 < 4:
                pm_val2 = ((4-rad2)/4)*255
                heat_map[h,k] += pm_val2
            if rad3 < 5:
                pm_val3 = ((5-rad3)/5)*255
                heat_map[h,k] += pm_val3
            if rad4 < 2:
                pm_val4 = ((2-rad4)/2)*255
                heat_map[h,k] += pm_val4
            if rad5 < 3:
                pm_val5 = ((3-rad5)/3)*255
                heat_map[h,k] += pm_val5
            if k==18 or k==35:
                if h in range (12,25):
                    heat_map[h,k] += random.randint(180,210)
                    if k==18:
                        heat_map[h,k-1] += random.randint(100,150)
                    if k==35:
                        heat_map[h,k+1] += random.randint(100,150)
            if k==24 or k==29:
                if h in range (12,22):
                    heat_map[h,k] += random.randint(180,210)
                    if k==23:
                        heat_map[h,k+1] += random.randint(100,150)
                    if k==30:
                        heat_map[h,k-1] += random.randint(100,150)
            if h==12:
                if k in range (18,25) or k in range (30,36):
                    heat_map[h,k] += random.randint(180,210)
                    heat_map[h-1,k] += random.randint(100,150)
            if h==20:
                if k in range (24,30):
                    heat_map[h,k] += random.randint(100,150)
            

    for l in range (10,27):
        for m in range (0,10):
            heat_map[l,m] = 0
    heatmap_image = Image.fromarray(heat_map)
    heatmap_image_resized = heatmap_image.resize((width,height))
    heatmap_image_resized = ndimage.gaussian_filter(heatmap_image_resized, 
                                                        sigma=(gaussian_std, gaussian_std), 
                                                        order=0)
    heatmap_image_resized = np.asarray(heatmap_image_resized)

    return image , heatmap_image_resized


