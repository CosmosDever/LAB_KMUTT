#include <bits/stdc++.h>
using namespace std;

struct Student {
    string name;
    int score;
};

vector<Student> students;

// Function to calculate MaxStudent
Student MaxStudent() {
    int maxScore = 0;
    Student maxStudent;
    for (int i = 0; i < students.size(); i++) {
        if (students[i].score > maxScore) {
            maxScore = students[i].score;
            maxStudent = students[i];
        }
    }
    return maxStudent;
}

// Function to calculate MinStudent
Student MinStudent() {
    int minScore = -1;
    Student minStudent;
    for (int i = 0; i < students.size(); i++) {
        if (students[i].score < minScore || minScore == -1) {
            minScore = students[i].score;
            minStudent = students[i];
        }
    }
    return minStudent;
}

// Function to calculate AvrScore
int AvrScore() {
    int sum = 0;
    for (int i = 0; i < students.size(); i++) {
        sum += students[i].score;
    }
    return sum / students.size();
}

// Function to calculate ModeScore
int ModeScore() {
    int maxCount = 0;
    int modeScore = 0;
    for (int i = 0; i < students.size(); i++) {
        int count = 0;
        for (int j = 0; j < students.size(); j++) {
            if (students[i].score == students[j].score) 
                count++;
        }

        if (count > maxCount) {
            maxCount = count;
            modeScore = students[i].score;
        }
    }
    return modeScore;
}

// Function to calculate MedianScore
int MedianScore() {
    vector<int> scores;
    for (int i = 0; i < students.size(); i++) {
        scores.push_back(students[i].score);
    }
    sort(scores.begin(), scores.end());
    int mid = students.size() / 2;
    if (students.size() % 2 == 1) 
        return scores[mid];
    else 
        return (scores[mid] + scores[mid-1]) / 2;
}

// Function to calculate SDScore
double SDScore() {
    int sum = 0;
    double avg = AvrScore();
    for (int i = 0; i < students.size(); i++) {
        sum += (students[i].score - avg)*(students[i].score - avg);
    }
    return sqrt(sum / students.size());
}

// Function to calculate the grade for each student
char Grade(int score) {
    int avr = AvrScore();
    double sd = SDScore();
    if (score > avr + 2*sd)
        return 'A';
    else if (score > avr + sd) 
        return 'B';
    else if (score > avr)
        return 'C';
    else if (score > avr - sd)
        return 'D';
    else
        return 'F';
}

int main() {
    // Input student data
    for (int i = 0; i < 10; i++) {
        Student s;
        cout << "Enter student " << i+1 << "'s name: ";
        cin >> s.name;
        cout << "Enter student " << i+1 << "'s score: ";
        cin >> s.score;
        students.push_back(s);
    }

    // Calculate MaxStudent
    Student maxStudent = MaxStudent();
    cout << "MaxStudent: " << maxStudent.name << endl;

    // Calculate MinStudent
    Student minStudent = MinStudent();
    cout << "MinStudent: " << minStudent.name << endl;

    // Calculate AvrScore
    int avrScore = AvrScore();
    cout << "AvrScore: " << avrScore << endl;

    // Calculate ModeScore
    int modeScore = ModeScore();
    cout << "ModeScore: " << modeScore << endl;

    // Calculate MedianScore
    int medianScore = MedianScore();
    cout << "MedianScore: " << medianScore << endl;

    // Calculate SDScore
    double sdScore = SDScore();
    cout << "SDScore: " << sdScore << endl;

    // Calculate grade for each student
    for (int i = 0; i < students.size(); i++) {
        cout << "Student " << students[i].name << ": " << Grade(students[i].score) << endl;
    }

    return 0;
}
