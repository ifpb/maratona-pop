#include <bits/stdc++.h>

using namespace std;


int main() {
	vector<int> v1,v2;
	int n,aux;
	cin >> n;
	while(n--) {
		cin >> aux;
		v1.push_back(aux);
		v2.push_back(aux);
	}
	sort(v1.begin(),v1.end());
	if(v1 == v2)
		cout << "SIM\n";
	else
		cout << "NAO\n";


	return 0;
}
