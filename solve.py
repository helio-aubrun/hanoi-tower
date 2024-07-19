class hanoi:

    def __init__(self):
        self.path = []

    def hanoi_solve(self, n, source, target, auxiliary):
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
            self.hanoi_solve(n-1, source, auxiliary, target)
            
            # Moves the remaining disk from source to target
            print(f"{source} -> {target}")
            self.path.append([int(source),int(target)])
            
            # Moves n-1 disks from auxiliary to target, through source
            self.hanoi_solve(n-1, auxiliary, target, source)
        

    # Main function to read user input and call hanoi function
    def main(self):
        # Read user entry
        input_str = "5,3" #input("Enter the number of disks followed by the number of sticks separated by a comma: ")
        disks, pegs = map(int, input_str.split(','))
        
        # Call hanoi function with appropriate settings
        self.hanoi_solve(disks, '1', '2', '3')

if __name__ == "__main__":
    main = hanoi()
    main.main()
    print (main.path)