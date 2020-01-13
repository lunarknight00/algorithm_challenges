#include<iostream>
#include<vector>

using namespace std;
int totalNQueens(int n);
void placeQ(int& count,const int& n,vector<int> board,int r);


int totalNQueens(int n) {
    int count = 0;
    vector<int> board(n);
    placeQ(count, n, board, 0);
    return count;
}

void placeQ(int& count,const int& n,vector<int> board,int r){
    if(r == n ){
        count ++;
        return;
    }
    for(int i=0;i<n;i++){
        bool legal = true;
        for(int j=0;j<r;j++){
            if(board[j] == i ||(board[j] == i+r-j)||(board[j] == i-r+j)){
                legal = false;
                break;
            }
        }
        if(legal){
            board[r] = i;
            placeQ(count, n, board, r+1);
        }
    }
}

int main()
{
    int n = 4;
    // int res = totalNQueens(4);
    // cout << res << endl; 

    int count = 0;
    vector<int> board(n);
    placeQ(count,n,board,0);
    cout << count << endl;
    // return count;
    return 0;
}