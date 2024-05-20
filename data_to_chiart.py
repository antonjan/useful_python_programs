import matplotlib.pyplot as plt
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [80, 20, 50, 30]
fig, ax1 = plt.subplots()
ax1.bar(categories, values, color='skyblue')
ax1.set_ylabel('Values', color='skyblue')
ax1.tick_params('y', colors='skyblue')
ax2= ax1.twinx()
cumulative_values = [sum(values[:i+1]) for i in range(len(values))]
ax2.plot(categories, cumulative_values, color='red', marker='o')
ax2.set_ylabel('Cumulative Values', color='red')
ax2.tick_params('y', colors='red')
plt.title('Pareto Chart')
plt.show()
#clcoding.com
