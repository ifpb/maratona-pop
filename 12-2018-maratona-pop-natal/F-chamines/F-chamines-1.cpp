#include <bits/stdc++.h>

#define vs vector<string>
#define pb push_back

using namespace std;

void elimineP(vs &vetor, int x, int y){
  vetor[x][y] = 'M';
  int moves_x[] = {0, 0, 1, -1};
  int moves_y[] = {1, -1, 0, 0};
  for (int i=0; i<4; i++){
    int new_x = x + moves_x[i];
    int new_y = y + moves_y[i];
    if(new_x>=0 && new_x<vetor.size() && new_y>=0 && new_y<vetor.size()){
      if(vetor[new_x][new_y]=='P')  
        elimineP(vetor,new_x, new_y);
    }
  }
}

int verifyP(vs &vetor){
  int cont = 0;
  for(int i=0; i<vetor.size(); i++)
    for(int j=0; j<vetor[i].size(); j++){
      if(vetor[i][j]=='P'){
        cont++;
        elimineP(vetor, i, j);
      }
    }
  return cont;
}

void eliminep(vs &vetor, int x, int y){
  vetor[x][y] = 'P';
  int moves_x[] = {0, 0, 1, -1};
  int moves_y[] = {1, -1, 0, 0};
  for (int i=0; i<4; i++){
    int new_x = x + moves_x[i];
    int new_y = y + moves_y[i];
    if(new_x>=0 && new_x<vetor.size() && new_y>=0 && new_y<vetor.size()){
      if(vetor[new_x][new_y]=='p')  
        eliminep(vetor,new_x, new_y);
    }
  }
}

int verifyp(vs &vetor){
  int cont = 0;
  for(int i=0; i<vetor.size(); i++)
    for(int j=0; j<vetor[i].size(); j++){
      if(vetor[i][j]=='p'){
        cont++;
        eliminep(vetor, i, j);
      }
    }
  return cont;
}

int main() {
  ios_base::sync_with_stdio(false);
  vs vetor;
  int cont = 0;
  for(int i=0; i<10; i++){
    string a;
    cin >> a;
    vetor.pb(a);
  }
  cont+=verifyp(vetor);
  cont+=verifyP(vetor);
  cout << cont << endl;
  return 0;
}
