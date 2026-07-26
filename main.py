from core.cli import start_screen, abyss_help


def main():
    start_screen()

    while True:

        choice = input("abyss:> ").strip()

        if choice not in ["help", "q", "exit"]:
            print("Please enter a valid choice.")
            continue

        elif choice == "help":
            abyss_help()
            continue

        elif choice in ["q", "exit"]:
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()
