# Brute force 
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if nums[i] + nums[j] + nums[k] == 0:

#Optimal Method 

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))