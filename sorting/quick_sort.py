from random import random

def quick_sort(array: list[int], lower_limit: int, upper_limit: int):
    if lower_limit < upper_limit:
        partition_index = partition(array, lower_limit, upper_limit)
        quick_sort(array, partition_index + 1, upper_limit)
        quick_sort(array, lower_limit, partition_index - 1)

def partition(array: list[int], lower_limit: int, upper_limit: int):
    partition_index = lower_limit - 1
    pivot = array[upper_limit]

    for i in range(lower_limit, upper_limit):
        if array[i] <= pivot:
            partition_index += 1
            
            array[i], array[partition_index] = array[partition_index], array[i]

    array[partition_index + 1], array[upper_limit] = array[upper_limit], array[partition_index + 1]

    return partition_index + 1


if __name__ == "__main__":
    random_list = [
        round(random() * 100) for _ in range(1000)
    ]
    print(f"Random list to sort: {random_list}")
    quick_sort(random_list, 0, len(random_list) - 1)
    print(f"Sorted list: {random_list}")
