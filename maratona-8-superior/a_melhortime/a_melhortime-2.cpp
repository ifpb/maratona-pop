#include <bits/stdc++.h>
using namespace std;

int main() {
  int id[300], valor[200];
  int n, maior=-1, mp;

  cin>>n;
  for(int i=0;i<n;i++){
    cin>>id[i]>>valor[i];
    if(valor[i]>maior){
      maior=valor[i];
      mp=i;
    }
  }
  cout<<id[mp]<<endl;


  return 0;
}

