formula=input('Formula: ')
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
def derive(f):
    f=f.replace('-','+-').replace('*+-','*-').split('+')
    print(f)
    r=[]
    for coef in f:
	    if '*x**' in coef:
		    coef=[float(x) for x in coef.split('*x**')]
		    r.append((str(coef[0]*coef[1])+'*x**'+str(coef[1]-1)))
	    elif 'x**'==coef[:3]:
		    coef=float(coef[3:])
		    r.append(str(coef)+'*x**'+str(coef-1))
	    elif '*x' in coef:
		    r.append(coef.replace('*x',''))
    print('+'.join(r).replace('+-','-'))
    return '+'.join(r).replace('+-','-')

fig, ax = plt.subplots()
graphRange=Range(-1,1,0.01,removeZeros=True)
derivativeFormula=eval('lambda x: '+derive(formula))
formula=eval('lambda x: '+formula)
x=np.array(graphRange)
y=formula(x)
formulaLine,=ax.plot(x,y, 'r')
derivativeLine,=ax.plot(x, x, 'b')
point,=ax.plot([graphRange[0]], [0], 'ro')

def updateDerivative(i):
    f=str(derivativeFormula(i))+"*(x-"+str(i)+')+'+str(formula(i)).replace('--','+').replace('+-','-')
    #print(f)
    point.set_data([i],[formula(i)])
    derivativeLine.set_ydata(eval(f))
    return derivativeLine,
anim = animation.FuncAnimation(fig, updateDerivative, x,  interval=1, blit=False)
plt.show()
