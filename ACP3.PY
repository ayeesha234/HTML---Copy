import os

filename = "demo_file.txt"

# 1. Create and Write to a New File
file = open(filename, "w")
file.write("Hello! This is the first line.\n")
file.write("Here is the second line.\n")
file.close()
print("✅ File created and written.")

# 2. Read the entire file
file = open(filename, "r")
print("\n📖 Full File Contents:")
print(file.read())
file.close()

# 3. Read specific number of characters
file = open(filename, "r")
print("\n🔍 First 10 characters:")
print(file.read(10))
file.close()

# 4. Append more content to the file
file = open(filename, "a")
file.write("Appended this third line.\n")
file.close()
print("\n➕ Appended new line to file.")

# 5. Read file line by line
file = open(filename, "r")
print("\n📃 File Line by Line:")
for line in file:
    print(line.strip())
file.close()

# 6. Check if file exists
if os.path.exists(filename):
    print("\n✅ The file exists.")
else:
    print("\n❌ The file does not exist.")

# 7. Delete the file
delete = input("\nDo you want to delete the file? (yes/no): ").lower()
if delete == "yes":
    os.remove(filename)
    print("🗑️ File deleted.")
else:
    print("🚫 File not deleted.")
