from random import randint
from main import find_substring
from main import get_pow_arr


def get_pow_arr1(element, st):
    arr = []
    i = 0
    while i < st:
        arr.append(bin(element ** i)[2:])
        i += 1
    return arr  # [:-1]


def generate_test_string():
    while True:
        n = randint(1, 100)
        pow_arr = get_pow_arr1(n, 5)
        count = randint(1, 10)
        string = ""
        for i in range(count):
            string += pow_arr[randint(0, 4)]
        # print(string + " " + str(n))
        sub_c = find_substring(string, get_pow_arr(n, len(string)))
        if count != sub_c:
            print("ERROR: " + string + " n: " + str(n) + " c: " + str(count) + " sub_c: " + str(sub_c))
            # return 0


if __name__ == '__main__':
    generate_test_string()
