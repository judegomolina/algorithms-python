import random


def binary_search(lookup_value: int, sorted_array: list[int], start: int, end: int) -> int:
    mid_point = int((end + start) / 2)
    
    if sorted_array[mid_point] == lookup_value:
        return mid_point
    
    if sorted_array[mid_point] > lookup_value:
        end = mid_point
    else:
        start = mid_point

    return binary_search(lookup_value, sorted_array, start, end)


if __name__ == "__main__":
    sample_array = list(set([random.randint(0, 99999) for _ in range(200)]))
    sample_array.sort()
    print(sample_array)
    found_index = binary_search(sample_array[25], sample_array, 0, len(sample_array) - 1)
    print(found_index)
