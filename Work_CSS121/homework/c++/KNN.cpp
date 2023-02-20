#include <bits/stdc++.h>
using namespace std;

double euclidean_distance( double data[], double testdata[], int n_features) {
    double distance = 0;
    for (int i = 0; i < n_features; i++) {
        distance += pow(data[i] - testdata[i], 2);
    }
    return sqrt(distance);
}
double DistanceList[54];
const int n_features = 8;
string mbti_type_data[54] ={"INTP","ISTP","ENTP","ISTJ","ENFP","ISTJ","INTJ","ESFJ","INFJ","INFJ","ENTP","INTP","INFP","ESTJ","ESTJ",
"INTP","INFP","ENTP","ESFP","ESTJ","ISFJ","ISTP","ENTP","ENTP","INTP","INTP","ISFJ","ISTJ","ESTJ","ESFJ","INTP","INTJ","INTP","ENFP","ISTP","INTP",
"ENTP","ISTJ","INTP","INTP","ENTP","ESTJ","ESTJ","ESTJ","INTP","ESTJ","INFP","ISTJ","ESTP","ESFJ","INFP","ENTP","INTP","INFJ"
    }; 
string Name_data[54]={"Warin Wattanapornprom","Kornkanok Welagert","Kunakron Tana","Chinnapt Sukthong","Chinavat Nachaithong",
"Teekamon Chaiwongwutikul","Dollatham Charoethammkic","Thiyada Kittiwithitkun","Thidarat Sitthidech",
"Phumiphat Santithawornying","Manotham Damnoen","Wachirawit Intapan","Warit Teerapong","Sasima Phanta",
"Artima Rojanagamonson","Koraphan Manitha","Ganyawee Sanghom","Kimhan Jongjaidee","Chaithawat Saklang",
"Nattanischa Aumpornchairuch","Thanapong Simmanee","Thidarut Deeramies","Panachai Suvimolopas","Pattanapol Saelim",
"Pichayut Sombat","Poomthai Promkote","Lalhada Suttiprapha","Santijit Kamnak","Kantinan Kuikeaw","Chothanin Thitisrirat",
"Warin Wattanapornprom","Yanisa Mungkarotai","Jessada Pranee","Suphanut Chanroong","Keerataphan Malai","Thanachot Wongyai",
"Pawinnarut Pornpanarat","Phirada Chemmanmud","Phattawee Witthayapanyanont","Sathapana Tinop","Nuttasit Tannitipaisal","Nut Somwang",
"Pattarachanon Uraiwichaikul","Krantharat Ratchart","Pasin Laopooti","Patchnida Hemwannanukul","Nakamon Yongpaisarn","Atchima Nateepradap",
"Natthapon Tanateeraanan","Naphatchanun Suecey","Narutchai Mauensaen","Natchapon Ponlaem","Phacharaphon Aiamphan","Sarita Tongsawat"
};
double train_data[54][n_features] = {
    {32,32,27,36,29,31,28,23},
{28.4,29.4,29,34,27,24,23,21},
{30,24,25,27,23,28,26,17},
{21,25.6,29,30,28,29,28,30},
{35.6,37.8,27,28,28,29,36,35},
{23.4,26,27,30,28,31,26,21},
{37,47.8,43,47,47,45,37,43},
{34,26.6,26,29,28,34,33,32},
{29,31.2,26,27,17,32,33,26},
{26.2,28.6,21,25,30,31,32,20},
{35.4,29.4,26,28,28,19,29,27},
{29,25,21,23,32,36,14,19},
{35.8,28.4,28,32,18,32,31,35},
{20.4,22.4,32,32,24,28,25,16},
{34.8,28,35,32,26,32,28,17},
{22.4,31.4,33,34,33,35,25,23},
{34.4,36.8,24,32,28,35,32,34},
{38.2,32.2,35,34,17,28,28,18},
{24.8,24.6,29,26,29,28,29,29},
{29.2,23.8,28,30,22,31,32,21},
{23.4,30.8,35,41,31,36,39,29},
{31.6,36.4,24,32,32,30,24,20},
{34.2,24.6,31,35,33,25,32,25},
{41.8,37.8,28,21,34,34,33,23},
{32.2,25.2,29,27,30,31,25,26},
{39.6,46.8,33,36,32,36,30,30},
{27.8,23.4,21,27,24,35,26,22},
{22.4,20.6,26,26,26,30,22,25},
{13.8,16,33,31,35,32,23,16},
{29.8,28,24,26,29,32,36,18},
{32,32,27,36,29,31,28,23},
{23,26.6,28,25,17,29,29,31},
{27.8,24.2,32,29,18,20,13,31},
{34.6,32,25,29,23,24,29,26},
{15.6,28.2,21,31,19,28,18,23},
{24.8,19.2,25,30,22,28,19,25},
{47.4,31.2,36,32,36,37,29,31},
{23.6,22.2,28,35,27,40,23,22},
{37.2,23.6,36,39,34,33,31,16},
{23.2,30.6,30,36,19,21,4,28},
{33.6,34.4,24,24,31,35,32,25},
{19.6,19.2,25,32,36,30,20,17},
{35.6,28.4,36,38,36,28,29,30},
{26.6,21,27,27,25,26,22,19},
{32.8,31,28,37,29,38,25,29},
{29.8,23.4,30,26,27,30,29,29},
{28,24,31,31,29,37,28,28},
{17.6,22.2,28,25,20,35,27,18},
{24.6,22,32,32,36,38,35,27},
{23.4,26,31,33,24,27,31,21},
{33.2,27,32,28,33,32,39,40},
{33.6,32,34,31,31,37,36,29},
{36.4,36.4,34,32,31,31,37,29},
{33,33.6,25,29,25,28,35,34}
    }; 
int main() {
     double test_data[n_features] = {31,	33,	30,	38,	31,	34,	31};

    // create a vector of pairs to store distance, name, and MBTI type
    vector<pair<double, pair<string, string>>> data_with_distances;

    // calculate distances and store in vector
    for (int i = 0; i < 54; i++) {
        double ptr_train[n_features];
        for (int j = 0; j < n_features; j++) {
            ptr_train[j] = train_data[i][j];
        }
        double distance = euclidean_distance(ptr_train, test_data, n_features);
        data_with_distances.push_back({distance, {Name_data[i], mbti_type_data[i]}});
    }

    // sort the vector by distance
    sort(data_with_distances.begin(), data_with_distances.end());

    // print the data with distances
    cout << setw(30) << "NAME" <<  setw(25) << "TYPE" << setw(20) << "DISTANCE" << endl;
    unordered_map<string, int> class_votes;
    int k = 13;
    for (int i = 0; i < k; i++) {
        string mbti_type = data_with_distances[i].second.second;
        if (class_votes.find(mbti_type) == class_votes.end()) {
            class_votes[mbti_type] = 1;
        } else {
            class_votes[mbti_type]++;
        }
        cout << "Neighbor " << i+1 << ": "  << setw(30) << data_with_distances[i].second.first 
             << setw(20) << data_with_distances[i].second.second 
             << setw(20) << data_with_distances[i].first << endl;;
    }
    // find the majority class and output the predicted MBTI type
    string predicted_type = "";
    int max_votes = 0;
    for (auto const& pair : class_votes) {
        if (pair.second > max_votes) {
            max_votes = pair.second;
            predicted_type = pair.first;
        }
    }
    cout << "Predicted MBTI type: " << predicted_type << endl;

    return 0;
}

