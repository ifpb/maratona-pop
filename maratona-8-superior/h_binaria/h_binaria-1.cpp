#include <bits/stdc++.h>
using namespace std;

#define TAM 260

int v[TAM][TAM];
int f[TAM];
int s[TAM];

void init ()
{
	memset(v, -1, sizeof v);
}

int pd (int a, int b)
{
  if (v[a][b] >= 0)
    return v[a][b];
  if (a >= b)
    return 0;
  if (a == b)
    return v[a][b] = f[a];
  
  int mn = INT_MAX;
  for (int i = a; i <= b; i++)
    mn = min(mn, pd(a, i - 1) + pd(i + 1, b) + s[b] - s[a - 1] - f[i]);
  return v[a][b] = mn;
}

int main()
{
	int n;
	
	while (cin >> n)
	{
    s[0] = 0;
    cin >> s[1];
    f[1] = s[1];
		for (int i = 2; i <= n; i++)
    {
			cin >> f[i];
      s[i] = s[i - 1] + f[i];
    }
		init();
		cout << pd(1, n) << "\n";
	}

	return 0;
}
