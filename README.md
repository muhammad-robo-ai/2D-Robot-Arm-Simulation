# 2d-arm-visualization

## Overview
This project visualizes a 2D robotic arm with three links using Python and Matplotlib. It demonstrates how to calculate the positions of the arm's joints based on specified angles and link lengths.

## Features
- **Vector Mathematics**: Utilizes vector addition and rotation matrices for calculating joint positions.
- **Graphical Visualization**: Plots the arm's configuration, including the origin and joint positions.

## Code Explanation
1. **Link Lengths**: Defines the lengths of the three links.
2. **Angles**: Sets the angles for each link in degrees, which are then converted to radians.
3. **Rotation Matrices**: Creates rotation matrices for each link based on its angle.
4. **Position Calculation**: Computes the rotated positions of each link and the cumulative positions of the joints.
5. **Plotting**: Uses Matplotlib to visualize the arm, including links and joint labels.

## How to Run
1. Ensure you have Python installed with the NumPy and Matplotlib libraries.
2. Copy the code into a Python script or Jupyter Notebook.
3. Run the script to visualize the 2D robotic arm.

## Example Output
The output will display a graphical representation of the robotic arm with labeled joints, showing the configuration based on the specified angles and lengths.

## License
This project is open source and available for modification and use.