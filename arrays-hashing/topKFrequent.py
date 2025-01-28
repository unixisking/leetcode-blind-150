"""
347. Top K Frequent Elements O(nLog(n))
https://leetcode.com/problems/top-k-frequent-elements/description/
"""
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(lambda: 0)
        for num in nums:
            hashmap[num] += 1
        hashmap = {k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1],reverse=True)}
        return list(hashmap.keys())[:k]