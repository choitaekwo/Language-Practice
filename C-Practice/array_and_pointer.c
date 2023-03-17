#include<stdio.h>

void print_array(int* parray, int size);
void input_array(double* parray, int size);
double find_max(int* parray, int size);
void input_nums(int* lotto_nums);
void print_nums(int* lotto_nums);

int main_array_and_pointer() {

	// �迭�� ������                                                            // *(arr + i) == arr[i]  �Ȱ��� ǥ��
																			   // arr == arr �迭�� ù ��° ���� �ּҿ� ���� == &arr[0]
	// �迭�� ���� ������ �����Ͽ� �迭 ��� ���
	int ary[3] = { 0 };

	*(ary + 0) = 10;   // ary[0] = 10
	*(ary + 1) = *(ary + 0) + 10;    // ary[1] = ary[0] + 10

	printf("�� ��° �迭 ��ҿ� Ű���� �Է� : ");
	scanf_s("%d", ary + 2);   // &ary[2]

	for (int i = 0; i < 3; i++)
	{
		printf("%5d", *(ary + i));   // ary[i]
	}
	printf("\n\n");


	// �迭��ó�� ���Ǵ� ������
	int ary2[3] = { 0 };
	int* pary2 = ary2;    // �����Ϳ� �迭�� ����

	*pary2 = 10;    // ù ��° �迭 ��ҿ� 10 ����
	*(pary2 + 1) = 20;  // �� ���� 20 ����
	pary2[2] = pary2[0] + pary2[2];   // ���ȣ�� �Ἥ pary2 �� �迭��ó�� ���

	for (int i = 0; i < 3; i++)
	{
		printf("%5d", pary2[i]);
	}
	printf("\n\n");


	// �����͸� �̿��� �迭�� �� ���
	int ary3[3] = { 10, 20, 30 };
	int* pary3;
	pary3 = &ary3;

	printf("�迭�� �� : ");
	for (int i = 0; i < sizeof(ary3) / sizeof(int); i++)
	{
		printf("%5d", *pary3);   // pary3 �� ����Ű�� �迭 ��� ���
		pary3++;            // ���� �迭 ��Ҹ� ����Ű���� pary3 �� ����
	}
	printf("\n\n");


	// �������� ������ ���� ����
	int ary4[5] = { 10, 20, 30, 40, 50 };
	int* pary4 = ary4;     // ù ��° �迭 ��� �ּ�
	int* pb = pary4 + 3;   // �� ��° �迭 ��� �ּ�

	printf("pary4 : %u\n", pary4);
	printf("pb : %u\n", pb);
	pary4++; // ���� �迭 ��ҷ� �̵�
	printf("pb - pary4 : %u\n", pb - pary4);   // �� �������� ����    // �迭 ��� ���� ���� ����

	printf("�տ� �ִ� �迭 ����� �� ��� : ");
	if (pary4 < pb) printf("%d\n", *pary4);
	else printf("%d\n", *pb);


	// �迭�� ó���ϴ� �Լ�
	int array[5] = { 10, 20, 30, 40, 50 };
	int array2[7] = { 1, 2, 3, 4, 5, 6, 7 };

	print_array(array, sizeof(array) / sizeof(int));   // �迭���� �ְ� �Լ� ȣ��
	printf("\n");
	print_array(array2, sizeof(array2) / sizeof(int));
	printf("\n");

	// �迭�� ���� �Է��ϴ� �Լ�
	double array3[5];
	double max;

	int size = sizeof(array3) / sizeof(array3[0]);

	input_array(array3, size);
	max = find_max(array3, size);

	printf("�迭�� �ִ밪 : %.1lf\n", max);


	// ���� �������� 10�� // �ζ� ��ȣ ���� ���α׷�
	int lotto_nums[6];
	input_nums(lotto_nums);
	print_nums(lotto_nums);

	return 0;
}
void print_array(int* parray, int size)
{
	for (int i = 0; i < size; i++)
	{
		printf("%d ", parray[i]);
	}
}

void input_array(double* parray, int size)
{
	printf("%d�� �Ǽ� �� �Է� : ", size);
	for (int i = 0; i < size; i++)
	{
		scanf_s("%lf", parray + i);
	}
}

double find_max(double* parray, int size)
{
	double max = parray[0];
	for (int i = 1; i < size; i++)
	{
		if (parray[i] > max)
		{
			max = parray[i];
		}
	}
	return max;
}

void input_nums(int* lotto_nums)
{
	for (int i = 0; i < 6; i++)
	{
		printf("��ȣ �Է� : ");
		scanf_s("%d", lotto_nums + i);

		if (lotto_nums[i] == lotto_nums[i - 1])
		{
			printf("���� ��ȣ�� �ֽ��ϴ�!\n");
			i--;
		}
	}
}

void print_nums(int* lotto_nums)
{
	printf("�ζ� ��ȣ : ");
	for (int i = 0; i < 6; i++)
	{
		printf("%d\t", lotto_nums[i]);
	}
}

void checking_grade(int* lotto_nums)     // �̸� ��ȣ 6�� �����س��� ��������� �Է� �ް� �� �� �¾Ҵ��� Ȯ���ؼ� ��� �˷��ֱ�
{

}