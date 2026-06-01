class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            num = nums[i]

            difference = target - num

            if difference in map:
                return [map[difference], i]

            map[num] = i
        