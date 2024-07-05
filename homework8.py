def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            print(number)
        if number < 0:
            break

numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers(numbers)
