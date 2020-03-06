/* Leetcode 204 problem
* input a integer number n
* output number of prime number in the range of (2,n)
* not include n
*/

// written by Henry Zhuo


#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;
int countPrime(int n);


int countPrime(int n){
    // init a vector buffer
    vector<bool> buffer(n,true);
    buffer[0]=buffer[1]=false;
    // iterate from first prime number 2
    // exclude n if n is a prime
    // noted that var type int has upper bound, use long long safer
    for(long long i =2;i<n;i++){
        // iterate i*i to n to filter non-primes
        for(long long j = i*i; j< n;j+i){
            if(buffer[j]) buffer[j] = false;
        }
    }
    return count(buffer.begin(),buffer.end(),true);
}


int main(){

    // test case 1
    int result = countPrime(3);
    if(1 == result) cout<<"Test case 1 pass"<< endl;
    else cout<<"test 1 failed"<<endl;
    result = countPrime(10);
    if(4 == result) cout<<"Test case 2 passs"<< endl;
    else cout<<"test 2 failed"<<endl;

    return 0;    
}