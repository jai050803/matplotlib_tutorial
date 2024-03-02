import matplotlib.pyplot as plt

# Sample data
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

# Creating pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Adding title
plt.title('Pie Chart Example')

# Show plot
plt.show()
