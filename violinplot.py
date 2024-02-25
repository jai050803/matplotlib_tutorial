import matplotlib.pyplot as plt
import numpy as np

# Generating sample data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Creating violin plot
plt.violinplot(data)

# Adding labels and title
plt.title('Violin Plot Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Show plot
plt.show()
