def func(arr,sum):
  my_set = set()
  for i in arr:
    if i in my_set:
      return True
    else:
      my_set.add(sum - i)
  return False
print(func([2,3,4,5,6],5))
print(my_set)

"""Returning the indices of the 2 numbers that add up to target"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {target-nums[0]:0}
        for i in range(1,len(nums)):
            if nums[i] in my_dict:
                return [my_dict[nums[i]],i]
            my_dict[target-nums[i]]=i

sol1 = Solution()
res = sol1.twoSum([2,11,7,15],9)
print(res)