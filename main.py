from typing import Optional, Tuple


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

    # 2 and 3 are primes
    if (n == 2) or (n ==3):
        return True

    # all even numbers > 2 are NOT primes
    if n % 2 == 0:
        return False

    # for odd numbers > 2, we only check odd divisors
    for d in range(3, (n // 2) + 1 , 2):
        if n % d == 0:
          return False

    # no divisor was found, so the number must be a prime
    return True


def is_palindrome(n: int) -> bool:
    """
    Finds whether a given natural number is a palindrome.

    Parameters
    ----------
    n : int
        The natural number for which we want to know whether it is a palindrome or not.

    Returns
    -------
        True, if the given number is a palindrome ; False, otherwise.
    """
    # we build the mirrored number
    original_n = n
    mirrored_n = 0
    while n > 0:
        mirrored_n = mirrored_n * 10 + n % 10
        n = n // 10

    # the given number is a palindrome iff the number equals its mirrored number.
    return mirrored_n == original_n


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


def get_goldbach(n: int) -> Optional[Tuple[int, int]]:
    """
    Finds whether a given natural number can be written as the sum of two primes, returning a decomposition in which the
    first prime is the lowest possible (and hence, the second is the largest possible) if it exists, or reports if no
    such decomposition exists.

    Parameters
    ----------
    n : int
        The natural number we are trying to write as a sum of two primes.

    Returns
    -------
    An (int, int) tuple representing two primes which add up to n (such that the first one is the lowest possible),
    if they exist ; None, otherwise.
    """

    # We only consider natural numbers. The numbers 1, 2 and 3 cannot be decomposed as the sum of two primes.
    if n <= 3:
        return None

    # OPTIMIZATION: If n = p1 + p2, where n is odd and p1, p2 are primes, then one of p1, p2 must be even, so must be 2.
    # So, when n is odd, it is enough to test whether (n-2) is a prime, as no other possible decompositions
    # exist, except for (2, n-2) (and (n-2, 2)).
    if n % 2 == 1:
        if is_prime(n - 2):
            return 2, n - 2

    # When n is even, we find each prime p1 from 2 up to n-2 and for each, we test whether n - p1 is also a prime.
    # If yes, the pair (p1, p2) is what we want, and we stop.
    for p1 in range(2, n - 1):
        if is_prime(p1):
            p2 = n - p1
            if is_prime(p2):
                return p1, p2

    return None


def test_get_largest_prime_below():
    """ Unit tests for the get_largest_prime_below(int) function. """
    assert get_largest_prime_below(0) == -1
    assert get_largest_prime_below(1) == -1
    assert get_largest_prime_below(2) == -1
    assert get_largest_prime_below(-5) == -1

    assert get_largest_prime_below(7) == 5
    assert get_largest_prime_below(103) == 101


def test_is_palindrome():
    """ Unit tests for the is_palindrome(int) function. """
    assert is_palindrome(-1) == False
    assert is_palindrome(1) == True
    assert is_palindrome(0) == True
    assert is_palindrome(1551) == True
    assert is_palindrome(2335) == False


def test_get_goldbach():
    """ Unit tests for the get_goldbach(int) function. """
    assert get_goldbach(-5) == None
    assert get_goldbach(0) == None
    assert get_goldbach(1) == None
    assert get_goldbach(2) == None
    assert get_goldbach(3) == None
    assert get_goldbach(4) == (2, 2)
    assert get_goldbach(10) == (3, 7)
    assert get_goldbach(39) == (2, 37)
    assert get_goldbach(98) == (19, 79)


def run_tests():
    """ Runs all unit tests and prints a message if they are successful. """
    test_get_largest_prime_below()
    test_is_palindrome()
    test_get_goldbach()

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
    """
    Reads an integer from Standard Input and displays the largest prime smaller than it, or a message if it does
    not exist.
    """
    n = int(input("Input an integer: "))
    largest_prime_below_n = get_largest_prime_below(n)
    if largest_prime_below_n == -1:
        # such prime does not exist
        print("There is no prime below {}.".format(n))
    else:
        print("The largest prime below {} is {}.".format(n, largest_prime_below_n))


def ui_process_is_palindrome():
    """ Reads an integer from Standard Input and displays whether it is a palindrome or not. """
    n = int(input("Input an integer: "))
    if is_palindrome(n):
        print("The number {} IS a palindrome.".format(n))
    else:
        print("The number {} is NOT a palindrome.".format(n))


def ui_process_get_goldbach():
    n = int(input("Input an integer: "))
    result = get_goldbach(n)
    if result is None:
        print("The number {} cannot be decomposed as the sum of two primes.".format(n))
    else:
        p1, p2 = result
        print("The number {} can be written as the sum of the primes {} and {}.".format(n, p1, p2))


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
    elif command == 4:
        ui_process_is_palindrome()
    elif command == 5:
        ui_process_get_goldbach()
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
    print("4. Find whether a read number is a palindrome")
    print("5. Find the Goldbach decomposition of a read number.")
    print("--------------------")
    print("0. EXIT")


def main() -> int:
    """ Entry point for the program. """
    run_tests()
    ui_loop()

    return 1


if __name__ == "__main__":
    main()

