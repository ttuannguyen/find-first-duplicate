input = [2, 1, 3, 3, 2]

def find(input):
    
    # A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. 
    set_ = set()
    
    # iterate through the arr, if the number is already in the set, return that number (duplicate); otherwise, add the item to the set
    for item in input:
        if item in set_:
            return item
        set_.add(item)
    return -1
    
    
    # For Loop Method (brute force) 
    # not returning 3, not good because O(n^2) 
    # size = len(input)
    # for i in range(size):
    #     for j in range(i+1, size):
    #         if input[i] == input[j]:
    #             return input[i]  
    #         print(input[i], input[j]
    # return -1 


print(find(input))
