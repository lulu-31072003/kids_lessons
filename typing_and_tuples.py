def even_digits(num):
    digits = []
    count = 0

    if num == 0:
        digits = [0]
        count = 1

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            digits.append(digit)
            count += 1
        num = num // 10

    return digits


print(even_digits(12345))
