# Function to check Disarium number
def is_disarium(number):
    total = 0
    num_str = str(number)
    for i in range(len(num_str)):
        digit = int(num_str[i])
        total += digit ** (i + 1)
    return total == number

# Get input from the user
num = int(input("Enter a number: "))

# Check and display result
if is_disarium(num):
    print(num, "is a Disarium number.")
else:
    print(num, "is NOT a Disarium number.")
