def quicksort(nums):
  
  if len(nums) <= 1:
    return nums
  else:
    left = nums[0:len(nums)//2]
    right = nums[len(nums)//2:len(nums)]
  
    if len(left) == 1 and len(right) == 1:
      if left[0] < right[0]:
        return left+right
      else:
        return right+left
    else:
      new_left = quicksort(left)
      new_right = quicksort(right)
      full = []
      i = 0
      j = 0
      
      while i < len(new_left) and j < len(new_right):
        if new_left[i] < new_right[j]:
          full.append(new_left[i])
          i += 1
        else:
          full.append(new_right[j])
          j += 1
      
      return full+new_left[i:len(new_left)]+new_right[j:len(new_right)]
    
nums = [2,6,2,8,4,7,1,9,4]

sorted_nums = quicksort(nums)

print(sorted_nums)
