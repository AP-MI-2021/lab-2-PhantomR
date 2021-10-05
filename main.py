def gui_read_command() -> int:
    """
    Reads an integer, representing a command number, from the user.
    :return:
    """
    return int(input("Please enter a command: "))


def gui_process_command(a: int) -> int:
    """

    Parameters
    ----------
    a : int
        Command number.

    Returns
    -------

    """


def gui_loop():
    """
    Reads and processes commands repeatedly.
    """
    read_another_command = True
    while read_another_command:
        gui_show_menu()
        command = gui_read_command()
        read_another_command = gui_process_command(command)


def gui_show_menu():
    print("Available commands:")
    print("1. Read list")
    print("2. Display list")
    print("--------------------")
    print("0. EXIT")


def main():
    print("test")


if __name__ == "__main__":
    main()
