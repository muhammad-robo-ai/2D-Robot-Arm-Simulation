import numpy as np
import matplotlib.pyplot as plt

# Length of the links
link1 = np.array([3, 0])
link2 = np.array([2, 0])
link3 = np.array([2, 0])

# Angles for each link
angle_L1 = 75
angle_L2 = 45
angle_L3 = 15

# Convert angles to radians
angle_L1_rad = np.radians(angle_L1)
angle_L2_rad = np.radians(angle_L2)
angle_L3_rad = np.radians(angle_L3)

# Create rotation matrices for each link angle for 2D rotation
rotMat_L1 = np.array([[np.cos(angle_L1_rad), -np.sin(angle_L1_rad)],
                      [np.sin(angle_L1_rad), np.cos(angle_L1_rad)]])

rotMat_L2 = np.array([[np.cos(angle_L2_rad), -np.sin(angle_L2_rad)],
                      [np.sin(angle_L2_rad), np.cos(angle_L2_rad)]])

rotMat_L3 = np.array([[np.cos(angle_L3_rad), -np.sin(angle_L3_rad)],
                      [np.sin(angle_L3_rad), np.cos(angle_L3_rad)]])

# Multiply the rotation matrices with the link vectors
link1_rotated = rotMat_L1 @ link1
link2_rotated = rotMat_L2 @ link2
position_link2 = link1_rotated + link2_rotated
link3_rotated = rotMat_L3 @ link3
position_link3 = position_link2 + link3_rotated





# Plotting the robot arm
plt.figure(figsize=(8, 8))

# Plot each link
plt.plot([0, link1_rotated[0]], [0, link1_rotated[1]], label='Link 1', color='b', linewidth=3)
plt.plot([link1_rotated[0], position_link2[0]], [link1_rotated[1], position_link2[1]], label='Link 2', color='g', linewidth=3)
plt.plot([position_link2[0], position_link3[0]], [position_link2[1], position_link3[1]], label='Link 3', color='r', linewidth=3)

# Mark the joints (origin and link endpoints)
plt.scatter([0, link1_rotated[0], position_link2[0], position_link3[0]],
            [0, link1_rotated[1], position_link2[1], position_link3[1]], color='k', zorder=5)


plt.text(0, 0, 'Origin', fontsize=12, ha='right')
plt.text(link1_rotated[0], link1_rotated[1], 'Joint 1', fontsize=12, ha='right')
plt.text(position_link2[0], position_link2[1], 'Joint 2', fontsize=12, ha='right')
plt.text(position_link3[0], position_link3[1], 'End Effector', fontsize=12, ha='right')

# Set plot limits
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Set aspect ratio to make it equal
plt.gca().set_aspect('equal', adjustable='box')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2d-arm-visualization')

# Show grid
plt.grid(True)
# Add legend
plt.legend()
# Show the plot
plt.show()