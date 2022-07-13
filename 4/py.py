class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numc1 = len(nums1)
        numc2 = len(nums2)
        m1 = m2 = -1
        i = j = 0
        for _ in range(0, (numc1 + numc2) // 2 + 1):
            m2 = m1
            if (i != numc1 and j != numc2):
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j = j + 1
                else:
                    m1 = nums1[i]
                    i = i + 1
            elif (i < numc1):
                m1 = nums1[i]
                i = i + 1
            else:
                m1 = nums2[j]
                j = j + 1
        if ((numc1 + numc2) % 2 == 1):
            return m1
        else:
            return ((m1 + m2) / 2)