import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import gif
from os import getcwd, path

def hilbert(i):
    index = i & 3
    points = np.array([[0,0],[0,1],[1,1],[1,0]])
    v = points[index]
    for iOrder in range(1,order):
        i = i >> 2
        index = i & 3
        l = int(2**iOrder)
        if index == 0:
            temp = v[0]
            v[0] = v[1]
            v[1] = temp
        elif index == 1:
            v[1] += l
        elif index == 2:
            v[0] += l
            v[1] += l
        elif index == 3:
            temp = l - 1 - v[0]
            v[0] = l - 1 - v[1]
            v[1] = temp
            v[0] += l
    return v

@gif.frame
def plot(i):
    plt.figure(frameon='False')    
    plt.imshow(img)
    x1 = curve[i-1,0]
    x2 = curve[i,0]
    y1 = curve[i-1,1]
    y2 = curve[i,1]
    x = np.arange(min(x1,x2),min(max(x1,x2)+1,width))
    y = np.arange(min(y1,y2),min(max(y1,y2)+1,heigth))
    xx,yy = np.meshgrid(x,y)
    background[xx,yy,3] = empty
    plt.imshow(background)
    plt.axis('off')
    
if __name__ == '__main__':
    defaultInputs = 3
    if len(sys.argv)-1 == defaultInputs:
        order = int(sys.argv[1])
        imagePath = sys.argv[2]
        gifPath = sys.argv[3]
    else:
        order = 1
        imagePath = 'Superman.png'
        gifPath = 'Superman.gif'
    # LOAD IMAGE
    img = mpimg.imread(imagePath)
    empty, full = 0, 255
    width, heigth, RGBa = img.shape
    background = np.zeros((width+1,heigth+1,RGBa))
    background[:,:,RGBa-1] = full
    N = int(2**order)
    total = N*N # 2D
    l = int(width / N) # or heigth
    curve = np.zeros((total,2)).astype(int)
    frames = []
    for i in range(0,total):
        curve[i] = hilbert(i)
        curve[i] = curve[i]*l
        curve[i] += int(l/2)
        if i > 0:
            frames.append(plot(i))    
    gif.save(frames,path.join(getcwd(),gifPath),duration=50)      