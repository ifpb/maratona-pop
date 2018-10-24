#include <bits/stdc++.h>

using namespace std;

int main (){
    string nome;
    cin >> nome;
    int a=0, b=0;
    int maximo = 1;
    int cont = 0;
    for(int i=0; i<nome.size(); i++){
        if(nome[i]=='0')
            cont++;
        else{
            if(cont>maximo){
                maximo = cont;
                a = i-cont;
                b = i-1;
            }
            cont = 0;
        }
    }
    cout << a << " " << b << endl;
    return 0;
}
