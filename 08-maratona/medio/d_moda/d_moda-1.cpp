#include <bits/stdc++.h>

using namespace std;

int main (){
    int n;
    int m[1000]={};
    cin >> n;
    int maximo = 0;
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        m[a]++;
        maximo = max(maximo, m[a]);
    }
    for(int i=0; i<=500; i++){
        if(m[i]==maximo){
            cout << i << endl;
            return 0;
        }
    }
    return 0;
}
