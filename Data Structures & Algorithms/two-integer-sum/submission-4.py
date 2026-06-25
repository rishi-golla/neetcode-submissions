class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, value in enumerate(nums):
            num = nums[index]

            difference = target - num

            if difference in map:
                return [map[difference], index]
            
            map[num] = index

            