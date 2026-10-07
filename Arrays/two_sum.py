def two_sum (nums, target):
  hashmap = {}
  for i, num in enumerate(nums):
    shit = target - num
    if shit in hashmap:
      return [hashmap[shit], i]
    hashmap[num] = i
  return []

nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))