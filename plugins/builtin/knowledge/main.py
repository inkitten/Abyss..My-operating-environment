import toml
import pathlib as pl


def config_file():
    try:
        with open("./plugins/builtin/knowledge/config.toml", "r") as f:
            config = toml.load(f)
    except FileNotFoundError:
        print("config file not found")
        return None
    return config


def add_note(main_path, name):
    note_path = main_path / f"{name}.md"
    try:
        note_path.touch(exist_ok=False)
    except FileExistsError:
        print("note already exists")
        return


def remove_note(main_path, name):
    note_path = main_path / f"{name}.md"
    print(note_path)
    try:
        note_path.unlink(missing_ok=False)
    except FileNotFoundError:
        print("Note dose not exists")
        return


def view_notes(main_path):
    items_list = list(main_path.glob("*"))
    for i in items_list:
        print(i)
    print("\n")


def main():
    config = config_file()
    # def_path = config.get("main").get("path")
    def_path = config["main"]["path"]
    if not def_path:
        print("Please enter a path for nots")
        def_path = input("path: ")
        config["main"]["path"] = def_path
        with open("config.toml", "w") as f:
            toml.dump(config, f)
    main_path = pl.Path(def_path)
    path = main_path / "Abyss_notes"
    (path).mkdir(exist_ok=True)
    while True:
        print("welcome to Notes module.")
        print("Please choose one of the following options:")
        print("1.Add Note")
        print("2.Remove Note")
        print("3.View Notes")
        print("4.Exit")
        choice = input("> ").strip()
        if not choice in ("1", "2", "3", "4"):
            print("please choose a valid option")
            continue
        elif choice == "1":
            add_note(path, input("Note Name: "))
        elif choice == "2":
            remove_note(path, input("Note Name:"))
        elif choice == "3":
            view_notes(path)
        elif choice == "4":
            print("Thank you for using Notes module")
            break


if __name__ == "__main__":
    main()
