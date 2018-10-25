#include <bits/stdc++.h>
using namespace std;

int main() {
  int n,qtde,iguais;
  int n1[100],n2[100];

  cin>>n;
  for(int i=0;i<n;i++){
    cin>>qtde;

    for(int j=0;j<qtde;j++) cin>>n1[j];
    for(int j=0;j<qtde;j++) cin>>n2[j];

    iguais=0;
    for(int j=0;j<qtde;j++){
      if(n1[j]==n2[j]){
        iguais++;
      }
    }
    cout<<iguais<<endl;

  }


  return 0;
}

