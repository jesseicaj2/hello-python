# Version 3: Interactive Greeting Options
# Intro to AI - Week 3 Assignment

def main():
    print("Hello, World!")
    print("Welcome to my first Python program.")

    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")

    print("\nChoose a greeting style:")
    print("1. Friendly")
    print("2. Professional")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print(f"Hey {name}! Hope you're having a great day!")
    elif choice == "2":
        print(f"Good day, {name}. It is a pleasure to meet you.")
    else:
        print("Invalid choice. Please select 1 or 2 next time.")

if __name__ == "__main__":
    main()
