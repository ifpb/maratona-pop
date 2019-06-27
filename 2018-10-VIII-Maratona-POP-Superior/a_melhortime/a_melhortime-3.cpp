#include <bits/stdc++.h>

using namespace std;

int main () {
    int n;
    int m[200];
    int maximo = 0, id = 0;
    cin >> n;
    for(int i=0; i<n; i++){
        int a, b;
        cin >> a >> b;
        m[a] = b;
        if(b>maximo){
            id = a;
            maximo = b;
        }
    }
    cout << id << "\n";

    return 0;
}
