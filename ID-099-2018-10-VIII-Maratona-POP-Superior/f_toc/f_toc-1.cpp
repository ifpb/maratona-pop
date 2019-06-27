#include <bits/stdc++.h>
using namespace std;

#define vi vector<int>
bool subsetsum(vi &vetor, int valor);

int main() {
	int n;
	cin >> n;
	vi v(n);
	for(int i =0; i < n; i++)
		cin >> v[i];

	cout << (subsetsum(v,7)? "SIM": "NAO") << '\n';



	return 0;
}

bool subsetsum(vi &vetor, int valor){
	vector<bool> marc(valor+1,false);
	marc[0] = true;
	for(int i = 0; i < vetor.size(); i++) {
		for(int j =  valor; j >=vetor[i]; j--) {
			if(marc[j-vetor[i]])
				marc[j] = true;
		}
	}
	return marc[valor];


}
