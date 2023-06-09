def array_sum(nums, left, right):
   if left == right:
       return nums[left]
   else:
       if left == right-1:
           return nums[left] + nums[right]
       else:
           mid = left + (right-left)//2
           left_sum = array_sum(nums, left, mid)
           right_sum = array_sum(nums, mid+1, right)
           return left_sum + right_sum

array_nums = [2, 2, 2]
print(f'Suma elementów tablicy wynosi: {array_sum(array_nums, 0, len(array_nums)-1)}')