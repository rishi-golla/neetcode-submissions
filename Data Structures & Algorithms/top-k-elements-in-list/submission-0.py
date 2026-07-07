class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            map[num] = map.get(num, 0) + 1

        for num, count in map.items():
            bucket[count].append(num)

        res = []

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


        return []