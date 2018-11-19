// 11718 그대로 출력하기 
// https://www.acmicpc.net/user/kqkdn

import java.io.IOException;
import java.util.Scanner;
 
public class Main{
    public static void main(String args[]) throws IOException{
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextLine()){
            System.out.println(sc.nextLine());
        }    
        sc.close();
    }
}
