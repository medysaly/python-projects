while True:
    user_input = int(input(" choose an option:\n1. Write a note\n2. View notes\n3. Delete a note\n4. Exit\n"))
    if user_input == 1:
        note = input ("Write your note: ")
        with open ("notes.txt", "a") as file:
            file.write(note + "\n")

    elif user_input == 2:
        with open("notes.txt", "r") as file:
            lines = file.readlines()
            if lines == []:
                print("No notes found.")
            else:
                for index, line in enumerate(lines, start=1):
                    print(f"{index}. {line.strip()}")

    elif user_input == 3:
        with open("notes.txt", "r") as file:
            lines = file.readlines()
            if lines == []:
                print("No notes to delete.")
            else:
                for index, line in enumerate(lines, start=1):
                    print(f"{index}. {line.strip()}")
                note_to_delete = int(input("Enter the number of the note you want to delete: "))
                if 1 <= note_to_delete <= len(lines):
                    del lines[note_to_delete - 1]
                    with open("notes.txt", "w") as file:
                        file.writelines(lines)
                    print("Note deleted.")
                else:
                    print("Invalid note number.")
    elif user_input == 4:
        print("Exiting the notes app.")
        break
  
        
    
