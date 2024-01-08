from sklearn.cluster import KMeans
import numpy as np
import os
import cv2
from gvfc import get_value_from_colour


def colourcheck(origin, image):

    def hsv(r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
        v = mx*100
        return h, s, v
    


    clusters = 1
    
    size = os.path.getsize(image)/1024
    size = round(size, 0)
      
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters = int(clusters))

    clt.fit(image)
    
    final = np.reshape(clt.cluster_centers_, (1, 3))
    
    final = final[0]
    c1 = final[:3].tolist()
     
    x1 = np.round(hsv(*c1), 0)[0]
    
    vfc = get_value_from_colour(x1, origin)
    
    return vfc
