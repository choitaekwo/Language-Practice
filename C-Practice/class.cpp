#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

// �θ� Ŭ����
class Animal {
private:
	int legs;
	char name[50];

public:
	Animal(int legs, const char* name) {
		cout << "Animal �����ڰ� �����" << endl;
		this->legs = legs;
		strcpy(this -> name, name);
	}

	void printAnimalInfo() {

		cout << "�ٸ��� ���� : " << legs << endl;
		cout << "�̸� : " << name << endl;
	}

	void printlegs() {
		cout << "Person �� �ٸ��� ���� : " << this->legs << endl;
	}
};

// �ڽ� Ŭ����
class Person : public Animal{
public:
	char regist_no[30];

	Person(const char* regist_no) : Animal(2, "���") {

		cout << "Person �����ڰ� �����" << endl;
		strcpy(this->regist_no, regist_no);
	}
	
};

class Dog : public Animal {
public:
	Dog() : Animal(4, "��") {
		cout << "Dog �����ڰ� �����" << endl;
	}
};

int main_class() {

	Person* p = new Person("1234-1234");
	//p->printAnimalInfo();
	cout << "Person �� �ٸ��� ���� : " << endl;//p->legs << endl;

	Dog* d = new Dog();
	//d->printAnimalInfo();

	return 0;
}
