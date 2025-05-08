🧠 Memory Allocation Simulator
This project simulates three dynamic memory allocation strategies—First Fit, Best Fit, and Worst Fit—for assigning processes to memory blocks. It's designed as a simple CLI (command-line interface) tool to help understand how different allocation strategies behave in a system with limited memory.

📂 Features
Displays current available memory blocks

Accepts user input for process size

Applies First Fit, Best Fit, and Worst Fit algorithms

Updates memory state after each allocation

Handles invalid input gracefully

Loop control for multiple simulations

🛠 How It Works
The program initializes with a fixed set of memory block sizes.

The user enters the size of a new process.

The program attempts to allocate the process using:

First Fit: Finds the first block that fits.

Best Fit: Finds the smallest block that fits.

Worst Fit: Finds the largest block that fits.

The memory block list is updated, and the new state is shown.

The user can continue adding processes or exit.

▶️ Getting Started
Prerequisites
Python 3.x installed
