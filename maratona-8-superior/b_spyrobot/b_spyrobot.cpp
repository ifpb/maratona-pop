#include<bits/stdc++.h>
using namespace std;
int main(){
	vector<int> v1(100),v2(100);
	int t,n;
	while(cin >> t) {
		while(t--){
			cin >> n;
			int cont = 0;
			for(int i = 0; i < n; i++)
				cin >> v1[i];
			for(int i = 0; i < n; i++){
				cin >> v2[i];
				if(v1[i] == v2[i])
					cont++;
			}
			cout << cont << '\n';
		}
		
		
	}
}


