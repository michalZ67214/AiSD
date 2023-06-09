import sys
 
def array_max(nums, left, right, max=-sys.maxsize):
    
    if right - left == 1:
 
        if nums[left] < nums[right]:
 
            if max < nums[right]:
                max = nums[right]
 
        else:
 
            if max < nums[left]:
                max = nums[left]
 
        return max


    if left == right:
        if max < nums[left]:
            max = nums[left]
 
        return max

 
    mid = (left + right) // 2
 
    max = array_max(nums, left, mid, max)
 
    max = array_max(nums, mid + 1, right, max)
 
    return max

nums = [4, 3, 9, 2, 12, 6, 8, 5, 4]

max = array_max(nums, 0, len(nums) - 1)

print(f'Maksymalny element tablicy to {max}')