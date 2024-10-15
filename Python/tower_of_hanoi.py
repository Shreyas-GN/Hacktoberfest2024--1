def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, target, source)

# Test the tower_of_hanoi function
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')  # Solve Tower of Hanoi with 3 disks
