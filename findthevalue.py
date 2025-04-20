# Given dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Ask user to enter a key
key = int(input("Enter a key (1 to 6): "))

# Check if key exists and print value
if key in d:
    print("The value for key", key, "is:", d[key])
else:
    print("❌ Key not found in dictionary.")
