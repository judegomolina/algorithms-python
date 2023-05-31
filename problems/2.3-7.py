"""
Describe a O(n lg n) time algorithm that, given a set S of n integers and another integer x, 
determines whether or not there exist two elements in S whose sum is exactly x.

"""

# This is actually O(n).
# For O(n log n), we could use merge sort to sort the array then iterate through the array 
# and use binary search to look for the complement in the sorted array.
def find_if_two_elements_sum(array: list[int], x: int) -> bool:
    complements = set()
    for n in array:
        if n in complements:
            return True
        
        complements.add(x - n)
    
    return False


if __name__ == "__main__":
    sample_array = [1, 5, 20, 16, 9]
    print(find_if_two_elements_sum(sample_array, 25))