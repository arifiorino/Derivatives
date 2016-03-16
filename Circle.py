import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import matplotlib.animation as animation

def Range(start=-2, end=2, i=.01, radians=False, shift=0, removeZeros=False):
    r=np.arange(start+(i*shift),end,i)
    if radians:
        r=np.radians(r)
    if removeZeros:
        b=r.tolist()
        r1=[]
        for n in b:
            if n>i or n<-i:
                r1.append(n)
        r=np.array(r1)
    return r
fig, ax = plt.subplots()
graphRange=Range(-1,1,0.01)
plt.axis([-2, 2, -2, 2])
#plt.gcf().gca().add_artist(plt.Circle((0,0),1,fill=False))
def updateDerivative(i):
    r=np.sqrt(7)
    x,y=np.cos(i),np.sin(i)
    ax.plot([r*np.cos(i-(np.pi/2))+x,r*np.cos(i+(np.pi/2))+x],[r*np.sin(i-(np.pi/2))+y,r*np.sin(i+(np.pi/2))+y],color=plt.cm.hsv(i/(np.pi*2)))
anim = animation.FuncAnimation(fig, updateDerivative, Range(0,360,5,radians=True),  interval=1, blit=False, repeat=False)
plt.get_current_fig_manager().window.wm_geometry("600x600+20+20")
plt.show()
