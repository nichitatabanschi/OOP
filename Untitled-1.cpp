#include <iostream>
#include <string>

class Person {
public:
    // Constructor
    Person(std::string name, int age) {
        this->name = name;
        this->age = age;
    }

    // Member function to set the name
    void setName(std::string newName) {
        name = newName;
    }

    // Member function to set the age
    void setAge(int newAge) {
        age = newAge;
    }

    // Member function to display person's information
    void displayInfo() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Age: " << age << std::endl;
    }

private:
    std::string name;
    int age;
};

int main() {
    // Create an instance of the Person class
    Person person1("John Doe", 30);

    // Display the initial information
    std::cout << "Initial Information:" << std::endl;
    person1.displayInfo();

    // Update the information
    person1.setName("Jane Doe");
    person1.setAge(25);

    // Display the updated information
    std::cout << "\nUpdated Information:" << std::endl;
    person1.displayInfo();

    return 0;
}
