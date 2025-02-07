# this function decides, if the given number is prime number
def is_prime(num):
    if num <= 1:
        return False
    
    i = 2
    while i < num:
        if num % i == 0:
            return False
    return True


# test function for is_prime function
def is_prime_test():
    assert not is_prime(1)
    print("Everything works :D !")


# finish the following function so that it returns result of num % 7
# don't you "%" operator though
def modulo_7(num):
    pass


# finish test function for modulo_7 function
def modulo_7_test():
    assert modulo_7(9) == 2


# finish the following function so that it returns sum of digits of the given number
# for 123 -> 1 + 2 + 3 = 6
def digit_sum(num):
    pass


# write test function for digit_sum function
def digit_sum_test():
    pass


# write test function for function that returns amount of occurences of "a" in the given word
def amount_of_a_test():
    pass


# now, write the function which returns amount of occurrences of "a" in the given word
# "abrakadabra" -> 5
# hint: strings are also lists in python
def amount_of_a(word):
    pass


def main():
    # you can call your functions here

    print()
    
    print(is_prime(1))

    print()


if __name__ == "__main__":
    main()
