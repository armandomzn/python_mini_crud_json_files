import helpers
import time 
import manager


def menu():
    helpers.create_directory()
    while True:
        helpers.clear()

        print("========================")
        print("  WELCOME TO THE MANAGER  ")
        print("========================")
        print("[1] List customer's     ")
        print("[2] Show customer     ")
        print("[3] Add customer      ")
        print("[4] Modify customer   ")
        print("[5] Delete customer      ")
        print("[6] Exit               ")
        print("========================")

        option = input("> ")

        helpers.clear()

        if option == '1':
            print("Listing customers...\n")
            manager.show_all()
            
        if option == '2':
            print("Show a customer...\n")
            manager.show_customer()

        if option == '3':
            print("Add a customer...\n")
            manager.add_client()

        if option == '4':
            print("Edit a customer...\n")
            manager.edit_customer()

        if option == '5':
            print("Delete a customer...\n")
            manager.delete_customer()

        if option == '6':
            print("Exit...\n")
            time.sleep(1)
            helpers.clear()
            break

        input("\nPress Enter to continue...")