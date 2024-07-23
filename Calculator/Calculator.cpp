#include <iostream>
#include <vector>
#include <fstream>
#include <stdexcept>
#include <map>
#include <memory>
#include <string>

// Base class with virtual functions
class Operation {
public:
    virtual double execute(double a, double b) = 0; // Pure virtual function
};

class Add : public Operation {
public:
    double execute(double a, double b) override {
        return a + b;
    }
};

class Subtract : public Operation {
public:
    double execute(double a, double b) override {
        return a - b;
    }
};

class Multiply : public Operation {
public:
    double execute(double a, double b) override {
        return a * b;
    }
};

class Divide : public Operation {
public:
    double execute(double a, double b) override {
        if (b == 0) {
            throw std::invalid_argument("Division by zero is not allowed.");
        }
        return a / b;
    }
};

// Function to read from a file
void readFromFile(const std::string& filename, std::vector<std::string>& history) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file " << filename << std::endl;
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        history.push_back(line);
    }
    file.close();
}

// Function to write to a file
void writeToFile(const std::string& filename, const std::vector<std::string>& history) {
    std::ofstream file(filename, std::ios::app);
    if (!file.is_open()) {
        std::cerr << "Error opening file " << filename << std::endl;
        return;
    }

    for (const auto& entry : history) {
        file << entry << std::endl;
    }
    file.close();
}

int main() {
    std::map<char, std::unique_ptr<Operation>> operations;
    operations['+'] = std::make_unique<Add>();
    operations['-'] = std::make_unique<Subtract>();
    operations['*'] = std::make_unique<Multiply>();
    operations['/'] = std::make_unique<Divide>();

    std::vector<std::string> history;
    std::string filename = "calc_history.txt";

    // Read previous history from the file
    readFromFile(filename, history);

    char choice;
    do {
        std::cout << "\nEnter operation (+, -, *, /) or 'q' to quit: ";
        std::cin >> choice;

        if (choice == 'q') {
            break;
        }

        if (operations.find(choice) == operations.end()) {
            std::cerr << "Invalid operation" << std::endl;
            continue;
        }

        double num1, num2;
        std::cout << "Enter first number: ";
        std::cin >> num1;
        std::cout << "Enter second number: ";
        std::cin >> num2;

        try {
            double result = operations[choice]->execute(num1, num2);
            std::cout << "Result: " << result << std::endl;
            history.push_back(std::to_string(num1) + " " + choice + " " + std::to_string(num2) + " = " + std::to_string(result));
        } catch (const std::invalid_argument& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }

    } while (true);

    // Write history to the file
    writeToFile(filename, history);

    return 0;
}
