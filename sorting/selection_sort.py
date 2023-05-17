def selection_sort(array: list[int]):
    for i in range(len(array)):

        min_pointer = i
        for j in range(i + 1, len(array)):
            if array[j] <= array [min_pointer]:
                min_pointer = j

        array[i], array[min_pointer] = array[min_pointer], array[i]

if __name__ == "__main__":
    sample_array = [1, 5, 2, 9, 9, 2, -2]
    selection_sort(sample_array)
    print(sample_array)
