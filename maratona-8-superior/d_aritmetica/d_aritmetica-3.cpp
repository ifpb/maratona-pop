#include <bits/stdc++.h>

using namespace std;

int main () {


    string operacao;
    vector<string> nomes;
    vector<int> numeros;
    nomes.push_back("um");
    nomes.push_back("dois");
    nomes.push_back("tres");
    nomes.push_back("quatro");
    nomes.push_back("cinco");
    nomes.push_back("seis");
    nomes.push_back("sete");
    nomes.push_back("oito");
    nomes.push_back("nove");
    nomes.push_back("dez");
    nomes.push_back("onze");
    nomes.push_back("doze");
    nomes.push_back("treze");
    nomes.push_back("catorze");
    nomes.push_back("quatorze");
    nomes.push_back("quinze");
    nomes.push_back("dezesseis");
    nomes.push_back("dezessete");
    nomes.push_back("dezoito");
    nomes.push_back("dezenove");
    nomes.push_back("vinte");
    for(int i=1; i<=14; i++)
        numeros.push_back(i);
    numeros.push_back(14);
    for(int i=15; i<=20; i++)
        numeros.push_back(i);

        vector<string> lista;
    vector<int> soma;
    while(cin >> operacao){
        //cout << operacao << "\n";
        //cout << lista.size() << "\n";
        lista.push_back(operacao);
    }
    if(lista.size() == 1)
        cout << lista[0] << "\n";
    else{
        for(int i = 1; i < lista.size(); i+=2){
            if(lista[i] == "vezes"){
                int acum ;
                if(i > 2){
                    if(lista[i-2] == "mais" )
                        acum = 1;
                    else if(lista[i-2] == "menos" )
                        acum = -1;


                }
                else
                    acum = 1;
                acum *= (numeros[find(nomes.begin(), nomes.end(), lista[i-1])-nomes.begin()]);
                if(i > 2)
                    lista[i-2] = "";
                //cout << acum << "|";
                for(; i < lista.size() && lista[i] == "vezes"; i+=2){
                    acum *= (numeros[find(nomes.begin(), nomes.end(), lista[i+1])-nomes.begin()]);
                    //cout << acum << "|";
                    lista[i+1] = "";
                    lista[i] = "";
                    lista[i-1] = "";
                }

                soma.push_back(acum);
            }
        }
        //cout << "passou\n";
        if(lista[0] != "")
            soma.push_back(numeros[find(nomes.begin(), nomes.end(),lista[0]) - nomes.begin()]);
        for(int i = 1; i < lista.size(); i++){

            //cout << "&\n";
            if(lista[i] == "mais"){
                //soma.push_back(numeros[find(nomes.begin(), nomes.end(),lista[i-1]) - nomes.begin()]);
                soma.push_back(numeros[find(nomes.begin(), nomes.end(),lista[i+1]) - nomes.begin()]);
                i++;
            }
            if(lista[i] == "menos"){
                //soma.push_back((-1)*(numeros[find(nomes.begin(), nomes.end(),lista[i-1]) - nomes.begin()]));
                soma.push_back((-1)*(numeros[find(nomes.begin(), nomes.end(),lista[i+1]) - nomes.begin()]));
                i++;
            }
        }

        int acum = 0;
        for(int i = 0 ; i < soma.size(); i++)
            acum += soma[i];

        cout << nomes[find(numeros.begin(), numeros.end(),acum)-numeros.begin()] << "\n";
    }



    return 0;
}
