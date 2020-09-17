#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int a, b;
    while(cin >> a >> b){
        for(int i = 0; a % i != b; i++){
            if(a % i == b)
                cout << i << '\n';
                    break;
        }
    }
}