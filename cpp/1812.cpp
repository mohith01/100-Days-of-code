class Solution {
public:
    bool squareIsWhite(string coordinates) {
          cout<< (coordinates[0]-97)<<(coordinates[1] - 49);
        return (((coordinates[0]-96)+(coordinates[1] - 48))%2==0?false:true);
    }
};
