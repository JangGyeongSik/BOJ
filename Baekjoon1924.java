// Baekjoon1924 날짜계산 
// https://www.acmicpc.net/user/kqkdn
import java.util.Scanner;

class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        int W = 0;
        
        if(x == 1 || x ==2)
	    {
	    	x += 12;
	    	W = (26 * (x + 1) / 10) + y - 1;
    	}
    	else if(x >= 3)
    	{
    		W = (26 * (x + 1) / 10) + y;
    	}
        
        int Key = W % 7;
        
       	if(Key == 0)
    		System.out.printf("SUN\n");
    	else if(Key == 1)
    		System.out.printf("MON\n");
    	else if(Key == 2)
    		System.out.printf("TUE\n");
    	else if(Key == 3)
    		System.out.printf("WED\n");
    	else if(Key == 4)
    		System.out.printf("THU\n");
    	else if(Key == 5)
    		System.out.printf("FRI\n");
    	else if(Key == 6)
    		System.out.printf("SAT\n");
    }
}
