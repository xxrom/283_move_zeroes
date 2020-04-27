from typing import List


class Solution:

  def moveZeroes(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """

    zerosCounter = 0
    noneZeroCounter = 0

    for value in nums:
      if value == 0:
        zerosCounter += 1
      else:
        nums[noneZeroCounter] = value
        noneZeroCounter += 1

    for index in range(zerosCounter):
      nums[noneZeroCounter + index] = 0


my = Solution()

n0 = [0, 1, 0, 3, 12]
# n0 = [1, 1, 3, 0]

my.moveZeroes(n0)

print('ans', n0)

# Runtime: 36 ms, faster than 99.62% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.3 MB, less than 5.97% of Python3 online submissions for Move Zeroes.