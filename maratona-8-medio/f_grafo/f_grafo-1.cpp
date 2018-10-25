#include <bits/stdc++.h>

using namespace std;

int main (){
    int n;
    cin >> n;
    int cont = 0;
    int maximo = 0;
    int who = 0;
    for(int i=0; i<n; i++){
        int cont = 0;
        for(int j=0; j<n; j++){
            int a;
            cin >> a;
            if(a==1){
                cont++;
                if(maximo < cont){
                    maximo = cont;
                    who = i+1;
                }
            }
        }
    }
    //cout << maximo << endl;
    if(maximo%2==0)
        cout << "J\n";
    else
        cout << "T\n";
    return 0;
}
