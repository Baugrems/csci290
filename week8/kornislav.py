line = input()
nums = line.split()

nums = [int(x) for x in nums]
max_num = nums.index(max(nums))

del nums[max_num]

print(max(nums) * min(nums))