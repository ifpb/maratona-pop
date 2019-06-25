#include <bits/stdc++.h>
using namespace std;

int main() {
  int qt[]={0,0,0,0,0,0,0};

  int mat[][8]{
  {7,0,0,0,0,0,0},
  {5,1,0,0,0,0,0},
  {4,0,1,0,0,0,0},
  {3,0,0,1,0,0,0},
  {2,0,0,0,1,0,0},
  {1,0,0,0,0,1,0},
  {0,0,0,0,0,0,1},
  {3,2,0,0,0,0,0},
  {2,1,1,0,0,0,0}, 
  {1,1,0,1,0,0,0},
  {0,1,0,0,1,0,0},
  {0,0,1,1,0,0,0},
  {1,0,2,0,0,0,0},
  {0,2,1,0,0,0,0}};

  int n,ler;
  vector<int> v;
  bool nao;

  cin>>n;

  for(int i=0;i<n;i++){
    cin>>ler;
    v.push_back(ler);
  }

  //sort(v.begin(),v.end());

  for(int i=0;i<n;i++){
    qt[v[i]-1]++;
  }
  
  /*for(int i=0;i<7;i++){
    cout<<qt[i]<<" ";
  }*/

  for(int i=0;i<14;i++){
    nao=0;
    for(int j=0;j<7;j++){
      if(qt[j] < mat[i][j]){
        nao=1;
        continue;
      }
    }
    if(!nao){
      cout<<"SIM\n";
      return 0;
    }

  }

  cout<<"NAO\n";
  return 0;
}

