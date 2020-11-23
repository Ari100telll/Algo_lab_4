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


def find_substring(string, pow_arr: list):
    if len(string) == 0:
        return 0
    counter = 0
    length = len(pow_arr)
    temp_arr = pow_arr[:]
    false_arr = [True for i in range(length)]
    i = 0
    while True:
        if is_all_false(false_arr):
            break
        for j in range(length):
            if not false_arr[j]:
                continue
            if temp_arr[j][i] != string[i] or len(temp_arr[j]) > len(string):
                false_arr[j] = False
            elif i == len(temp_arr[j]) - 1:
                steps = find_substring(string[i + 1:], pow_arr)
                if steps != -1:
                    if counter == 0:
                        counter = steps
                    counter = min(counter, steps) + 1
                false_arr[j] = False
        i += 1
    if counter == 0:
        return -1
    return counter


if __name__ == '__main__':
    s, n = input().split(" ")
    n = int(n)
    len_arr = len(s)
    n_arr = get_pow_arr(n, len_arr)
    print(find_substring(s, n_arr))