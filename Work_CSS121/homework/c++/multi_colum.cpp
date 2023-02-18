#include <bits/stdc++.h>
using namespace std;

int Column_A[14] = {1,3,4,2,3,4,1,2,3,1,1,4,5,3};
int Column_B[14] = {1,1,4,4,5,3,3,4,3,5,1,1,2,5};
int Column_C[14] = {4,1,4,4,3,3,3,3,5,3,4,1,3,2};
int first,second,third;
int** merge_multi_Colum() {
    int** result = new int*[14];
    for (int i = 0; i < 14; i++) {
        result[i] = new int[3];
        result[i][0] = Column_A[i];
        result[i][1] = Column_B[i];
        result[i][2] = Column_C[i];
    }
    return result;
}
//Sort by columns 
bool compare_rows(int* row1, int* row2) {
    if (row1[first] != row2[first]) {
        return row1[first] < row2[first];
    } else if (row1[second] != row2[second]) {
        return row1[second] < row2[second];
    } else {
        return row1[third] < row2[third];
    }
}
//Sort order
void get_sort_order(int& first, int& second, int& third) {
    char sort_order;
    cout << "Enter the order to sort by columns (e.g. ABC): ";
    cin >> sort_order;

    first = sort_order - 'A';
    cin >> sort_order;
    second = sort_order - 'A';
    cin >> sort_order;
    third = sort_order - 'A';
}
int main() {
    int** multi_Colum = merge_multi_Colum();
     get_sort_order(first, second, third);
    sort(multi_Colum, multi_Colum + 14, compare_rows);

    // Print sorted array
    for (int i = 0; i < 14; i++) {
        for (int j = 0; j < 3; j++) {
            cout << multi_Colum[i][j] << " ";
        }
        cout << endl;
    }
}
