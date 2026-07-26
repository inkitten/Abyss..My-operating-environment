from core.cli import start_screen, abyss_help


def main():
    start_screen()

    while True:
        print("1. help")
        print("2. exit")

        choice = input("Enter your choice: ").strip()

        if choice not in ["1", "2"]:
            print("Please enter a valid choice.")
            continue

        elif choice == "1":
            abyss_help()
            continue

        elif choice == "2":
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()