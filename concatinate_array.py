class Solution:
def getConcatenation(self, nums: List[int]) -> List[int]:
nums.extend(nums)
return nums

return nums + nums
return nums * 2

ans = []
for k in range(2):
  for i in nums:
    ans.append(i)
return ans
