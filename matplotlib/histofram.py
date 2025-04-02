import numpy as np 
import matplotlib.pyplot as plt
# d=np.random.rand(1000)
# plt.figure()
# plt.hist(d,bins=30,color='green',alpha=0.7)
# plt.xlabel("value")
# plt.ylabel("frequency")
# plt.title("histogram")
# plt.show()


# lables=["A","B","C"]
# size=[25,35,40]
# color=['gold','yellowgreen','lightcoral']
# plt.figure()
# plt.pie(size,labels=lables,colors=color,autopct='%1.1f%%')
# plt.title("pie chart")
# plt.show()


# d=[np.random.rand(100),np.random.rand(100)+1,np.random.rand(100)+2]
# plt.figure()
# plt.boxplot(d)
# plt.xlabel("category")
# plt.ylabel("values")
# plt.title("Box plot example")
# plt.show()


# fig,axs = plt.subplots(2,2)
# x=np.linspace(0,10,100)
# axs[0,0].plot(x,np.sin(x),'o')
# axs[0,0].set_title("sine")
# axs[0,1].plot(x,np.cos(x),'d')
# axs[0,1].set_title("cosine")
# axs[1,0].plot(x,np.tan(x),'p')
# axs[1,0].set_title("tangent")
# axs[1,1].plot(x,-np.sin(x),'g')
# axs[1,1].set_title("Negative Sine")
# plt.tight_layout()
# plt.show()




fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=np.random.rand(50)
y=np.random.rand(50)
z=np.random.rand(50)
ax.scatter(x,y,z,c='r',marker='o')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("z-lable")
plt.title("3d Scatter plot")
plt.show()