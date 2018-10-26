#include <bits/stdc++.h>

using namespace std;

bool subsetsum(vector<int> &vetor, int valor){
    vector<bool> marc(valor+1, false);
    marc[0] = true;
    for(int i=0; i<vetor.size(); i++){
        for(int j=valor; j>=vetor[i]; j--){
            if(marc[j-vetor[i]])
                marc[j] = true;
        }
    }
    return marc[valor];
}

int main () {
    int n;
    cin >> n;
    vector<int> vetor;
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        vetor.push_back(a);
    }
    if(subsetsum(vetor, 7))
        cout << "SIM\n";
    else
        cout << "NAO\n";
    return 0;
}
