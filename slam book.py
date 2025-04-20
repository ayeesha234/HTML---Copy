import sys

def initial_slambook():
    row = int(input("Enter the number of people that will be answering the questions: "))
    cols = 5

    slam_book = []

    for i in range(row):
        print("\nEnter contact %d details in the following order (ONLY): " % (i + 1))
        print("NOTE: * indicates mandatory fields")
        print("..................................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                name = input("Enter name: ")
                if name.strip() == '':
                    sys.exit("Name is a mandatory field. Processing exit due to blank field...")
                temp.append(name)

            elif j == 1:
                temp.append(input("Enter age: "))

            elif j == 2:
                hobby = input("Enter your hobbies: ")
                temp.append(hobby if hobby.strip() != '' else None)

            elif j == 3:
                favs = input("Enter your favorite color, animal, number, sport, B.F.F, and grade: ")
                temp.append(favs if favs.strip() != '' else None)

            elif j == 4:
                opinion = input("Enter something you hate and like about the person who made this slambook: ")
                temp.append(opinion if opinion.strip() != '' else None)

        slam_book.append(temp)

    print("\nCollected Slam Book Entries:")
    for entry in slam_book:
        print(entry)

    return slam_book


def thanks():
    print("***********************************************************************************")
    print("Thank you for checking out the slam book")
    print("Please visit again!")
    print("***********************************************************************************")
    sys.exit("Goodbye, have a nice day!")


def instructions():
    print("..................................................................................")
    print("\t\tHOW TO USE A SLAM BOOK:")
    print("It's simple! I will have questions written in this book.")
    print("Answer them, once you're done give it to your friend.")
    print("They will keep repeating the same process again. Have Fun!!!")
    print("..................................................................................")


def menu():
    print("***********************************************************************************")
    print("\t\t\t\tSLAM BOOK DIRECTORY")
    print("***********************************************************************************")
    print("\tYou can now perform the following operations in this slam book\n")
    print("1. Answer questions")
    print("Other number. Exit slambook")
    choice = int(input("Please enter your choice: "))
    return choice


def main():
    print("..................................................................................")
    print("Hello dear friend, welcome to my slam book")
    print("You may now proceed to explore my slam book")
    print("..................................................................................")

    instructions()

    while True:
        choice = menu()
        if choice == 1:
            _ = initial_slambook()
        else:
            thanks()


main()
