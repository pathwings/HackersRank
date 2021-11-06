from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    # List to store results
    result = []
    # Dictionary to store the difference and its index
    index_map = {}
    # Loop for each element
    for i, n in enumerate(nums):
        print("i",i,"n",n)
        # Difference which needs to be checked
        difference = target - n
        print("difference",difference)
        if difference in index_map:
            result.append(i)
            result.append(index_map[difference])
            break
        else:
            index_map[n] = i
            print("index_map",index_map)
    print(result)

twoSum([2,7,11,15],9)