import java.io.*;
import java.util.*;

public class Main {
	static int[][] fibo = new int[41][2]; // 0~40
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		fibo[0][0] = 1; fibo[0][1] = 0;
		fibo[1][0] = 0; fibo[1][1] = 1;
		for(int i=2;i<=40;i++) {
			fibo[i][0] = fibo[i-1][1];
			fibo[i][1] = fibo[i-1][1] + fibo[i-2][1];
		}
		for(int i=0;i<TC;i++) {
			int N = Integer.parseInt(br.readLine());
			System.out.println(fibo[N][0]+" "+fibo[N][1]);
		}
	}
}
