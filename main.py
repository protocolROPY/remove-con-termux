import subprocess
import json
def removeStartWith(start):
    contacts_output = subprocess.check_output(["termux-contact-list"])
    contacts = json.loads(contacts_output)
    for contact in contacts:
        name = contact["name"]
        if name.startswith(start):
            print(str(contact["name"]))
    print("\n")
    makeSure = input("Are you sure😨[Y/N]? ")
    if makeSure.lower() == "y":
        for contact in contacts:
            name = contact["name"]
            if name.startswith(start):
                    subprocess.call(["termux-contact-remove", str(contact["name"])])
    else:
        print("😅bye HHHOOO !")

if __name__ == "__main__":
    subprocess.call(["clear"])
    sw = input("Enter name or start-With you want to remove: ")
    removeStartWith(sw)