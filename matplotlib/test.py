import matplotlib.pyplot as plt
import numpy as np
# y=[6,5]
# z=[4,4]
# plt.figure(figsize=(8,5))
# plt.plot(y,z,color='red',marker='*',linestyle='--')
# plt.title("xy")
# plt.xlabel("kv")
# plt.ylabel("uj")
# plt.grid(True)
# plt.tight_layout()
# plt.legend()
# plt.show()


# t=['apple','orange']
# u=[45,56]
# color=['red','green']
# plt.pie(u,labels=t,colors=color,autopct="%1.1f%%")
# plt.show()


# t=np.random.rand(50)
# plt.figure()
# plt.hist(t,bins=4,color='green',alpha=0.9)
# plt.show()


# p=[4,8,15,6,4]
# q=[4,8,6,16,5]
# plt.figure()
# plt.bar(p,q,color=["gray",'blue'])
# plt.show()


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
p=np.random.rand(10)
q=np.random.randn(10)
ax.scatter(p,q,c='red',marker="*")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.show()