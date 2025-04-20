# Reading the full contents of the file
file = open("Codingal.txt", "r")
print("Full File Contents:\n")
print(file.read())
file.close()

# Reading the first 8 characters
file = open("Codingal.txt", "r")
print("\nFirst 8 characters of the file:\n")
print(file.read(8))
file.close()

# Appending a name and age to the file
file = open("Codingal.txt", "a")
file.write("\nHi! I am Penguin and I am 1 yr old.")
file.close()
