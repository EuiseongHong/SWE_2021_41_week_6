#initial version
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    answer = [0,0]
    for i in range(length):
        x = nums[i]
        for k in range(i+1,length):
            y = nums[k]
            
            if x+y == target:
                answer[0] = i
                answer[1] = k
                return answer
    return answer

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))