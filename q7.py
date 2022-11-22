def sum_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum_list(numbers[1:])