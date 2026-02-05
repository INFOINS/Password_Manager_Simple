def encrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) + 3)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - 3)
    return result

while True:
    print("\nPassword Manager")
    print("1. Save password")
    print("2. View passwords")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        account = input("Account name: ")
        password = input("Password: ")

        encrypted = encrypt(password)

        with open("passwords.txt", "a") as file:
            file.write(account + "|" + encrypted + "\n")

        print("Password saved!")

    elif choice == "2":
        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    account, encrypted = line.strip().split("|")
                    print(account, "->", decrypt(encrypted))
        except:
            print("No passwords saved yet.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
