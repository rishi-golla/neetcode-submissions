class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        output = []

        for num in nums:
            map[num] = map.get(num, 0) + 1

        array = sorted(map, key = map.get, reverse = True)

        return array[:k]



        