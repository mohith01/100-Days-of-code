class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
     vector<int> res;
     res.emplace_back(first);
    for (int i =0;i<encoded.size();i++){
        res.emplace_back(res[res.size()-1]^encoded[i]);
    }
    return res;
    }
};
