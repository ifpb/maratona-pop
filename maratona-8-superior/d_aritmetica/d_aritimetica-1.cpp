#include <bits/stdc++.h>
#define TAM 100100
using namespace std;

int main() {
  string eq;
  int sinal=1,k =0;
  map<string,int>ln;
  string index[] = {"um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"};
  for(int i=0;i<20;i++)
    
    ln[index[i]]=i+1;
  int vetor[TAM];
  while(cin>>eq){
    if(eq=="quatorze")
      eq="catorze";
    if(ln.count(eq)){
      vetor[k]=sinal*ln[eq];
     
      k++;
    }
    else if(eq=="vezes"){
      cin>>eq;
      
      vetor[k-1]*=ln[eq];
      
      sinal=1;
    }
    else if(eq=="mais")
      sinal=1;
    else
      sinal=-1;
  }
  for(int i=1;i<k;i++){
    vetor[i]+=vetor[i-1];
  }
  cout<<index[vetor[k-1]-1]<<"\n";
}
