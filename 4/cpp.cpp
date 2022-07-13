class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int numc1 = nums1.size();
        int numc2 = nums2.size();
        int i = 0;
        int j = 0;
        int m1 = -1;
        int m2 = -1;
        for (int count = 0; count < (numc1 + numc2) / 2 + 1; count++) {
            m2 = m1;
            if (i != numc1 && j != numc2) {
                m1 = (nums1[i] > nums2[j]) ? nums2[j++] : nums1[i++];
            } else if (i < numc1) {
                m1 = nums1[i++];
            } else {
                m1 = nums2[j++];
            }
        }
        if ((numc1 + numc2) % 2 == 1) {
            return m1;
        } else {
            return ((double)(m1+m2) / 2);
        }
    }
};