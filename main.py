from core.cli import start_screen
from core.plugin_manager import run_command


def main():
    start_screen()
    while True:

        choice = input("abyss:> ").strip()
        if choice in ["q", "exit"]:
            break
        run_command(choice)

    print("Goodbye!")


if __name__ == "__main__":
    main()
