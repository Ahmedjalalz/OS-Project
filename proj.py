# Initial memory blocks
initial_memory_blocks = [100, 500, 200, 300, 600]
memory_blocks = initial_memory_blocks.copy()  # This will be updated over time

# Function to display current memory blocks
def display_memory_blocks():
    print("\nCurrent memory blocks:")
    for i, size in enumerate(memory_blocks):
        print(f"Block {i}: {size} MB")

# First Fit Allocation
def first_fit(p):
    print("\nFirst Fit Allocation:")
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= p:
            print(f"Process {p} -> Block {i} (Size: {memory_blocks[i]} MB)")
            memory_blocks[i] -= p  # Update memory block
            return
    print(f"Process {p} -> Not allocated")

# Best Fit Allocation
def best_fit(p):
    print("\nBest Fit Allocation:")
    best = -1
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= p:
            if best == -1 or memory_blocks[i] < memory_blocks[best]:
                best = i
    if best != -1:
        print(f"Process {p} -> Block {best} (Size: {memory_blocks[best]} MB)")
        memory_blocks[best] -= p
    else:
        print(f"Process {p} -> Not allocated")

# Worst Fit Allocation
def worst_fit(p):
    print("\nWorst Fit Allocation:")
    worst = -1
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= p:
            if worst == -1 or memory_blocks[i] > memory_blocks[worst]:
                worst = i
    if worst != -1:
        print(f"Process {p} -> Block {worst} (Size: {memory_blocks[worst]} MB)")
        memory_blocks[worst] -= p
    else:
        print(f"Process {p} -> Not allocated")

# ------------------- MAIN LOOP -------------------
print("Welcome to the Memory Allocation Simulator!")
display_memory_blocks()

while True:
    try:
        # Ask for new process size
        process_size = int(input("\nEnter size of the process: "))

        # Show allocation for all strategies
        first_fit(process_size)
        best_fit(process_size)
        worst_fit(process_size)

        # Show updated memory blocks
        display_memory_blocks()

        # Ask user to continue or end
        choice = input("\nDo you want to add another process? (y/n): ").strip().lower()
        if choice != "y":
            print("Exiting the simulator. Goodbye!")
            break

    except ValueError:
        print("Please enter a valid number.")
