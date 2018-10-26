#include <bits/stdc++.h>

using namespace std;

int main () {
    int n;
    bool ok = true;
    cin >> n;
    int v[300];
    cin >> v[0];
    for(int i = 1; i<n; i++){
        cin >> v[i];
        if(v[i]<v[i-1]){
            ok = false;
        }
    }
    if(ok)
        cout << "SIM\n";
    else
        cout << "NAO\n";
    return 0;
}
