#include<stdio.h>

void print_array(int* parray, int size);
void input_array(double* parray, int size);
double find_max(int* parray, int size);
void input_nums(int* lotto_nums);
void print_nums(int* lotto_nums);

int main_array_and_pointer() {

	// 배열과 포인터                                                            // *(arr + i) == arr[i]  똑같은 표현
					                             // arr == arr 배열의 첫 번째 값의 주소와 동일 == &arr[0]
	// 배열명에 정수 연산을 수행하여 배열 요소 사용
	int ary[3] = { 0 };

	*(ary + 0) = 10;   // ary[0] = 10
	*(ary + 1) = *(ary + 0) + 10;    // ary[1] = ary[0] + 10

	printf("세 번째 배열 요소에 키보드 입력 : ");
	scanf_s("%d", ary + 2);   // &ary[2]

	for (int i = 0; i < 3; i++)
	{
		printf("%5d", *(ary + i));   // ary[i]
	}
	printf("\n\n");


	// 배열명처럼 사용되는 포인터
	int ary2[3] = { 0 };
	int* pary2 = ary2;    // 포인터에 배열명 저장

	*pary2 = 10;    // 첫 번째 배열 요소에 10 대입
	*(pary2 + 1) = 20;  // 두 번재 20 대입
	pary2[2] = pary2[0] + pary2[2];   // 대괄호를 써서 pary2 를 배열명처럼 사용

	for (int i = 0; i < 3; i++)
	{
		printf("%5d", pary2[i]);
	}
	printf("\n\n");


	// 포인터를 이용한 배열의 값 출력
	int ary3[3] = { 10, 20, 30 };
	int* pary3;
	pary3 = &ary3;

	printf("배열의 값 : ");
	for (int i = 0; i < sizeof(ary3) / sizeof(int); i++)
	{
		printf("%5d", *pary3);   // pary3 가 가리키는 배열 요소 출력
		pary3++;            // 다음 배열 요소를 가리키도록 pary3 값 증가
	}
	printf("\n\n");


	// 포인터의 뺄셈과 관계 연산
	int ary4[5] = { 10, 20, 30, 40, 50 };
	int* pary4 = ary4;     // 첫 번째 배열 요소 주소
	int* pb = pary4 + 3;   // 네 번째 배열 요소 주소

	printf("pary4 : %u\n", pary4);
	printf("pb : %u\n", pb);
	pary4++; // 다음 배열 요소로 이동
	printf("pb - pary4 : %u\n", pb - pary4);   // 두 포인터의 뺄셈    // 배열 요소 간의 간격 차이

	printf("앞에 있는 배열 요소의 값 출력 : ");
	if (pary4 < pb) printf("%d\n", *pary4);
	else printf("%d\n", *pb);


	// 배열을 처리하는 함수
	int array[5] = { 10, 20, 30, 40, 50 };
	int array2[7] = { 1, 2, 3, 4, 5, 6, 7 };

	print_array(array, sizeof(array) / sizeof(int));   // 배열명을 주고 함수 호출
	printf("\n");
	print_array(array2, sizeof(array2) / sizeof(int));
	printf("\n");

	// 배열에 값을 입력하는 함수
	double array3[5];
	double max;

	int size = sizeof(array3) / sizeof(array3[0]);

	input_array(array3, size);
	max = find_max(array3, size);

	printf("배열의 최대값 : %.1lf\n", max);


	// 도전 실전예제 10장 // 로또 번호 생성 프로그램
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
	printf("%d개 실수 값 입력 : ", size);
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
		printf("번호 입력 : ");
		scanf_s("%d", lotto_nums + i);

		if (lotto_nums[i] == lotto_nums[i - 1])
		{
			printf("같은 번호가 있습니다!\n");
			i--;
		}
	}
}

void print_nums(int* lotto_nums)
{
	printf("로또 번호 : ");
	for (int i = 0; i < 6; i++)
	{
		printf("%d\t", lotto_nums[i]);
	}
}

void checking_grade(int* lotto_nums)     // 미리 번호 6개 생성해놓고 사용자한테 입력 받고 몇 개 맞았는지 확인해서 등수 알려주기
{

}
