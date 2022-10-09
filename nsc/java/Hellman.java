public class Hellman {
    public static long power(int p, int g, int k){
        return (long)(Math.pow(g,k)%p);
    }

    public static void main(String[] args) {
        int p=11,g=2,a=8,b=4;
        long x = power(p,g,b);
        long y = power(p,g,a);
        System.out.println((long)Math.pow(x,a)%p);
        System.out.println((long)Math.pow(y,b)%p);
    }
}