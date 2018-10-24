#include <bits/stdc++.h>

using namespace std;

int main (){
    int n;
    int a[200][200];
    int b[200][200];
    int cont = 0;

    cin >> n;
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cin >> a[i][j];
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            cin >> b[i][j];
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++){
            if(a[i][j]>0&& b[i][j]>0)
                cont++;
        }
    cout << cont << "\n";

    return 0;
}
