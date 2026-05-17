class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;

        // Step 1: Add all elements to the set
        for (int i = 0; i < nums.size(); i++) {
            st.insert(nums[i]);
        }

        int length = 0;

        // Step 2: Iterate through the set
        for (auto num : st) {
            // Only check for sequence start
            if (st.find(num - 1) == st.end()) {
                int curr = num;
                int mxlen = 1;

                // Step 3: Count consecutive numbers
                while (st.find(curr + 1) != st.end()) {
                    curr++;
                    mxlen++;
                }

                // Step 4: Track max length
                length = max(length, mxlen);
            }
        }

        return length;
    }
};