import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[4,5,6,8]
plt.bar(x,y, color=['red', 'blue'])  

plt.title("Urban vs Rural Student Distribution")
plt.xlabel("Address Type")
plt.ylabel("Count")

plt.show()