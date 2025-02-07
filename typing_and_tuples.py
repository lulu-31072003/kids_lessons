from typing import List, Union, Tuple

def even_digits(num: int) -> Tuple[bool, List[int]]:
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

    return (is_even, digits)


print(even_digits(12345))

my_tuple = (1, 2, 3)

num_1, num_2, num_3 = my_tuple

my_list = [1, 2, 10, 20]

my_list[1] = 5

a: int = 5
a = a + 5

b: str = "tomas je super"
b = "text"

c: float = 2.5

d: bool = True

e: List[int] = [1, 2, 3]

f: List[str] = ["a", "b", "C"]

g: List[Union[str, int]] = [1, "text", "5", 10]

h: Tuple[str, int, bool] = ("text", 1, False)
