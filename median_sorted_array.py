class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        new_total = []
        
        if nums1.__len__() == 0:
            new_total = nums2
        elif nums2.__len__() == 0:
            new_total = nums1
        else:
            for a in range(0, nums1.__len__() + nums2.__len__()):
                if nums1[0] <= nums2[0]:
                    this_num = nums1.pop(0)
                else:
                    this_num = nums2.pop(0)
                new_total.append(this_num)
                if nums1.__len__() == 0:
                    new_total = new_total + nums2
                    break
                elif nums2.__len__() == 0:
                    new_total = new_total + nums1
                    break
                    
        print(new_total)
        
        if new_total.__len__() % 2 == 0:
            indices = (int(new_total.__len__()/2)-1, int(new_total.__len__()/2))
            return (new_total[indices[0]] + new_total[indices[1]])/2
        else:
            index = ((new_total.__len__()/2)-.5)
            return new_total[int(index)]

'''
Success
Details 
Runtime: 209 ms, faster than 5.15% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.5 MB, less than 80.98% of Python3 online submissions for Median of Two Sorted Arrays.
'''
