from typing import List


class Solution:

  def moveZeroes(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """

    zeroes = []
    allCounter = 0

    for index, val in enumerate(nums):
      if val == 0:
        zeroes.append(val)
      else:
        nums[allCounter] = val
        allCounter += 1

    for index, val in enumerate(zeroes):
      nums[allCounter + index] = val


my = Solution()

n0 = [0, 1, 0, 3, 12]

my.moveZeroes(n0)

print('ans', n0)

# Runtime: 36 ms, faster than 99.51% of Python3 online submissions for Move Zeroes.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Move Zeroes.