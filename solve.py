def hanoi(n, source, target, auxiliary):
    """
    Solves the Hanoi Tower problem with n discs between three sticks.
    
    Args:
    n (int): Number of disks.
    source (str): Source stick.
    target (str): Target stick.
    auxiliary (str): Auxiliary stick.
    """
    if n > 0:
        # Moves n-1 disks from source to auxiliary, through target
        hanoi(n-1, source, auxiliary, target)
        
        # Moves the remaining disk from source to target
        print(f"{source} -> {target}")
        
        # Moves n-1 disks from auxiliary to target, through source
        hanoi(n-1, auxiliary, target, source)

# Main function to read user input and call hanoi function
def main():
    # Read user entry
    input_str = input("Enter the number of disks followed by the number of sticks separated by a comma: ")
    disks, pegs = map(int, input_str.split(','))
    
    # Call hanoi function with appropriate settings
    hanoi(disks, '1', '2', '3')

if __name__ == "__main__":
    main()