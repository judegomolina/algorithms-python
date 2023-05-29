def merge_sort(array: list[int], p: int, r: int):
    if p < r - 1:
        q = int((p + r) / 2)
        merge_sort(array, p, q)
        merge_sort(array, q, r)
        merge(array, p, q, r)
        
def merge(array: list[int], p: int, q: int, r: int):
    left = array[p: q] + [float("inf")]
    right = array[q: r] + [float("inf")]
    
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        
        else:
            array[k] = right[j]
            j += 1


if __name__ == "__main__":
    sample_array = [4, 3, 2, 1]
    merge_sort(sample_array, 0, len(sample_array))
    print(sample_array)
    