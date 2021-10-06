def ui_process_read_list() -> list:
    """
    Reads a list from Standard Input.

    Returns
    -------
    list:
        The list read from Standard Input.
    """
    n = int(input("Input the number of elements in the list:"))
    lst = []
    for i in range(n):
        list_element = int(input("Input element {}:".format(i)))
        lst.append(list_element)

    return lst


def ui_process_display_list(lst: list):
    """
    Displays a list to Standard Output.

    Parameters
    ----------
    lst : list
        The list to display.
    """
    for list_element in lst:
        print(list_element, end=" ")


def ui_read_command() -> int:
    """
    Reads an integer, representing a command number, from Standard Input.

    Returns
    -------
    int:
        The command number read.
    """
    return int(input("Please enter a command: "))


def ui_process_command(command: int, lst: list) -> (list, bool):
    """
    Receives a command number and processes it, eventually using the list lst.
    Returns the (possible modified) list and a bool telling whether an exit command was
    issued or not.

    Parameters
    ----------
    command : int
        The command to process, specified by a number.
    lst : list
        The list used by some of the commands.

    Returns
    -------
    list:
        The (possible modified) list.
    bool:
        True, if the command is an EXIT command; False, otherwise.
    """

    exit_command = False

    if command == 0:
        exit_command = True
    elif command == 1:
        lst = ui_process_read_list()
    elif command == 2:
        ui_process_display_list(lst)
    else:
        print("Invalid command. Please try again.")

    return lst, exit_command


def ui_loop():
    """ Reads and processes commands repeatedly until an EXIT command is received. """
    exit_command_was_received = False
    lst = []
    while not exit_command_was_received:
        ui_show_menu()
        command = ui_read_command()
        lst, exit_command_was_received = ui_process_command(command, lst)


def ui_show_menu():
    """ Displays a menu showing available commands. """
    print()
    print("Available commands:")
    print("--------------------")
    print("1. Read list")
    print("2. Display list")
    print("--------------------")
    print("0. EXIT")


def main() -> int:
    """ Entry point for the program. """
    ui_loop()

    return 1

if __name__ == "__main__":
    main()
