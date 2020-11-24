from random import randint
from main import find_substring
from main import get_pow_arr


def generate_test_string():
    while True:
        n = randint(1, 100)
        pow_arr = get_pow_arr(n, 20)
        count = randint(1, 10)
        string = ""
        test_s = ""
        for i in range(count):
            s = pow_arr[randint(0, len(pow_arr) - 1)]
            string += s
            test_s += s + " "
        sub_c = find_substring(string, get_pow_arr(n, len(string)))
        if count < sub_c or (sub_c == -1 and count != -1):
            print("ERROR: " + test_s + " n: " + str(n) + " c: " + str(count) + " sub_c: " + str(sub_c))


if __name__ == '__main__':
    generate_test_string()
