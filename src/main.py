import numpy as np
import matplotlib.pyplot as plt

def rotate_vector(vector, angle_deg):
    """Rotate a 2D vector by angle in degrees."""
    angle_rad = np.radians(angle_deg)
    rot_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    return rot_matrix @ vector

# Define links as vectors along the x-axis
links = [np.array([3, 0]), np.array([2, 0]), np.array([2, 0])]

# Joint angles in degrees (can be positive or negative)
angles = [70, -30, -45]

# Calculate cumulative angles for each link
cumulative_angles = np.cumsum(angles)

# Calculate joint positions
positions = [np.array([0, 0])]  # origin
for link, angle in zip(links, cumulative_angles):
    rotated_link = rotate_vector(link, angle)
    new_pos = positions[-1] + rotated_link
    positions.append(new_pos)

# Extract X and Y coordinates for plotting
x_coords = [pos[0] for pos in positions]
y_coords = [pos[1] for pos in positions]

# Plotting with colored links
plt.figure(figsize=(8, 8))

# Plot each link with distinct color
colors = ['b', 'g', 'r']
for i in range(len(links)):
    plt.plot([x_coords[i], x_coords[i+1]], [y_coords[i], y_coords[i+1]], color=colors[i], linewidth=3, label=f'Link {i+1}')

# Mark the joints with black dots
plt.scatter(x_coords, y_coords, color='k', zorder=5)

# Label the joints
labels = ['Origin', 'Joint 1', 'Joint 2', 'End Effector']
for x, y, label in zip(x_coords, y_coords, labels):
    plt.text(x, y, label, fontsize=12, ha='right')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Robot Arm Simulation')
plt.grid(True)
plt.axis('equal')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.legend()
plt.show()
