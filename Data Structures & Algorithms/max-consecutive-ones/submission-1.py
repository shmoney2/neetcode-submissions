class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      macs,cnt = 0,0
      for num in nums:
        if num == 0:
            cnt = 0
        elif num == 1:
            cnt += 1
            macs = max(macs,cnt)
      return macs
