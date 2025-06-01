
# 2D Robot Arm Visualization


## Overview

This project visualizes a 2D robotic arm with three links using Python and Matplotlib. It demonstrates how to calculate the positions of the arm's joints using vector rotation and cumulative joint angles, simulating realistic forward kinematics.

## Features

* **Vector Mathematics**: Uses vector addition and rotation matrices for accurate joint position calculations.
* **Cumulative Joint Angles**: Implements forward kinematics by summing joint angles to rotate links relative to previous joints.
* **Color-coded Visualization**: Displays the robotic arm with colored links and labeled joints for easy understanding.

## Code Explanation

1. **Link Lengths**: Defines each link as a vector along the x-axis with specified lengths.
2. **Joint Angles**: Joint angles are provided in degrees and can be positive or negative to indicate direction.
3. **Cumulative Angles**: Calculates the cumulative sum of joint angles for proper rotation relative to previous joints.
4. **Rotation Function**: Rotates each link vector using a rotation matrix based on cumulative angles.
5. **Joint Position Calculation**: Computes joint positions by sequentially adding rotated vectors.
6. **Visualization**: Plots colored links, marks joint positions with dots, and labels each joint for clarity.

## How to Run

1. Install Python 3.x if not already installed.
2. Install required packages using pip:

   ```bash
   pip install numpy matplotlib
   ```
3. Place the script (`main.py`) inside the `src/` directory (if following the suggested repo structure).
4. Run the script:

   ```bash
   python src/main.py
   ```
5. The program will open a window displaying the 2D robotic arm configuration based on the specified link lengths and joint angles.

## Example Output

A graphical plot of a three-link robotic arm with blue, green, and red colored links, showing labeled joints including the origin, joints 1 and 2, and the end effector.


## License

This project is open source and free to use and modify under the MIT License.

