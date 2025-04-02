# import pandas as pd
# h=pd.read_csv("delhivery_data.csv")
# print(h)
# h["trip_creation_time"]=pd.to_datetime(h["trip_creation_time"],errors="coerce")


# h["trip_creation_day"]=h["trip_creation_time"].dt.day_name()
# print(h["trip_creation_time"].value_counts())


# print("average trip time duration: \n",(h["od_end_time"]-h["od_start_time"]).mean())



# import matplotlib.pyplot as mt
# import numpy as np
# x=np.array([5,8,6,1])
# y=np.array([6,3,1,2])
# mt.plot(x,y)
# mt.show()



import matplotlib.pyplot as plt

# Data for the plots
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
brands = ['Toyota', 'Ford', 'BMW', 'Audi', 'Tesla']
car_prices = [20000, 15000, 25000, 28000, 32000]
fuel_types = ['Petrol', 'Diesel', 'Electric']
fuel_counts = [40, 30, 30]
mileages = [50000, 60000, 70000, 80000, 50000]

# 1. Line Chart

plt.figure(figsize=(10,6))  # New figure with size
plt.subplot(231)  # 2x3 grid, first subplot
plt.plot(mileages, y, color='blue', marker='o', linestyle='-', label="Car Price vs Year")
plt.title("Line Chart Example")
plt.xlabel("Year")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()