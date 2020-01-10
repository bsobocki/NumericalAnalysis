#include <iostream>
#include <math.h>
#include <iomanip>

/*
    |S - Sn| <= |An+1| < 10^(-5)
    4/(2n + 1) <= 1/100000
    2n + 1 >= 400 000
    n >= 399 999 / 2
    n >= 200 000
*/

using namespace std;

int firstNumberToPi(){
    double sum =0;
    int i =-1;
    while(abs(sum-M_PI)>=0.00001){
        i++;
        sum += (pow((-1),i)/(2*i + 1))*4;
        cout<<setprecision(15)<<"sum ("<<sum<<") -  PI ("<<M_PI<<")    =    "<<abs(M_PI - sum)<<endl;
    }
    return i;
}

int main()
{
    int minimum_N = firstNumberToPi();
    cout<<"minimalne N = "<<minimum_N<<endl; // Wyjdzie liczba 100 000.. no cóż ...
    return 0;
}