import java.math.BigInteger;
import java.util.Scanner;

public class RSA {

    public static BigInteger gcd(BigInteger a , BigInteger b){
        if(b.compareTo(new BigInteger("0")) == 0){
            return a;
        }
        return gcd(b,a.mod(b));
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Take two random prime numbers.
        System.out.print("Enter prime 1 : ");
        BigInteger p = sc.nextBigInteger();
        System.out.print("Enter Prime 2 : ");
        BigInteger q = sc.nextBigInteger();

        // To find first part of public key.
        BigInteger n = p.multiply(q);

        // To find second part of public key.
        // e stands for encrypt.
        BigInteger e = new BigInteger("2");

        BigInteger pi_n = (p.subtract(new BigInteger("1"))).multiply(q.subtract(new BigInteger("1")));
        while (e.compareTo(pi_n) < 0){
            if (gcd(e,pi_n).compareTo(new BigInteger("1")) == 0){
                break;
            }
            e = e.add(new BigInteger("1"));
        }

        BigInteger d = new BigInteger("2");
        while (d.compareTo(pi_n) < 0){
            if (((d.multiply(e).mod(pi_n)).compareTo(new BigInteger("1")) == 0)){
                break;
            }
            d = d.add(new BigInteger("1"));
        }


        // To generate the private key.
        System.out.print("Enter Message Data : ");
        BigInteger msg = sc.nextBigInteger();
    
        BigInteger encrypted = (msg.pow(e.intValue())).mod(n);
        System.out.println("Encrypted Data : "+encrypted);


        BigInteger decrypted = (encrypted.pow(d.intValue())).mod(n);
        System.out.println("Decrypted Data : "+decrypted);

    }
}