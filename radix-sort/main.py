# It never makes comparasion with other elements


# Best time complexity: O(nk)
# Time complexity average: O(nk)
# Time complexity worst: O(nk)
# Space complexity: O(n + k)

# Notes: For this algorithm does not care if the data is sorted 
# or the data length also there is not edge cases

import math

def get_digit_from_number(number, position):
    to_str = str(abs(number))[::-1]
    to_str_len = len(to_str)

    return int(to_str[position]) if position >= 0 and position < to_str_len else 0


def get_digit_count(number):
    if number == 0:
        return 1

    return math.floor(math.log10(abs(number))) + 1


def get_most_digit_number(arr):
    highest_counter = 0 
    for item in arr:
        curr_highest_counter = get_digit_count(item)
        if (curr_highest_counter > highest_counter):
            highest_counter = curr_highest_counter
    
    return highest_counter


def redux_sort(arr):
    highest_counter = get_most_digit_number(arr)
    buket = [[] for _ in range(10)]

    for k in range(highest_counter):
        for j in arr:
            buket_item = get_digit_from_number(j, k)
            buket[buket_item].append(j)
        
        arr = [item for sublist in buket for item in sublist]
        buket = [[] for _ in range(10)]

    return arr


print(redux_sort([239,345,5467,12,2345,9852]))





