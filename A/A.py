from bisect import bisect_right


def input_int():
    """
    Allows you to enter integer from console.

    Returns:
        int: entered integer

    Raises:
        ValueError: If the number entered does not correspond to the condition (1 <= value <= 200000)
            or if the entered value is not integer.
    """

    value = int(raw_input())
    if not check_integer(value):
        raise ValueError

    return value


def input_dish_prices():
    """
    Allows you to enter the number of dishes and price for each dish from console.

    Returns:
        list: the sorted list of entered prices

    Raises:
        ValueError: If some number entered does not correspond to the condition (1 <= value <= 200000)
            or if some entered value is not integer.
    """

    # entering number of dishes
    dish_count = input_int()

    # entering prices of dishes
    prices = list(map(int, raw_input().split(' ')))
    prices.sort()

    # if the number of prices is not equal to the number of dishes and
    # if the price range is incorrect, then raise exception
    if len(prices) != dish_count or \
       prices and not check_integer(prices[0]) or \
       prices and not check_integer(prices[-1]):
        raise ValueError

    return prices


def input_amounts():
    """
    Allows you to enter the number of days and amount for each day from console.

    Returns:
        list: the list of entered amounts

    Raises:
        ValueError: If some number entered does not correspond to the condition (1 <= value <= 200000)
            or if some entered value is not integer.
    """

    # entering number of amounts
    days_count = input_int()

    # entering amounts per day
    amounts = [input_int() for _ in xrange(days_count)]

    return amounts


def check_integer(value):
    """
    Checks the value is correct.

    Returns:
        bool: True if it corresponds to the condition  (1 <= value <= 200000) otherwise False
    """

    return True if 1 <= value <= 200000 else False


def calculate_and_print_result(amounts, prices):
    """
    Calculate and print number of dishes for which Vasya can have enough money a day.

    Args:
        amounts (list): the list of amounts
        prices (list): the list of prices
    """

    for amount in amounts:
        print bisect_right(prices, amount + amount)


def main():
    try:
        prices = input_dish_prices()
        amounts = input_amounts()
        calculate_and_print_result(amounts, prices)

    except ValueError:
        pass

    except Exception:
        pass


if __name__ == '__main__':
    main()
