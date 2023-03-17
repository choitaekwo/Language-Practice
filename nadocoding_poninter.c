#include<stdio.h>

void change(int a, int b);
void change_addr(int* a, int* b);
void changeArray(int* arr2);

int main_nadocoding_pointer() {

	// 주소 값 
	int 철수 = 1;   // 암호
	int 영희 = 2;
	int 민수 = 3;

	printf("철수네 주소 : %p, 암호 : %d\n", &철수, 철수);
	printf("영희네 주소 : %p, 암호 : %d\n", &영희, 영희);
	printf("민수네 주소 : %p, 암호 : %d\n", &민수, 민수);



	// 포인터 선언
	int* 미션맨;
	미션맨 = &철수;

	int* 미션맨2 = &영희;   // 선언과 동시에 초기화
	int* 미션맨3 = &민수;

	printf("미션맨이 방문하는 곳의 주소 : %p, 암호 : %d\n", 미션맨, *미션맨);
	printf("미션맨2이 방문하는 곳의 주소 : %p, 암호 : %d\n", 미션맨2, *미션맨2);
	printf("미션맨3이 방문하는 곳의 주소 : %p, 암호 : %d\n", 미션맨3, *미션맨3);

	// 미션 : 각 암호에 3을 곱해라
	*미션맨 = *미션맨 * 3;
	*미션맨2 = *미션맨2 * 3;
	*미션맨3 = *미션맨3 * 3;

	printf("철수 암호 X 3 : %d\n", *미션맨);
	printf("영희 암호 X 3 : %d\n", *미션맨2);
	printf("민수 암호 X 3 : %d\n", *미션맨3);

	// 스파이
	// 미션맨이 바꾼 암호에서 2를 빼라
	int* 스파이 = 미션맨;   // 두 포인터 변수가 모두 철수의 주소 값을 가리킴
	int* 스파이2 = 미션맨2;
	int* 스파이3 = 미션맨3;

	*스파이 = *스파이 - 2;  // 철수 = 철수 - 2;
	*스파이2 = *스파이2 - 2;
	*스파이3 = *스파이3 - 2;

	printf("스파이가 방문하는 곳의 주소 : %p, 암호 : %d\n", 스파이, *스파이);
	printf("스파이2가 방문하는 곳의 주소 : %p, 암호 : %d\n", 스파이2, *스파이2);
	printf("스파이3가 방문하는 곳의 주소 : %p, 암호 : %d\n", 스파이3, *스파이3);

	// 암호가 진짜로 바꼇는지 확인
	printf("철수네 주소 : %p, 암호 : %d\n", &철수, 철수);
	printf("영희네 주소 : %p, 암호 : %d\n", &영희, 영희);
	printf("민수네 주소 : %p, 암호 : %d\n", &민수, 민수);

	// 미션맨이 사는 곳의 주소
	printf("미션맨의 주소 : %p\n", &미션맨);
	printf("미션맨2의 주소 : %p\n", &미션맨2);
	printf("미션맨3의 주소 : %p\n", &미션맨3);



	// 배열과 포인터
	int arr[3] = { 5, 10 ,15 };
	int* parr = arr;

	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		printf("arr[%d] 의 값 : %d\n", i, arr[i]);
	}
	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		printf("포인터 parr[%d] 의 값 : %d\n", i, parr[i]);
	}

	parr[0] = 100;    // 포인터 변수로 arr 의 값 변경
	parr[1] = 200;
	parr[2] = 300;

	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		//printf("arr[%d] 의 값 : %d\n", i, arr[i]);
		printf("arr[%d] 의 값 : %d\n", i, *(arr + i));
	}
	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
	{
		//printf("포인터 parr[%d] 의 값 : %d\n", i, parr[i]);
		printf("포인터 parr[%d] 의 값 : %d\n", i, *(parr + i));
	}

	// *(arr + i) == arr[i]  똑같은 표현
	// arr == arr 배열의 첫 번째 값의 주소와 동일 == &arr[0]
	printf("arr 자체의 값 : %p\n", arr);
	printf("arr[0] 의 주소 : %p\n", &arr[0]);

	printf("arr 자체의 값이 가지는 주소의 실제 값 : %d\n", *arr);  // * (arr + 0)
	printf("arr[0] 의 실제 값 : %d\n", arr[0]);

	// 포인터로 배열 값 변경하기
	int arr2[3] = { 10, 20, 30 };

	changeArray(arr2);        // 배열일 때 -> arr2 -> 주소
	//changeArray(&arr2[0]);    // arr2 == &arr[0]

	for (int i = 0; i < sizeof(arr2) / sizeof(int); i++)
	{
		printf("arr[%d] : %d\n", i, arr2[i]);
	}



	// a 와 b 의 값 바꾸기 (swap)
	int a = 10;
	int b = 20;

	printf("a 의 주소 : %p\n", &a);
	printf("b 의 주소 : %p\n", &b);

	printf("swap 함수 전 => a : %d, b : %d\n", a, b);

	change(a, b);

	printf("swap 함수 후 => a : %d, b : %d\n", a, b);

	// 주소값 전달
	printf("(주소값 전달) swap 함수 전 => a : %d, b : %d\n", a, b);

	change_addr(&a, &b);

	printf("(주소값 전달) swap 함수 후 => a : %d, b : %d\n", a, b);


	return 0;
}

void change(int a, int b)  // 값에 의한 복사 ( Call by Value ) -> 값만 복사한다는 의미
{
	printf("swap 함수 내부 a 의 주소 : %p\n", &a);  // main함수의 a, b 와 chagne함수 내의 a, b 는 다름
	printf("swap 함수 내부 b 의 주소 : %p\n", &b);

	int temp;

	temp = a;
	a = b;
	b = temp;

	printf("swap 함수 내부 => a : %d, b : %d\n", a, b);
}
void change_addr(int* a, int* b)   // 주소값 전달
{
	int temp;

	temp = *a;
	*a = *b;
	*b = temp;

	printf("(주소값 전달) swap 함수 내부 => a : %d, b : %d\n", *a, *b);
}
void changeArray(int* arr2)
{
	arr2[2] = 50;
}