def recursive_insertion_sort(array: list[int], length: int):
    if length <= 1:
        return
    
    recursive_insertion_sort(array, length - 1)

    key = array[length - 1]
    i = length - 2
    while i >= 0 and array[i] > key:
        array[i + 1] = array[i]
        i -= 1
    
    array[i + 1] = key


if __name__ == "__main__":
    sample_list = [2, 7, 1, 0]
    recursive_insertion_sort(sample_list, len(sample_list))
    print(sample_list)

    
    