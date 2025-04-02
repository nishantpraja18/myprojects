import matplotlib.pyplot as plt
name=['ankita','ravi','deshna','bhumi','nitin']
marks=[95,85,97,89,85]
clas=[11,12,10,11,12]
hight=[5.9,5.6,5.5,5.5,5.7]

plt.plot(name,marks,label="marks",marker="*",linestyle="--",color="Black")
plt.plot(name,clas,label="clas",marker="^",linestyle="-",color="pink")
plt.plot(name,hight,label="hight",marker="o",linestyle="-",color="Green")
plt.title("marks , class and hight")
plt.xlabel("name")
plt.ylabel("marks")
plt.grid(True)
plt.fill_between(name,marks)
plt.fill_between(name,clas)
plt.fill_between(name,hight)
plt.legend()
plt.show()