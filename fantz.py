import re


def get_pow_arr(element, leng):
    if element == 1:
        return ["1"]
    arr = []
    i = 0
    while True:
        arr.append(bin(element ** i)[2:])
        if len(arr[i]) > leng:
            break
        i += 1
    return arr[:-1]


def is_all_false(arr: list):
    for element in arr:
        if element:
            return False
    return True


def find_substring(string, pow_strings_arr: list):
    if len(string) == 0:
        return 0
    counter = 0
    for pow_string in pow_strings_arr:
        if len(pow_string) > len(string):
            break
        result = re.match(pow_string, string)
        if result is not None:
            index = result.span(0)[1]
            inner_counter = find_substring(string[index:], pow_strings_arr)
            if inner_counter != -1:
                if counter == 0:
                    counter = inner_counter + 1
                counter = min(counter - 1, inner_counter) + 1
    if counter == 0:
        return -1
    return counter


def count_elements_in_string(string, element):
    pow_arr = get_pow_arr(element, len(string))
    return find_substring(string, pow_arr)


if __name__ == '__main__':
    s, n = input().split(" ")
    n = int(n)
    print(count_elements_in_string(s, n))
