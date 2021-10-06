def is_prime(n):
    """
    Tests whether an integer is a prime number.

    Parameters
    ----------
    n : int
        The natural number whose primality we want to test.

    Returns
    -------
        True if and only if n is a prime.
    """
    # 0 and 1 are not primes, by definition
    if (n == 0) or (n == 1):
        return False

    # 2 is a prime
    if (n == 2):
        return True

    # for numbers > 2, we can start checking divisors from 2 up to number / 2 (inclusive because of number 4)
    for d in range(2, (n // 2) + 1 , 2):
        if n % d == 0:
          return False

    # no divisor was found, so the number must be a prime
    return True


def get_largest_prime_below(n: int) -> int:
    """
    Finds the largest prime number smaller than a given number, if it exists.
    Returns -1 if the number does not exist.

    Parameters
    ----------
    n : int
        The number whose largest smaller prime we are looking for.

    Returns
    -------
    int:
        The value of the largest prime smaller than n, if it exists ; -1, if it does not exist.
    """
    # we check the primality of the numbers smaller than n in decreasing order
    for number in range(n - 1, 1, -1):
        if is_prime(number):
            return number

    # we were unable to find such prime
    return -1


def test_get_largest_prime_below():
    """ Unit tests for the get_largest_prime_below(int) function. """
    assert get_largest_prime_below(0) == -1
    assert get_largest_prime_below(1) == -1
    assert get_largest_prime_below(2) == -1
    assert get_largest_prime_below(-5) == -1

    assert get_largest_prime_below(7) == 5
    assert get_largest_prime_below(103) == 101


def run_tests():
    """ Runs all unit tests and prints a message if they are successful. """
    test_get_largest_prime_below()

    print("\n[TEST] All tests passed, yay!\n")


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


def ui_read_command() -> int:
    """
    Reads an integer, representing a command number, from Standard Input.

    Returns
    -------
    int:
        The command number read.
    """
    return int(input("Please enter a command: "))


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


def ui_process_find_largest_prime_below():
    """ Reads an integer from Standard Input and displays the largest prime smaller than it, or a message if it does not exist. """
    n = int(input("Input an integer: "))
    largest_prime_below_n = get_largest_prime_below(n)
    if largest_prime_below_n == -1:
        # such prime does not exist
        print("There is no prime below {}.".format(n))
    else:
        print("The largest prime below {} is {}.".format(n, largest_prime_below_n))


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
    elif command == 3:
        ui_process_find_largest_prime_below()
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
    print("3. Find largest prime below a read number")
    print("--------------------")
    print("0. EXIT")


def main() -> int:
    """ Entry point for the program. """
    run_tests()
    ui_loop()

    return 1

if __name__ == "__main__":
    main()
