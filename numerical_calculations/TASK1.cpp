#include <iostream>
#include<math.h>
#include <iomanip>

using namespace std;

// cos(10^-7) = 0.99999999999995
//cos(10^-i) = 1.0 gdzie i = 8, 9, 10 ...

float f(long double x){
    return 4038 * (1 - cos(x)) / (pow(x,2.0));
}

long double f2(long double x){
    return 4038 * (1 - cos(x)) / (pow(x,2.0));
}

int main()
{
    //for(int i=11; i<=20; i++){
    //    cout<<f2(pow(10,-i))<<endl;
    //}
    long double x = 0.01;
    while(cos(x)!=1){
        x /= 10.0;
        cout<<setprecision(10)<<(double)cos(x)<<"     x = "<<x<<endl;
    }
    return 0;
}
