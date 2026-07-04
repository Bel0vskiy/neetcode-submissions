class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # Sorting is crucial for the duplicate-skipping trick!
        
        for i, a in enumerate(nums):
            # 1. SKIP DUPLICATES FOR THE FIRST NUMBER
            # If this isn't the first element and it's equal to the previous element, skip it.
            if i > 0 and a == nums[i - 1]:
                continue
                
            # Optimize: If the first number is greater than 0, 3 positive numbers can never sum to 0
            if a > 0:
                break
                
            # Run two-pointer search for the remaining two numbers
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum == 0:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # 2. SKIP DUPLICATES FOR THE SECOND NUMBER
                    # Keep moving 'l' forward if it's pointing to the same value as before
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
                    
        return ans
