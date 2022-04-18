public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        System.out.println(gcd(20,8));
    }
    public static int gcd(int a,int b){
        return b==0 ? a : gcd(b, a%b); 
    }
}
