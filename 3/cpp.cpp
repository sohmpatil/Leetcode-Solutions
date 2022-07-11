class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int L = 0;
        int R = 0;
        int maxLength = 0;
        
        unordered_set<char> have;
        
        for(R = 0; R < s.size(); R++){
            char newChar = s[R];
            
            while(have.count(newChar)){
                have.erase(s[L]);
                L++;
            }
			
            maxLength = max(maxLength, R-L + 1);
            have.insert(s[R]);
        }
        return maxLength;
    }
};