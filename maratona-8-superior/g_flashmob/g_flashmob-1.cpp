#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define vvi vector<vi>


vvi AdjList;
vi match,vis;
int Aug(int l);
int main() {
	int n;
	cin >> n;
  string lixo;
  getline(cin,lixo);
	AdjList.resize(n*2);
	int MCBM = 0;
	match.assign(n*2,-1);
	for(int i  =0 ; i < n; i++) {
		string linha;
		int h;
		getline(cin,linha);
  
		stringstream ss(linha);
		while(ss >> h){
			AdjList[i].push_back(h+n);
     
		}
	}
	for(int i = 0; i < n; i++) {
		vis.assign(n,0);
		MCBM+=Aug(i);
	}
	cout << (MCBM  == n? "s2": "s/2") << '\n';



	return 0;
}

int Aug(int l){
	if(vis[l])
		return 0;
	vis[l] = 1;
	for(int i = 0; i < AdjList[l].size(); i++) {
		int r = AdjList[l][i];
		if(match[r] == -1 || Aug(match[r]) ) {
			match[r] = l;
			return 1;
		}
			
	}
	return 0;

}

