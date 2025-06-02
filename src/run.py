import numpy as np
from main import run_simulation
from plot import plot_robot

# Define links as vectors along the x-axis
links = [np.array([3, 0]), np.array([2, 0]), np.array([2, 0])]

# Joint angles in degrees (can be positive or negative)
angles = [70, -30, -45]

# Force vector applied at end effector
F = np.array([0, -10])  # Vertical force

# Run simulation
orig_positions, new_positions, torques, new_angles = run_simulation(angles, links, F)

# Visualize results
plot_robot(orig_positions, new_positions, torques, angles, new_angles, F)