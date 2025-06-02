import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot_robot(orig_positions, new_positions, torques, angles, new_angles, force):
    """Visualize the robot arm with torque effects"""
    # Extract coordinates for plotting
    orig_x = [pos[0] for pos in orig_positions]
    orig_y = [pos[1] for pos in orig_positions]
    new_x = [pos[0] for pos in new_positions]
    new_y = [pos[1] for pos in new_positions]
    
    # Create figure
    plt.figure(figsize=(12, 10))
    ax = plt.gca()
    
    # Plot original arm (solid lines)
    colors = ['blue', 'green', 'red']
    for i in range(len(orig_positions)-1):
        # Original arm
        ax.plot([orig_x[i], orig_x[i+1]], [orig_y[i], orig_y[i+1]], 
                color=colors[i], linewidth=3.5, linestyle='-', 
                label=f'Link {i+1} (Original)')
        
        # Torque-adjusted arm
        ax.plot([new_x[i], new_x[i+1]], [new_y[i], new_y[i+1]], 
                color=colors[i], linewidth=3.5, linestyle='--', alpha=0.8,
                label=f'Link {i+1} (After Torque)')
    
    # Mark joints for both configurations
    for i, (x, y) in enumerate(zip(orig_x, orig_y)):
        # Original joints (filled)
        ax.scatter(x, y, s=120, color=colors[min(i, len(colors)-1)], edgecolor='k', zorder=5)
        
        # Torque-adjusted joints (hollow)
        if i < len(new_x):
            ax.scatter(new_x[i], new_y[i], s=100, facecolor='none', 
                       edgecolor=colors[min(i, len(colors)-1)], linewidth=2, zorder=5)
    
    # Add force vector
    force_color = 'darkviolet'
    ax.quiver(orig_x[-1], orig_y[-1], force[0], force[1], 
              scale=30, width=0.008, color=force_color,
              label=f'Force: (0, {force[1]} N)')
    
    # Add annotations
    joint_labels = ['Base', 'Joint 1', 'Joint 2', 'End Effector']
    for i, (x, y, label) in enumerate(zip(orig_x, orig_y, joint_labels)):
        offset_x = 0.35 if i > 0 else 0.1
        offset_y = 0.35 if i != 3 else -0.45
        ax.annotate(label, (x, y), xytext=(x + offset_x, y + offset_y),
                    fontsize=12, ha='center', 
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.8))
    
    # Add torque information
    torque_text = "\n".join([
        f"Base Torque: {torques[0]:.2f} N·m",
        f"Joint 1 Torque: {torques[1]:.2f} N·m",
        f"Joint 2 Torque: {torques[2]:.2f} N·m"
    ])
    ax.text(0.05, 0.95, torque_text, transform=ax.transAxes,
            fontsize=12, verticalalignment='top', 
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Add angle information
    angle_text = (
        f"Original Angles: {angles[0]}°, {angles[1]}°, {angles[2]}°\n"
        f"New Angles: {new_angles[0]:.1f}°, {new_angles[1]:.1f}°, {new_angles[2]:.1f}°"
    )
    ax.text(0.05, 0.05, angle_text, transform=ax.transAxes,
            fontsize=12, bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    
    # Set plot properties
    ax.set_xlim(-1, 8)
    ax.set_ylim(-5, 6)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlabel('X Position (m)', fontsize=12)
    ax.set_ylabel('Y Position (m)', fontsize=12)
    ax.set_title('Robot Arm Simulation with Torque Effects', fontsize=16, pad=20)
    
    # Create custom legend
    legend_elements = [
        Line2D([0], [0], color='blue', lw=3, linestyle='-', label='Original Arm'),
        Line2D([0], [0], color='blue', lw=3, linestyle='--', label='After Torque'),
        Line2D([0], [0], marker='o', markersize=8, 
               markerfacecolor='blue', markeredgecolor='k', label='Original Joint'),
        Line2D([0], [0], marker='o', markersize=8, 
               markerfacecolor='none', markeredgecolor='blue', label='New Joint'),
        Line2D([0], [0], color=force_color, lw=2, label='Force Vector')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right', fontsize=11)
    
    plt.tight_layout()
    plt.show()