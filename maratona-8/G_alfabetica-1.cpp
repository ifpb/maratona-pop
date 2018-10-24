#include <bits/stdc++.h>

using namespace std;

int main (){
    int n, b;
    cin >> n;
    string a;
    vector<int> vetor;
    for(int i=0; i<n; i++){
        cin >> a >> b;
        vetor.push_back(b);
    }
    sort(vetor.begin(), vetor.end());
    for(int i=0; i<vetor.size(); i++){
        if(i!=0)
            cout << " ";
        cout << vetor[i];
    }
    cout << "\n";
    return 0;
}
