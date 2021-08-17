#include <iostream>
#include <vector>
#include <map>

std::vector<int> a = {10, 11, 12, 13, 14};
std::map<int,int> d = std::map<int,int>();


void build(int l, int r, int p) {  
  if (l == r) {
    d[p] = a[l]; 
    return;
  }
  int m = l + ((r - l) / 2);
  build(l, m, p * 2); 
  build(m + 1, r, (p * 2) + 1);  
  d[p] = d[p * 2] + d[(p * 2) + 1];
}

int getsum(int l, int r, int s, int t, int p) {
  if (l <= s && t <= r) return d[p];
  int m = s + ((t - s) / 2);
  int sum = 0;
  if (l <= m)
    sum += getsum(l, r, s, m, p * 2);  
  if (r > m) 
    sum += getsum(l, r, m + 1, t, (p * 2) + 1);
  return sum;
}

void print(int number){
    std::cout << number << std::endl;
}

int main(){
    build(0,4,1);
    print(getsum(2,4,0,4,1));
    return 0;
}