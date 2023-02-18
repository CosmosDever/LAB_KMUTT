#include <bits/stdc++.h>

using namespace std;

struct ScoreboardEntry
{
    string name;
    double points;
    ScoreboardEntry* prev;
    ScoreboardEntry* next;
};

class Scoreboard
{
private:
    ScoreboardEntry* head;
    ScoreboardEntry* tail;
    int size = 0;

public:
    Scoreboard()
    {
        head = NULL;
        tail = NULL;
    }

    void insert(string name, double points)
    {
        ScoreboardEntry* ne = new ScoreboardEntry;
        ne->name = name;
        ne->points = points;
        ne->prev = NULL;
        ne->next = NULL;

        if (head == NULL) {
            head = ne;
            tail = ne;
            size++;
        }
        else {
            ScoreboardEntry* curr = head;
            while ((curr != NULL) && (curr->points > points)) {
                curr = curr->next;
            }
            if (curr == NULL) {
                tail->next = ne;
                ne->prev = tail;
                tail = ne;
                size++;
            }
            else {
                ne->next = curr;
                ne->prev = curr->prev;
                curr->prev = ne;
                if (curr == head) {
                    head = ne;
                }
                else {
                    ne->prev->next = ne;
                }
                size++;
            }
            if (size > 10) {
                ScoreboardEntry* curr = tail;
                tail = curr->prev;
                tail->next = NULL;
                delete curr;
                size--;
            }
        }
    }
    void display()
    {
        ScoreboardEntry* curr = head;
        int rank = 1;
        cout << "Rank\tName\tPoints" << endl;
        while (curr != NULL)
        {
            cout << rank << "\t" << curr->name << "\t" << curr->points << endl;
            curr = curr->next;
            rank++;
        }
    }
};
int main()
{
    string newname;
    int newscore;
    Scoreboard s;
    s.insert("John", 1000);
    s.insert("Jim", 800);
    s.insert("Bob", 900);
    s.insert("David", 1100);
    s.insert("Tom", 700);
    s.insert("Jerry", 1200);
    s.insert("Folk", 120);
    s.insert("Deaw", 670);
    s.insert("Pluem", 98);
    s.insert("Poom", 1200);
    s.display();
    cout <<"Enter new name and score \n";
    cin >> newname;
    cin >> newscore;
    s.insert(newname, newscore);
    s.display(); 
    return 0;
}
