#include <iostream>
using namespace std;

int main(){
    int p1, q1, p2, q2, p3, q3, p4, q4;
    cin >> p1 >> q1 >> p2 >> q2 >> p3 >> q3 >> p4 >> q4;
    double n1 = double(p1 / q1);
    double n2 = double(p2 / q2);
    double n3 = double(p3 / q3);
    double n4 = double(p4 / q4);

    if (n1 + n2 > n3 +n4){
        cout << '1';
    }
    if(n1 + n2 < n3 + n4){
        cout << '-1';
    }
    if (n1 + n2 == n3 + n4){
        cout << '0';
    }
}
