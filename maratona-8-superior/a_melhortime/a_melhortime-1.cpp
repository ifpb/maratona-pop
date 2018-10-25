#include<bits/stdc++.h>
using namespace std;
int main(){
	int n,maior=-1,s=-1,t,p;
	vector<pair<int,int> >v(210);
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>t>>p;
		if(p>maior){
			maior=p;
			s=t;
		}
	}
	cout<<s<<"\n";
}


