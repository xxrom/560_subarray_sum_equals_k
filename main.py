# Clear explanation URL:
# https://medium.com/@edward.zhou/leet-code-560-subarray-sum-equals-k-explained-python3-solution-31ab6262615e

from typing import List

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    ans = 0
    prev = { 0: 1 }
    sum = 0

    for num in nums:
      sum += num
      diff = sum - k
      # print('sum %d, diff %d' % ( sum, diff))

      # Check if we had diff number previously
      if diff in prev:
        # If had then add number of times
        ans += prev[diff]

      # save each sum
      if sum not in prev:
        prev[sum] = 1
      else:
        prev[sum] += 1

    return ans

my = Solution()

nums = [1,1,1]
k = 2
trueAns = 2
# ----
# nums = [-1,-1,1,-1,1]
# k = 0
# trueAns = 4
# # ----
# nums = [0,0,0,0,0,0,0,0,0,0]
# k = 0
# trueAns = 55
# # ----
# # nums = [28,54,7,-70,22,65,-6]
# # k = 100
# # trueAns = 1
# # ----
# nums = [1, 1, 0, 1, 1, 0]
# k = 2
# trueAns = 2

ans = my.subarraySum(nums, k)
print("ans", ans, ans == trueAns)


# Runtime: 160 ms, faster than 46.44% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.4 MB, less than 15.06% of Python3 online submissions for Subarray Sum Equals K.