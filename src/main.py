import numpy as np

def rotate_vector(vector, angle_deg):
    """Rotate a 2D vector by angle in degrees."""
    angle_rad = np.radians(angle_deg)
    rot_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    return rot_matrix @ vector

def calculate_positions(angles, links):
    """Calculate joint positions for given angles and links."""
    cumulative_angles = np.cumsum(angles)
    positions = [np.array([0, 0])]  # origin
    
    for i, (link, angle) in enumerate(zip(links, cumulative_angles)):
        rotated_link = rotate_vector(link, angle)
        new_pos = positions[-1] + rotated_link
        positions.append(new_pos)
    
    return positions

def calculate_torques(positions, force):
    """Calculate torques at each joint for given positions and force."""
    # Torque = r × F (cross product)
    torques = []
    # Base torque (from origin to end effector)
    r_base = positions[-1] - positions[0]
    torques.append(r_base[0] * force[1] - r_base[1] * force[0])
    
    # Joint torques (relative to each joint)
    for i in range(1, len(positions)-1):
        r_joint = positions[-1] - positions[i]
        torques.append(r_joint[0] * force[1] - r_joint[1] * force[0])
    
    return torques

def run_simulation(angles, links, force, k=0.1):
    """Run the robot arm simulation with torque effects"""
    # Calculate original positions
    orig_positions = calculate_positions(angles, links)
    
    # Calculate torques at each joint
    torques = calculate_torques(orig_positions, force)
    
    # Apply torque to angles (simplified model)
    new_angles = [
        angles[0] + torques[0] * k,  # Base torque affects first joint
        angles[1] + torques[1] * k,  # Joint 1 torque affects second joint
        angles[2] + torques[2] * k   # Joint 2 torque affects third joint
    ]
    
    # Calculate new positions after torque application
    new_positions = calculate_positions(new_angles, links)
    
    return orig_positions, new_positions, torques, new_angles