#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
int map[10][10];
int HERO_P=2 ,HERO_X=2 ,HERO_Y=1;
int MON_P=3 ,MON_X=8 ,MON_y=5;
int T_P=1 ,T_X=5 ,T_Y=3;
int main()
{
    for(int i =0;i<10;i++){
        for(int k =0;k<10;k++){
            if (i==HERO_X and k==HERO_Y)
                map[i][k]=HERO_P;
            else if (i==MON_X and k==MON_y)
                map[i][k]=MON_P;
            else if (i==T_X and k==T_Y)
                map[i][k]=T_P;
            else
                map[i][k]=0;              
        }
    }
    cout << "The Map"<<endl; 
    for(int i =9;i>=0;i--){
        for(int k =0;k<10;k++){
            cout <<map[k][i];
        }
        cout <<endl;
    }
    int Taxicab =abs(MON_X-HERO_X)+abs(MON_y-HERO_Y);
    float Euclidean =sqrt(pow((MON_X-HERO_X),2)+pow((MON_y-HERO_Y),2));
    int Chebyshev;
    if (abs(MON_X-HERO_X) > abs(MON_y-HERO_Y))
        Chebyshev=abs(MON_X-HERO_X);
    else
        Chebyshev=abs(MON_y-HERO_Y);   
    cout << "Taxicab distance = " <<Taxicab <<endl;
    cout << "Euclidean distance = " <<Euclidean <<endl;
    cout << "Chebyshev distance = " <<Chebyshev <<endl;
    return 0;
}

