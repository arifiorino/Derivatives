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
def derive(f='2x**4+56x**2-2x+56'):
    f=f.replace('-','+-').split('+')
    print(f)
fig, ax = plt.subplots()
graphRange=Range(-360,360,10,radians=True)
formula=lambda x: np.sin(x)#x**2+2*x-4#np.log(x)#1/x#
derivativeFormula=lambda x: np.cos(x)#2*(x)+2#1/x#-(x**-2)#
x=np.array(graphRange)
y=formula(x)
formulaLine,=ax.plot(x,y, 'r')
derivativeLine,=ax.plot(x, x, 'b')
point,=ax.plot([graphRange[0]], [0], 'ro')

def updateDerivative(i):
    #print(i)
    f=str(derivativeFormula(i))+"*(x-"+str(i)+')+'+str(formula(i))
    #print(f)
    point.set_data([i],[formula(i)])
    derivativeLine.set_ydata(eval(f))
    return derivativeLine,
anim = animation.FuncAnimation(fig, updateDerivative, x,  interval=3, blit=False)
plt.show()
