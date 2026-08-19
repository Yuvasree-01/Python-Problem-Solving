# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         result=[]
#         n=len(nums)/2
#         if nums[n]>=target:
#             nums[0]=n
#         # left=0
#         # right=len(nums)-1
#         neg_result=[-1,-1]

#         if len(nums)==0:
#             return neg_result

#         for i in range(n,len(nums)):
#             if nums[i]==target:
#                 result.append(i)
#                 break

#         for i in range(len(nums)-1,-1,-1):
#             if nums[i]==target:
#                 result.append(i)
#                 break
        
#         if len(result)==0:
#             return neg_result

#         return result


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost or rightmost index
        def findBound(find_leftmost: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    bound = mid # Found target, but let's look for a better boundary
                    if find_leftmost:
                        right = mid - 1 # Keep scanning left half
                    else:
                        left = mid + 1  # Keep scanning right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # Run binary search twice: once for the start index, once for the end index
        start = findBound(find_leftmost=True)
        end = findBound(find_leftmost=False)
        
        return [start, end]
