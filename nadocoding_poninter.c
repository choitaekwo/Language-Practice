#include<stdio.h>

void change(int a, int b);
void change_addr(int* a, int* b);
void changeArray(int* arr2);

int main_nadocoding_pointer() {

	// �ּ� �� 
	int ö�� = 1;   // ��ȣ
	int ���� = 2;
	int �μ� = 3;

	printf("ö���� �ּ� : %p, ��ȣ : %d\n", &ö��, ö��);
	printf("����� �ּ� : %p, ��ȣ : %d\n", &����, ����);
	printf("�μ��� �ּ� : %p, ��ȣ : %d\n", &�μ�, �μ�);



	// ������ ����
	int* �̼Ǹ�;
	�̼Ǹ� = &ö��;

	int* �̼Ǹ�2 = &����;   // ����� ���ÿ� �ʱ�ȭ
	int* �̼Ǹ�3 = &�μ�;

	printf("�̼Ǹ��� �湮�ϴ� ���� �ּ� : %p, ��ȣ : %d\n", �̼Ǹ�, *�̼Ǹ�);
	printf("�̼Ǹ�2�� �湮�ϴ� ���� �ּ� : %p, ��ȣ : %d\n", �̼Ǹ�2, *�̼Ǹ�2);
	printf("�̼Ǹ�3�� �湮�ϴ� ���� �ּ� : %p, ��ȣ : %d\n", �̼Ǹ�3, *�̼Ǹ�3);

	// �̼� : �� ��ȣ�� 3�� ���ض�
	*�̼Ǹ� = *�̼Ǹ� * 3;
	*�̼Ǹ�2 = *�̼Ǹ�2 * 3;
	*�̼Ǹ�3 = *�̼Ǹ�3 * 3;

	printf("ö�� ��ȣ X 3 : %d\n", *�̼Ǹ�);
	printf("���� ��ȣ X 3 : %d\n", *�̼Ǹ�2);
	printf("�μ� ��ȣ X 3 : %d\n", *�̼Ǹ�3);

	// ������
	// �̼Ǹ��� �ٲ� ��ȣ���� 2�� ����
	int* ������ = �̼Ǹ�;   // �� ������ ������ ��� ö���� �ּ� ���� ����Ŵ
	int* ������2 = �̼Ǹ�2;
	int* ������3 = �̼Ǹ�3;

	*������ = *������ - 2;  // ö�� = ö�� - 2;
	*������2 = *������2 - 2;
	*������3 = *������3 - 2;

	printf("�����̰� �湮�ϴ� ���� �ּ� : %p, ��ȣ : %d\n", ������, *������);
	printf("������2�� �湮�ϴ� ���� �ּ� : %p, ��ȣ : %d\n", ������2, *������2);
	printf("������3�� �湮�ϴ� ���� �ּ� : %p, ��ȣ : %d\n", ������3, *������3);

	// ��ȣ�� ��¥�� �ٲ����� Ȯ��
	printf("ö���� �ּ� : %p, ��ȣ : %d\n", &ö��, ö��);
	printf("����� �ּ� : %p, ��ȣ : %d\n", &����, ����);
	printf("�μ��� �ּ� : %p, ��ȣ : %d\n", &�μ�, �μ�);

	// �̼Ǹ��� ��� ���� �ּ�
	printf("�̼Ǹ��� �ּ� : %p\n", &�̼Ǹ�);
	printf("�̼Ǹ�2�� �ּ� : %p\n", &�̼Ǹ�2);
	printf("�̼Ǹ�3�� �ּ� : %p\n", &�̼Ǹ�3);



	// �迭�� ������
	int arr[3] = { 5, 10 ,15 };
	int* parr = arr;

	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		printf("arr[%d] �� �� : %d\n", i, arr[i]);
	}
	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		printf("������ parr[%d] �� �� : %d\n", i, parr[i]);
	}

	parr[0] = 100;    // ������ ������ arr �� �� ����
	parr[1] = 200;
	parr[2] = 300;

	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		//printf("arr[%d] �� �� : %d\n", i, arr[i]);
		printf("arr[%d] �� �� : %d\n", i, *(arr + i));
	}
	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		//printf("������ parr[%d] �� �� : %d\n", i, parr[i]);
		printf("������ parr[%d] �� �� : %d\n", i, *(parr + i));
	}

	// *(arr + i) == arr[i]  �Ȱ��� ǥ��
	// arr == arr �迭�� ù ��° ���� �ּҿ� ���� == &arr[0]
	printf("arr ��ü�� �� : %p\n", arr);
	printf("arr[0] �� �ּ� : %p\n", &arr[0]);

	printf("arr ��ü�� ���� ������ �ּ��� ���� �� : %d\n", *arr);  // * (arr + 0)
	printf("arr[0] �� ���� �� : %d\n", arr[0]);

	// �����ͷ� �迭 �� �����ϱ�
	int arr2[3] = { 10, 20, 30 };

	changeArray(arr2);        // �迭�� �� -> arr2 -> �ּ�
	//changeArray(&arr2[0]);    // arr2 == &arr[0]

	for (int i = 0; i < sizeof(arr2) / sizeof(int); i++)
	{
		printf("arr[%d] : %d\n", i, arr2[i]);
	}



	// a �� b �� �� �ٲٱ� (swap)
	int a = 10;
	int b = 20;

	printf("a �� �ּ� : %p\n", &a);
	printf("b �� �ּ� : %p\n", &b);

	printf("swap �Լ� �� => a : %d, b : %d\n", a, b);

	change(a, b);

	printf("swap �Լ� �� => a : %d, b : %d\n", a, b);

	// �ּҰ� ����
	printf("(�ּҰ� ����) swap �Լ� �� => a : %d, b : %d\n", a, b);

	change_addr(&a, &b);

	printf("(�ּҰ� ����) swap �Լ� �� => a : %d, b : %d\n", a, b);


	return 0;
}

void change(int a, int b)  // ���� ���� ���� ( Call by Value ) -> ���� �����Ѵٴ� �ǹ�
{
	printf("swap �Լ� ���� a �� �ּ� : %p\n", &a);  // main�Լ��� a, b �� chagne�Լ� ���� a, b �� �ٸ�
	printf("swap �Լ� ���� b �� �ּ� : %p\n", &b);

	int temp;

	temp = a;
	a = b;
	b = temp;

	printf("swap �Լ� ���� => a : %d, b : %d\n", a, b);
}
void change_addr(int* a, int* b)   // �ּҰ� ����
{
	int temp;

	temp = *a;
	*a = *b;
	*b = temp;

	printf("(�ּҰ� ����) swap �Լ� ���� => a : %d, b : %d\n", *a, *b);
}
void changeArray(int* arr2)
{
	arr2[2] = 50;
}