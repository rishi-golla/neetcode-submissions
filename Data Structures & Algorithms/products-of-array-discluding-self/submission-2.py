class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        make an array of all ones
        define prefix = 1
        for loop
        output[i] *= prefix
        prefix *= nums[i]

        postfix = 1
        for loop -1, -1, -1
        output[i] *= postfix
        postfix *= nums[i]

        return output

        '''

        output = [1] * len(nums)

        prefix = 1
        postfix = 1 

        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output