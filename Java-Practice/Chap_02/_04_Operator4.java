package chap_02;

public class _04_Operator4 {
	public static void main(String[] args) {
		
		// 논리 연산자
		boolean kimchi = false;
		boolean egg = false;
		boolean pork = true;
		
		System.out.println(kimchi || egg || pork);  // 하나라도 true이면 true
		System.out.println(kimchi && egg && pork);  // 모두 true일 때 true
		
		System.out.println((5 > 3) && (3 > 1));  // 5는 3보다 크고 3은 1보다 크다
		System.out.println((5 > 3) && (3 < 1));  // 5는 3보다 크고 3은 1보다 작다
		
		System.out.println((5 > 3) || (3 > 1));  // 5는 3보다 크거나 3은 1보다 크다
		System.out.println((5 < 3) || (3 < 1));  // 5는 3보다 작거나 3은 1보다 작다
		
		System.out.println(!true);
		System.out.println(!false);
		System.out.println(!(5 == 5));
		System.out.println(!(5 == 3));
	}
}
