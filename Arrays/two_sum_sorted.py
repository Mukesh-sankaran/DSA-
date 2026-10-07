def two_sum_sorted (nums, target):
  left = 0
  right = len(nums) - 1
  while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
      return [left , right] 
    elif current_sum < target:
      left += 1 
    else: 
      right -= 1
  return[]
nums = [2, 7, 11, 15, 22, 25, 29]
target = 29
print(two_sum_sorted (nums, target))