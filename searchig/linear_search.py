def linear_search(array: list[int], search_value: int) -> int:
    for i in range(len(array)):
        if array[i] == search_value:
            return i
        
    return -1

if __name__ == "__main__":
    sample_array = [1, 25, 50, 46, 2, 17]
    search_result = linear_search(sample_array, 50)
    print(search_result)
