class dup:
  def dups(self, nums: list[int]):
    hash = set()
      for i in nums:
        if i in hash:
          return True
        hash.add(i)
      return False
