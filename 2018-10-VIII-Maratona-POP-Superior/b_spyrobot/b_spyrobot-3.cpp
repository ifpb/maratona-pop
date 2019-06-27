#include <bits/stdc++.h>

using namespace std;

int main () {
    int n;
    int cont = 0;
    int m[200];
    int b[200];
    cin >> n;
    for(int i=0; i<n; i++){
        int n2;
        cont = 0;
        cin >> n2;
        for(int i=0; i<n2; i++){
        cin >> m[i];
        }
        for(int i=0; i<n2; i++){
            cin >> b[i];
        }
        for(int i=0; i<n2; i++){
            if(m[i]==b[i])
                cont++;
        }
        cout << cont << "\n";
    }

    return 0;
}
