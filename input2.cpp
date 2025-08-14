#include <iostream>
#include <string>
using namespace std;

// Structure to represent a student
struct Student {
    string name;
    int rollNumber;
    float gpa;
};

// Function to display student details
void printStudent(const Student& s) {
    cout << "Student Name: " << s.name << endl;
    cout << "Roll Number: " << s.rollNumber << endl;
    cout << "GPA: " << s.gpa << endl;
}

// Function to find top student
Student getTopper(Student students[], int size) {
    float maxGPA = -1.0;
    int topperIndex = -1;

    for (int i = 0; i < size; i++) {
        if (students[i].gpa > maxGPA) {
            maxGPA = students[i].gpa;
            topperIndex = i;
        }
    }

    return students[topperIndex];
}

int main() {
    Student students[3] = {
        {"Alice", 101, 3.8},
        {"Bob", 102, 3.5},
        {"Charlie", 103, 3.9}
    };

    for (int i = 0; i < 3; i++) {
        printStudent(students[i]);
    }

    Student topper = getTopper(students, 3);
    cout << "Topper is: " << topper.name << " with GPA: " << topper.gpa << endl;

    return 0;
}
