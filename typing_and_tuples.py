def even_digits(num):
    digits = []
    is_even = True

    if num == 0:
        digits = [0]

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            digits.append(digit)
        else:
            is_even = False
        num = num // 10

    return is_even


print(even_digits(12345))


