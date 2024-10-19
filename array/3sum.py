# Bruit Force method

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in final:
                            final.append(temp)
        return final


# Better Approach

final = []
for i in range(0, len(nums)):
    hashset = set()
    for j in range(i + 1, len(nums)):
        third = -(nums[i] + nums[j])
        if third in hashset:
            temp = [nums[i], nums[j], third]
            temp.sort()
            if temp not in final:
                final.append(temp)
        set.add(nums[j])



# Optimal Solution 

nums = [-1,0,1,2,-1,-4]
nums.sort()
final = []
for i in range(0, len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    j = i + 1
    k = len(nums) - 1

    while j < k:
        sum = nums[i] + nums[j] + nums[k]
        if sum < 0:
            j += 1
        
        elif sum > 0:
            k -= 1 
        else:
            temp = [nums[i] , nums[j] , nums[k]]
            final.append(temp)
            j += 1
            k -= 1
            while(j < k and nums[j] == nums[j -1]):
                j += 1
            while(j < k and nums[k] == nums[k+1]):
                k -= 1
            


print(final)