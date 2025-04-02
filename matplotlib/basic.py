import matplotlib.pyplot as plt
# Sample data: Stock prices over 7 days

# days=['mon','tue','wed','thu','fri','sat','sun']
# stock_price=[120,125,123,130,128,135,110]
# plt.figure(figsize=(8,5))
# plt.plot(days,stock_price,marker='o',color='Black',linestyle='-')
# plt.title("Stock Price Trend Over a Week")
# plt.xlabel("days")
# plt.ylabel("price in(usd)")
# plt.grid(True)
# plt.show()

# student attendence over 5 days (education domain)

# days=['mon','tue','wed','thu','fri']
# attendence=[80,78,82,85,90]
# plt.subplot(323)
# plt.plot(days,attendence,marker='D',color='green')
# plt.title("3 student attendance over a week")
# plt.xlabel("days")
# plt.ylabel("No. of student")
# plt.grid(True)
# plt.show()



#montly product sales(sales/marketing domain)

# months=['jan','feb','mar','apr','may','jun']
# sales=[5000,7000,8000,7500,9000,10000]
# plt.subplot(324)
# plt.plot(months,sales,marker='^',color='purple')
# plt.title("4 monthly product Sales")
# plt.xlabel("Months")
# plt.ylabel("Units Sold")
# plt.grid(True)

# months=['jan','feb','mar','apr','may','jun']
# sales=[5000,7000,8000,7500,9000,10000]
# plt.subplot(234)
# plt.plot(months,sales,marker='^',color='purple')
# plt.title("4 monthly product Sales")
# plt.xlabel("Months")
# plt.ylabel("Units Sold")
# plt.grid(True)

# plt.show()


#Heart Rate Over Time (Health Domain)
 

# minutes=[0,5,10,15,20,25,30]
# heart_rate=[72,76,80,85,82,78,74]
# plt.subplot(325)
# plt.plot(minutes,heart_rate,marker="*",color='red')
# plt.title("5.heart rate over time")
# plt.xlabel("Minutes")
# plt.ylabel("BPM(Beast per minutes)")
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# revenue and profit

# months=['jan','feb','mar','apr','may','jun']
# revenue=[15000,18000,20000,22000,25000,28000]
# profit=[5000,6000,6500,7000,8000,9000]
# plt.figure(figsize=(8,5))
# plt.plot(months,revenue,label='Revenue',marker='o',color='blue')
# plt.plot(months,profit,label='Profit',marker='s',color="orange")
# plt.title("Revenue vs profit")
# plt.xlabel("Month")
# plt.ylabel("Amount($)")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# # Add Value Labels for Revenue
# for i in range(len(months)):
#     plt.text(months[i],revenue[i]+500,  f"${revenue[i]+500}", ha='center', fontsize=9,color='green')
# plt.show()



