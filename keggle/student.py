import pandas as pd
import matplotlib.pyplot as plt
v=pd.read_csv("student-mat.csv")
f=pd.read_csv("student-por.csv")
df=pd.concat([v,f],ignore_index=True)
# t=df.to_csv("nishant.csv")
# print(df["G3"].mean())
# print(v["G3"].mean())
# print(f["G3"].mean())
# list=df["address"].tolist()
# p=[]
# p.append(list.count('U'))
# p.append(list.count('R'))
# q=['urban','rular']
# plt.bar(q,p,color=['red', 'blue'])  
# plt.title("Urban vs Rural Student Distribution")
# plt.xlabel("Address Type")
# plt.ylabel("Count")
# plt.show()

# p=df["schoolsup"].count()
# d=df[df["schoolsup"]=="yes"].count()
# i=d.schoolsup
# persentage=i*100/p
# print(persentage)

h=df["studytime"].value_counts()
r=h.tolist()
print(r)
o=df.groupby("studytime")['G3'].mean()
list1=o.tolist()
print(list1)
plt.scatter(list1,r,color='red',marker='o')
plt.title("Performance & Study Habits")
plt.xlabel("study_time")
plt.ylabel("affect_final_grades")
plt.show()

# print(df[['absences','G3']].corr())
# print(df[['G1','G2','G3']].corr())