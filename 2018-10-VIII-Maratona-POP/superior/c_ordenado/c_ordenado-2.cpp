#include <bits/stdc++.h>
using namespace std;

int main() {
  int v[300];
  int n;

  cin>>n;

  for(int i=0;i<n;i++){
    cin>>v[i];
  }
  for(int i=0;i<n-1;i++){
    if(v[i+1] < v[i]){
      cout<<"NAO\n";
      return 0;
    }
  }

  cout<<"SIM\n";
  return 0;
}

