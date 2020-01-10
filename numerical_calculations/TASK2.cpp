#include <iostream>
#include<math.h>

using namespace std;

// FUNKCJA NIE DZIAŁA, WYNIKIEM JEST inf i -inf
//BARDZO DŁUGO LICZY  
float x(int n){
    if(n==0)
        return 1;
    if(n==1)
        return 1/3;
    return ((-299)*x(n-1) + 100*x(n-2))*1/3;
}

//PO PARU ITERACJACH ZACZYNA SIĘ PSUĆs
void fun(){
    double x [51];
    x[0] = 1.0;
    x[1] = 1.0/3.0;
    cout<<"x1 = 1/"<<pow(3,1)<<" "<<"  | rekursja = "<<x[1]<<"   1/(3^"<<1<<") = "<<float(1/pow(3,1))<<endl;
    for(int i=2; i<=50; i++){
        x[i] = ((-299)*x[i-1] + 100*x[i-2])/3;
        cout<<"x"<<i<<" = 1/"<<pow(3,i)<<" "<<"  | rekursja = "<<x[i]<<"   1/(3^"<<i<<") = "<<float(1/pow(3,i))<<endl;
    }
}

int main()
{
    fun();
    return 0;
}