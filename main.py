import subprocess
import json
def removeStartWith(start):
    contacts_output = subprocess.check_output(["termux-contact-list"])
    contacts = json.loads(contacts_output)

    for contact in contacts:
        name = contact["name"]
        if name.startswith(start):
            print(str(contact["name"]))
            # subprocess.call(["termux-contact-remove", str(contact["id"])])

if __name__ == "__main__":
    subprocess.call(["clear"])
    sw = input("Enter name or start-With you want to remove: ")
    makeSure = input("Are you sure😨[Y/N]? ")
    if makeSure.lower() == "y":
        removeStartWith(sw)