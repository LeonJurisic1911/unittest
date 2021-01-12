class Device:
    def __init__(self, pc_name, system, user):
        self.pc_name = pc_name
        self.system = system
        self.user = user

    def __str__(self):
        return f"{self.pc_name}, {self.system}, {self.user}"


class Workstation(Device):
    pass


class Laptop(Device):
    pass


class Macbook(Device):
    pass


operation_systems = ["Windows 10", "Windows 7", "Linux"]

devices = []


def name_check(eingabe, registry_or_change):
    for x in devices:
        if x.pc_name in eingabe:
            input("This name is already taken or not valid. Press Enter to try another one.")
            if registry_or_change == "registry":
                registry()
            elif registry_or_change == "change":
                change()
        else:
            pass
    if eingabe == "" or eingabe == " ":
        input("You need to write something!\nPress Enter to Continue")
        if registry_or_change == "registry":
            registry()
        elif registry_or_change == "change":
            search()
    else:
        pass


def os_check(eingabe, registry_or_change):
    if eingabe in operation_systems:
        for os in operation_systems:
            if os == eingabe:
                clear()
                print("OS:", eingabe)
                input("Press Enter to continue")
    else:
        input("OS hasn't been found.. Press Enter")
        if registry_or_change == "registry":
            registry()
        elif registry_or_change == "change":
            search()


def user_check(eingabe, registry_or_change):
    if eingabe == "" or eingabe == " ":
        input("You need to write something! Press Enter")
        if registry_or_change == "registry":
            registry()
        elif registry_or_change == "change":
            search()


def clear():
    for clearing in range(50):
        print(" ")


def what_do_you_want():
    clear()
    choice = input("What do you want to do? \nRegister \nSearch\nChange\n> ")
    if choice == "register" or choice == "Register":
        registry()
    elif choice == "search" or choice == "Search":
        search()
    elif choice == "change" or choice == "Change":
        change()
    else:
        input("Didn't understand that.. Press Enter to continue")

        what_do_you_want()


def registry():
    clear()
    device_choice = input("Register Device (Type exit to go back to menu)\n ---------------- \n"
                          "What kind of computer do you have? \n| ws | laptop | mac |\n> ")
    if device_choice == "ws" or device_choice == "workstation" or device_choice == "WS":
        clear()
        ws_name = input("Workstation Name \n> ")
        name_check(ws_name, "registry")
        clear()
        # os registry
        for x in operation_systems:
            print(x)
        ws_os = input("Workstation OS [First letter is always Capital] \n> ")
        os_check(ws_os, "registry")
        clear()
        ws_user = input("Workstation User \n> ")
        user_check(ws_user, "registry")
        ws = Workstation(ws_name, ws_os, ws_user)
        devices.append(ws)
        print(devices[-1])
        choice = input("Do you want to register another device? Type yes or no\n> ")
        if choice == "yes":
            registry()
        elif choice == "no":
            what_do_you_want()
        else:
            input("Didn't understand that.. Sending you back to menu, press Enter")
            what_do_you_want()

    # laptop registry
    elif device_choice == "laptop":
        clear()
        lap_name = input("Laptop Name\n> ")
        name_check(lap_name, "registry")
        clear()
        for x in operation_systems:
            print(x)
        lap_os = input("Laptop OS [First letter is always Capital]\n> ")
        os_check(lap_os, "registry")
        clear()
        lap_user = input("Laptop user\n> ")
        user_check(lap_user, "registry")
        clear()
        laptop = Laptop(lap_name, lap_os, lap_user)
        devices.append(laptop)
        print(devices[-1])
        choice = input("Do you want to register another device? Type yes or no\n> ")
        if choice == "yes":
            registry()
        elif choice == "no":
            what_do_you_want()
        else:
            input("Didnt understand that.. Sending you back to menu, press Enter")

    # mac registry
    elif device_choice == "mac":
        clear()
        mac_name = input("Mac Name\n> ")
        name_check(mac_name, "registry")
        clear()
        input("Operation System: Mac-OS\n Press Enter to continue")
        mac_os = "Mac-OS"
        clear()
        mac_user = input("Mac user\n> ")
        user_check(mac_user, "registry")
        mac = Workstation(mac_name, mac_os, mac_user)
        devices.append(mac)
        print(devices[-1])
        choice = input("Do you want to register another device? Type yes or no\n> ")
        if choice == "yes":
            registry()
        elif choice == "no":
            what_do_you_want()
        else:
            input("Didn't understand that.. Sending you back to menu, press Enter")
    elif device_choice == "exit" or device_choice == "Exit":
        what_do_you_want()
    else:
        input("Didn´t understand that.. Press enter")
        registry()


def search():
    clear()
    user_search = input("Type in the username you are looking for, or type 'exit' to go back to menu\n> ")
    for x in devices:

        if user_search == x.user:
            clear()
            print(x.pc_name, ",", x.system, ",", x.user)
            sec_choice = input("Do you want to search for more devices with the same username? Type 'yes' for search,\n"
                               "or 'no' to get back to the search function\n>")
            if sec_choice == "no" or sec_choice == "No":
                clear()
                input("Going back to search. Press Enter..")
                search()
            elif sec_choice == "yes" or sec_choice == "Yes":
                clear()
                if user_search != x.user:
                    input("User hasn't been found.. Press Enter to continue")

    if user_search == "Exit" or user_search == "exit":
        clear()
        input("Going back to menu.. Press Enter")
        what_do_you_want()
    else:
        clear()
        input("Nothing found.. Press Enter to get back to search function")
        search()


def change():
    clear()
    user_search = input("Type in the username you are looking for, or type 'exit' to go back to menu \n>")
    if user_search == "exit" or user_search == "Exit":
        what_do_you_want()
    for x in devices:
        if user_search == x.user:
            clear()
            print(x.pc_name, ",", x.system, ",", x.user)

            while True:
                clear()
                next_choice = input(
                    f"Profile: {x}\nWhat do you want to change?\n-----------\nPC-Name[Type 'Name']\nUsername[User]"
                    " \nOS[OS]\nOr do you want to quit[Quit] the change function?\n> ")

                if next_choice == "name" or next_choice == "Name":
                    clear()
                    print("Current PC-Name:", x.pc_name)
                    new_pc_name = input(f"\n--------\nChange the PC Name:\n> ")
                    name_check(new_pc_name, "change")
                    x.pc_name = new_pc_name
                    clear()
                    print(f"Profile has been changed: {x.pc_name, x.system, x.user}\nPress Enter to continue")

                elif next_choice == "User" or next_choice == "user":
                    clear()
                    new_user = input(f"Change the PC User:\n> ")
                    user_check(new_user, "change")
                    x.user = new_user
                    clear()
                    print(f"Profile has been changed: {x.pc_name, x.system, x.user}\nPress Enter to continue")

                elif next_choice == "OS" or next_choice == "os":
                    clear()
                    print(operation_systems)
                    new_os = input(f"Current OS: {x.system}\nChange the PC OS:\n> ")
                    if x.system == "Mac-OS":
                        input("You can't change a Macbook's operation system. Press Enter")
                    os_check(new_os, "change")
                    x.system = new_os
                    clear()
                    print(f"Profile has been changed: {x.pc_name, x.system, x.user}\nPress Enter to continue")

                elif next_choice == "quit" or next_choice == "Quit":
                    clear()
                    change()
                    break
                else:
                    clear()
                    input("Didn't understand that.. Press Enter and try again")
                    search()


what_do_you_want()
