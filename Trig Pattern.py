import math
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
graphRange=Range(-360,360,5,radians=True)
formula=lambda x: np.sin(x)#x**2+2*x-4#np.log(x)#1/x#
derivativeFormula=lambda x: np.cos(x)#2*(x)+2#1/x#-(x**-2)#
x=np.array(graphRange)
y=formula(x)
ax.plot(x,y, 'r')
def updateDerivative(i):
    f=str(derivativeFormula(i))+"*(x-"+str(i)+')+'+str(formula(i))
    return ax.plot(x, eval(f), color=plt.cm.hsv((i-x[0])/(x[-1]-x[0])))
anim = animation.FuncAnimation(fig, updateDerivative, x,  interval=1, blit=False,repeat=False)
plt.show()
