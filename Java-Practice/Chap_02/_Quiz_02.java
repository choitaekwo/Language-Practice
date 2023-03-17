package chap_02;

import java.util.Scanner;

public class _Quiz_02 {
	public static void main(String[] args) {
		
		// 퀴즈
		// 어린이 키에 따른 놀이기구 탑승 가능 여부를 확인하는 프로그램을 작성하시오
		
		double height;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("키를 입력하세요 : ");
		height = sc.nextDouble();
		
		String result = (height < 121) ? "키가 " + height + "이므로 탑승 불가능합니다" : "키가 " + height + "이므로 탑승 가능합니다";
		System.out.println(result);
		
		sc.close();
	}

}