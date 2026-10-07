# Brute force 
# def three_sum_closest(nums, target):
#     closest = nums[0] + nums[1] + nums[2]
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             for k in range(j + 1, len(nums)):
#                 total = nums[i] + nums[j] + nums[k]
#                 if abs(total - target) < abs(closest - target):
#                     closest = total
#     return closest

def three_sum_closest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    return closest
nums = [-1, 2, 1, -4]
target = 1
print(three_sum_closest(nums, target))