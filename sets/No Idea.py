class Solution():
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = 0
        R = len(nums) - 1
        print("R:",R)

        while L < R:
            middle = (L + R) // 2
            print("middle",middle,nums[middle])
            if nums[middle] == target:
                print ('found',nums[middle])
                break
            elif nums[middle] > target:
                R = middle - 1
                print('R',R)
            else:
                L = middle + 1
                print("L",L)

        return -1
T=Solution
T.search([-1,0,3,5,9,12],9)


