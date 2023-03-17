#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

// 부모 클래스
class Animal {
private:
	int legs;
	char name[50];

public:
	Animal(int legs, const char* name) {
		cout << "Animal 생성자가 실행됨" << endl;
		this->legs = legs;
		strcpy(this -> name, name);
	}

	void printAnimalInfo() {

		cout << "다리의 갯수 : " << legs << endl;
		cout << "이름 : " << name << endl;
	}

	void printlegs() {
		cout << "Person 의 다리의 개수 : " << this->legs << endl;
	}
};

// 자식 클래스
class Person : public Animal{
public:
	char regist_no[30];

	Person(const char* regist_no) : Animal(2, "사람") {

		cout << "Person 생성자가 실행됨" << endl;
		strcpy(this->regist_no, regist_no);
	}
	
};

class Dog : public Animal {
public:
	Dog() : Animal(4, "개") {
		cout << "Dog 생성자가 실행됨" << endl;
	}
};

int main_class() {

	Person* p = new Person("1234-1234");
	//p->printAnimalInfo();
	cout << "Person 의 다리의 개수 : " << endl;//p->legs << endl;

	Dog* d = new Dog();
	//d->printAnimalInfo();

	return 0;
}
