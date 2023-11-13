def generate_all_numbers():
    valid_numbers = []

    for first_digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for second_digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for third_digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                for fourth_digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            number = str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit)
                            valid_numbers.append(number)

    return valid_numbers


# Example usage
valid_numbers = generate_all_numbers()
for number in valid_numbers:
    print(number)
