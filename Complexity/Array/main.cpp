#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    vector<int> v;
    int number;
    int size = pow(10,5) + 1;
    vector<int> count(size, 0);  
    int unique = 0;
    int j = 0;

    for(int i=0 ; i<n; i++){
        cin >> number;
        v.push_back(number);
    }

    for(int i=0; i<n; i++){
        if(count[v[i]] == 0){
            unique++;
        }
        count[v[i]]++;
        if(unique == k){
            while(j < i  && count[v[j]] > 1){
                count[v[j]]--;
                j++;
            }
            cout << j + 1 << " " << i + 1 << endl;
            return 0;
        }
    }
    cout << -1 << " " << - 1 << endl;
}