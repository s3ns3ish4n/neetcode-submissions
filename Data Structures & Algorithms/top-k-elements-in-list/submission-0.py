class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        answer = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                answer.append(num)
            if(len(answer)==k):
                return answer


        return answer