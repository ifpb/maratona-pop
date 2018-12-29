#include <bits/stdc++.h>

#define TAM 10000
#define pb push_back
#define vi vector<int>
#define vb vector<bool>

using namespace std;

void crivo (vb &matrix, vi &primos){
  for (int i=2; i<TAM; i++){
    if (!matrix[i]){
      for (int j=i+i; j<TAM; j+=i)
          matrix[j] = true;
      primos.pb(i);
    }
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  vb matrix(TAM, false);
  vi primos;
  crivo(matrix, primos);
  int s1=0, s2=0;
  int n;
  cin >> n;
  while(n--){
    int a;
    cin >> a;
    if(find(primos.begin(), primos.end(),a)!=primos.end())
      s2+=a;
    else
      s1+=a;
  }
  cout << s1 << endl << s2 << endl;
  return 0;
}