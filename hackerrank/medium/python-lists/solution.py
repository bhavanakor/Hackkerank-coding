if __name__ == '__main__':
    N = int(input())
    a = []  # Initialize your empty list
    
    # Loop N times to process each command line
    for _ in range(N):
        # Read the line and split by spaces
        parts = input().split()
        command = parts[0]
        
        # Check which command it is and execute it
        if command == "insert":
            index = int(parts[1])
            element = int(parts[2])
            a.insert(index, element)
            
        elif command == "print":
            print(a)
            
        elif command == "remove":
            element = int(parts[1])
            a.remove(element)
            
        elif command == "append":
            element = int(parts[1])
            a.append(element)
            
        elif command == "sort":
            a.sort()
            
        elif command == "pop":
            a.pop()
            
        elif command == "reverse":
            a.reverse()
