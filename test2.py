import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d  import Axes3D

# 曲线图
# x=np.arange(-10,10,0.005)
# y=x**2+1
# plt.xlim(-10,10)
# plt.plot(x,y)
# plt.show()
#
# # 散点图
# n=1000
# x=np.random.normal(0,1,n)
# y=np.random.normal(0,1,n)
#
# plt.scatter(x,y,alpha=0.5)
# plt.xlim(-1.5,1.5)
# plt.ylim(-1.5,1.5)
# plt.xticks()
# plt.yticks()
# plt.show()


# 3D
fig=plt.figure()
ax=Axes3D(fig)

x=[1,2,3,4]
y=[3,4,5,6]
z=[5,6,7,8]

ax.scatter(x,y,z)
plt.show()