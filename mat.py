import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 2, 1.6, 1.6])
y = np.array([0.5, -0.5, 0.5, 0])
z = np.array([1.6, 1.6, 0.9, 0.9])
t = np.array([0, 2, 4, 6])

AA = np.zeros((14, 14))
BB = np.zeros((14, 1))

# functions
def F4(t):
    return np.array([1, t, t**2, t**3, t**4])
def F4Dot(t):
    return np.array([0, 1, 2*t, 3*(t**2), 4*(t**3)])
def F4DotDot(t):
    return np.array([0, 0, 2, 6*t, 12*(t**2)])

def F3(t):
    return np.array([1, t, t**2, t**3])
def F3Dot(t):
    return np.array([0, 1, 2*t, 3*(t**2)])
def F3DotDot(t):
    return np.array([0, 0, 2, 6*t])


AA[0,0:5] = F4(t[0])                                    
BB[0] = x[0]
AA[1, 0:5] = F4Dot(t[0])
AA[2, 0:5] = F4DotDot(t[0])
AA[3,0:5] = F4(t[1])                                    
BB[3] = x[1]
AA[4,0:5] = F4(t[1])      
AA[4,5:9] = -F3(t[1])
AA[5,0:5] = F4Dot(t[1])   
AA[5,5:9] = -F3Dot(t[1])
AA[6,0:5] = F4DotDot(t[1])  
AA[6,5:9] = -F3DotDot(t[1])
AA[7,5:9] = F3(t[2])                                    
BB[7] = x[2]
AA[8,5:9] = F3(t[2])      
AA[8,9:14] = -F4(t[2])
AA[9,5:9] = F3Dot(t[2])  
AA[9,9:14] = -F4Dot(t[2])
AA[10,5:9] = F3DotDot(t[2]) 
AA[10,9:14] = -F4DotDot(t[2])
AA[11,9:14] = F4(t[3])                                 
BB[11] = x[3]
AA[12,9:14] = F4Dot(t[3])
AA[13,9:14] = F4DotDot(t[3])

coeff = np.linalg.lstsq(AA, BB)[0]

print(coeff)
print("Coef length: ", len(coeff))

a = coeff[0:5]
b = coeff[5:9]
c = coeff[9:14]

tsamp1 = np.linspace(t[0],t[1],100)
tsamp2 = np.linspace(t[1],t[2],100)
tsamp3 = np.linspace(t[2],t[3],100)

xsamp1 = []
for i in tsamp1:
    xsamp1.append(np.matmul(F4(i), a))

xsamp2 = []
for i in tsamp2:
    xsamp2.append(np.matmul(F3(i), b))

xsamp3 = []
for i in tsamp3:
    xsamp3.append(np.matmul(F4(i), c))


plt.plot(tsamp1, xsamp1)
plt.plot(tsamp2, xsamp2)
plt.plot(tsamp3, xsamp3)
plt.show()