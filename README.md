# 2D Robot Arm Simulation with Torque Effects

![Robot Arm Visualization](results/Robot_Arm_Simulation_with_Torque_Effects.png)

## Overview

This project simulates a 2D robotic arm with three links, demonstrating forward kinematics, torque calculations, and the arm's response to external forces. The visualization shows both the original arm configuration and its deformation under applied forces, providing an intuitive understanding of robotic arm dynamics.

## Key Features

* **Forward Kinematics**: Calculates joint positions using vector rotation and cumulative angles
* **Torque Simulation**: Computes joint torques resulting from forces applied at the end effector
* **Dynamic Visualization**: Shows original vs. torque-adjusted arm configurations
* **Comprehensive Metrics**: Displays joint angles, torque values, and force vectors
* **Interactive Simulation**: Easily modify parameters to explore different scenarios

## Enhanced Capabilities (New)

1. **Force Response Modeling**:
   - Simulates the effect of external forces on joint angles
   - Calculates torque at each joint using cross-product formulas
   - Visualizes force vectors applied at the end effector

2. **Comparative Visualization**:
   - Shows original arm configuration (solid lines)
   - Displays torque-adjusted configuration (dashed lines)
   - Differentiates joints with filled vs. hollow circles

3. **Comprehensive Metrics Display**:
   - Real-time torque values at each joint
   - Original and adjusted joint angles
   - Force magnitude and direction

## Code Structure

The project is organized into three modular files:

```
├── main.py             # Core calculation logic
├── plot.py             # Visualization functions
├── run_viz.py          # Execution script
├── results/            # Output visualizations
│   ├── Robot_Arm_Simulation.png
│   └── Robot_Arm_Simulation_with_Torque_Effects.png
└── README.md
```

### 1. main.py
Contains the core mathematical operations:
- Vector rotation using rotation matrices
- Forward kinematics position calculation
- Torque computation at each joint
- Simulation of angle changes under applied torque

### 2. plot.py
Handles visualization aspects:
- Comparative arm plotting (original vs. adjusted)
- Joint marking and labeling
- Force vector visualization
- Information boxes for torques and angles
- Custom legend creation

### 3. run_viz.py
Execution script that:
- Defines arm parameters (link lengths, joint angles)
- Specifies force vectors
- Runs the simulation
- Generates the visualization

## Results

### 1. Basic Robot Arm Simulation
![Basic Simulation](results/Robot_Arm_Simulation.png)

This visualization shows the robotic arm in its default configuration:
- Three links with lengths 3m, 2m, and 2m
- Joint angles: 70°, -30°, -45°
- Color-coded links (blue, green, red)
- Labeled joints (Base, Joint 1, Joint 2, End Effector)

### 2. Robot Arm with Torque Effects
![Torque Effects](results/Robot_Arm_Simulation_with_Torque_Effects.png)

This enhanced visualization demonstrates the arm's response to a vertical force:
- **Force Applied**: 10N downward at end effector
- **Visual Elements**:
  - Solid lines: Original arm position
  - Dashed lines: Torque-adjusted position
  - Filled circles: Original joints
  - Hollow circles: Adjusted joints
  - Purple arrow: Force vector
- **Information Boxes**:
  - Torque values at each joint
  - Original and adjusted joint angles
  - Force magnitude

## Technical Explanation

### Torque Calculation
Torque (τ) at each joint is calculated using the cross product formula:
```
τ = r × F = (x*Fy - y*Fx)
```
Where:
- `r` is the position vector from joint to end effector
- `F` is the force vector applied at end effector

### Angle Adjustment
Joint angles respond to torque through a simplified model:
```
new_angle = original_angle + τ * k
```
Where `k` is a sensitivity constant (default: 0.1)

### Forward Kinematics
Joint positions are calculated using:
```
position[i] = position[i-1] + R(θ_cumulative) @ link_vector
```
Where:
- `R(θ)` is the 2D rotation matrix
- `θ_cumulative` is the sum of all previous joint angles

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/robot-arm-simulation.git
   cd robot-arm-simulation
   ```

2. Install required packages:
   ```bash
   pip install numpy matplotlib
   ```

3. Run the simulation:
   ```bash
   python run_viz.py
   ```

4. Modify parameters in `run.py` to explore different configurations:
   ```python
   # Change link lengths
   links = [np.array([3, 0]), np.array([2, 0]), np.array([2, 0])]
   
   # Change joint angles
   angles = [70, -30, -45]
   
   # Change force vector
   F = np.array([0, -10])  # [Fx, Fy]
   
   # Adjust torque sensitivity
   k = 0.1
   ```

## Customization Options

1. **Arm Configuration**:
   - Modify link lengths in `links` array
   - Change joint angles in `angles` array
   - Adjust number of links (code supports N links)

2. **Force Application**:
   - Change force direction and magnitude
   - Apply forces at different points
   - Simulate multiple simultaneous forces

3. **Visual Settings**:
   - Modify colors in `plot.py`
   - Adjust axis limits for better framing
   - Change information box positions

## Applications

This simulation demonstrates principles relevant to:
- Robotic arm design and control
- Inverse kinematics solutions
- Force/torque analysis in mechanical systems
- Robotics education and visualization
- Path planning and obstacle avoidance

## License

This project is open source and free to use and modify under the MIT License.