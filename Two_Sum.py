class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
#                print buff_dict
                return [buff_dict[nums[i]] - 1, i]
            else:
                buff_dict[target - nums[i]] = i + 1
#                print buff_dict



nums = range(0, 23456, 2)
#nums = [2, 3, 4, 5, 6]
so1 = Solution()
print so1.twoSum(nums, 16000)
assert 1 not in [1, 2] , "123"