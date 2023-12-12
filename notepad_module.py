# Francisco Sanchez
# 12/02/23

import os


def display_notes(notes):
    print("\n===== Your Notes =====")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
    print("======================\n")


def add_note(notes):
    new_note = input("Enter your new note: ")
    notes.append(new_note)
    print("Note added successfully!\n")


def delete_note(notes):
    display_notes(notes)
    try:
        index = int(input("Enter the number of the note you want to delete: "))
        if 1 <= index <= len(notes):
            deleted_note = notes.pop(index - 1)
            print(f"Note '{deleted_note}' deleted successfully!\n")
        else:
            print("Invalid note number. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")


def save_notes(notes, filename="notes.txt"):
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")


def load_notes(filename="notes.txt"):
    notes = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            notes = [line.strip() for line in file.readlines()]
    return notes


def main():
    notes_filename = "notes.txt"
    notes = load_notes(notes_filename)

    while True:
        print("===== Notepad Menu =====")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Exit")
        print("--------------------------------------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_notes(notes)
        elif choice == "2":
            add_note(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            save_notes(notes, notes_filename)
            print("Exiting Notepad. Your notes are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()
