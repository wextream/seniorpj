import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import  Image
import scipy.ndimage as ndimage
import math

def mapping(input,min,max):
    delta = max - min
    return (255/delta) * (input -min)



def param_func(df,pmwant):
    lat = df['lat'].tolist()
    lon = df['lon'].tolist()
    lat.sort(reverse=True)
    lon.sort()
    pmval = df[pmwant].tolist()
    df_list  = df.values.tolist()
    return [pmval,lat,lon,df_list]


def HM_pro(df,pmwant,wid,hig):
    val = param_func(df,pmwant)[0]
    lat = param_func(df,pmwant)[1]
    lon = param_func(df,pmwant)[2]
    location = param_func(df,pmwant)[3]

    d_lon = (max(lon)-min(lon))
    d_lat = (max(lat)-min(lat))
    scale = d_lat/d_lon
    data_size_lon = int(math.ceil(math.sqrt(len(lon)/scale)))
    data_size_lat = int(data_size_lon*scale)
    #data_size = math.ceil(math.sqrt(len(lon)))

    data_mt = np.zeros((data_size_lat,data_size_lon))
    lon_time = (max(lon)-min(lon))/(data_size_lon)
    lat_time = (max(lat)-min(lat))/(data_size_lat)

    min_of_val  =  min(val)
    max_of_val  =  max(val)
    for i in location:
        lat_of_i = i[0]
        lon_of_i = i[1]
        pm = i[2]
        index_lon = math.floor((lon_of_i-min(lon))/lon_time)
        index_lat = (data_size_lat-1) - math.floor((lat_of_i-min(lat))/lat_time)
        if index_lon == data_size_lon:
            index_lon = data_size_lon-1
        if index_lat == -1:
            index_lat = 0
        if data_mt[index_lat,index_lon] != 0:
            data_mt[index_lat,index_lon] = (data_mt[index_lat,index_lon] + mapping(pm,min_of_val,max_of_val))/2
        if data_mt[index_lat,index_lon] == 0 :
            data_mt[index_lat,index_lon] = mapping(pm,min_of_val,max_of_val)



    heatmap_image = Image.fromarray(data_mt)
    heatmap_image_resized = heatmap_image.resize((wid,hig))
    heatmap_image_resized = np.asarray(heatmap_image_resized)
    heatmap_image_resized = np.clip(heatmap_image_resized,0,255)

    return heatmap_image_resized

# p = param_func('HM_data.txt')
# print(p)

# heatmap_image_resized = HM_pro(p[0],p[1],p[2])
# print(heatmap_image_resized)

# fig , ax = plt.subplots(figsize=(300/100 , 600/100),frameon=False)
# ax.imshow(heatmap_image_resized,alpha=0.8,cmap='seismic')
# ax.axis('off')
# plt.savefig("./static/test3.png")







