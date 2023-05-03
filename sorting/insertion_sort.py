"""
Insertion Sort

Time complexity: O(n^2)
Space complexity: O(1)
"""


from typing import List

def insertion_sort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key


if __name__ == "__main__":
    sample_list = [2, 7, 1, 4, 99, -1, 1]
    insertion_sort(sample_list)
    print(sample_list)
    