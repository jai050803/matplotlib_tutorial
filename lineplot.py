import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotting the line plot with custom attributes
plt.plot(x, y,
         label='Sine Curve',  # Label for the legend
         color='blue',        # Line color
         linestyle='--',      # Line style (dashed)
         linewidth=2,         # Line width
         marker='o',          # Marker style (circle)
         markersize=8,        # Marker size
         markerfacecolor='red',  # Marker face color
         markeredgecolor='black',  # Marker edge color
         alpha=0.7,           # Transparency level
         zorder=10           # Rendering order (on top)
         )

# Adding labels, title, and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Custom Attributes')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
