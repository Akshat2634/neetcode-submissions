class Solution {
public:
    string encode(vector<string>& strs) {
        string res = "";
        int size = strs.size();  // Changed from res.length() to strs.size()
        for (int i = 0; i < size; i++) {
            res += to_string(strs[i].length()) + "#" + strs[i];
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (j < s.length() && s[j] != '#') {
                j++;
            }
            int len = stoi(s.substr(i, j - i));
            string str = s.substr(j + 1, len);
            res.push_back(str);
            i = j + 1 + len;
        }
        return res;
    }
};
