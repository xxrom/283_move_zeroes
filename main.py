from typing import List


class Solution:

  def moveZeroes(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    all = []
    zeroes = []

    for index, val in enumerate(nums):
      if val == 0:
        zeroes.append(val)
      else:
        all.append(val)

    for index, val in enumerate(all):
      nums[index] = val

    for index, val in enumerate(zeroes):
      nums[len(all) + index] = val


my = Solution()

n0 = [0, 1, 0, 3, 12]

my.moveZeroes(n0)

print('ans', n0)

# Runtime: 48 ms, faster than 74.43% of Python3 online submissions for Move Zeroes.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.