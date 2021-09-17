#include <bits/stdc++.h>

#define INF 0x3f3f3f3f

using namespace std;

int memo[2020][2020];
int value[2020], wgt[2020];
int n, m;

int solve(int ind, int cap){

  if(cap < 0) return -INF;
  if(ind == n) return 0;

  int& pdm = memo[ind][cap];
  if(pdm != -1) return pdm;

  return pdm = max( max(
    solve(ind+1, cap-wgt[ind]) + value[ind], 
    solve(ind+1, cap)), 
    solve(ind, cap-wgt[ind]) + value[ind]);

}

int main(){

  memset(memo, -1, sizeof memo);

  cin >> n >> m; 
  for(int i=0;i<n;i++){
    cin >> wgt[i] >> value[i];
  }  

  int dp = solve(0,n); 
  cout << (dp >= m ? "SIM\n" : "NAO\n"); 
 
  return 0;

}