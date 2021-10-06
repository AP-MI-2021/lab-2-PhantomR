def ui_process_read_list():
    """
    Reads a list from Standard Input.

    Returns
    -------
    list:
        The list read from Standard Input.
    """
    return list(input("Please input a list (comma separated elements): "))

def ui_read_command() -> int:
    """
    Reads an integer, representing a command number, from Standard Input.

    Returns
    -------
    int:
        The command number read.
    """
    return int(input("Please enter a command: "))


def ui_process_command(command: int, lst: list) -> bool:
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


def main():
    """ Entry point for the program. """
    ui_loop()

if __name__ == "__main__":
    main()
