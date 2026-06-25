from collections import defaultdict

class Solution(object):
    def countMajoritySubarrays(self, nums, target):

        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + (1 if num == target else -1)

        count = 0 
        for j in range(1,len(prefix)):
            for i in range(j):
                if prefix[j] - prefix[i] > 0:
                    count += 1
        return count
        