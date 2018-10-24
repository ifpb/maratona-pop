#include <bits/stdc++.h>

using namespace std;

int main (){
    int a, b;
    cin >> a >> b;
    double c = a-((b/100.0) * a);
    double d = a - b;
    if(abs(c-d)<0.01)
        cout  << "TANTO FAZ COMO TANTO FEZ\n";
    else if(d<c)
        cout << "ABSOLUTO\n";
    else{
        cout << "PORCENTAGEM\n";
    }
    return 0;
}
