import numpy as np
import matplotlib.pyplot as plt
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
        l = 2**iOrder
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
    plt.imshow(background)
    plt.plot(curve[:i,0],curve[:i,1],'w')
    plt.axis('off')
    
if __name__ == '__main__':
    defaultInputs = 1
    width, heigth = 512, 512
    background = np.zeros((width,heigth,3))

    if len(sys.argv)-1 == defaultInputs:
        order = int(sys.argv[1])
    else:
        order = 1
        
    N = 2**order
    total = N*N # 2D
    l = width / N # or height
    curve = np.zeros((total,2))
    frames = []
    for i in range(0,total):
        curve[i] = hilbert(i)
        curve[i] = curve[i]*l
        curve[i] += l/2
        frames.append(plot(i))
        
    gif.save(frames,path.join(getcwd(),'Hilbert.gif'),duration=50)
        
    
    
        
    
        