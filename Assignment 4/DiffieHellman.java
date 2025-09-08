import java.math.BigInteger;
import java.util.*;

public class DiffieHellman {

    static boolean isPrimitiveRoot(BigInteger alpha, BigInteger prime) {
        BigInteger phi = prime.subtract(BigInteger.ONE);
        Set<BigInteger> factors = getPrimeFactors(phi);

        for (BigInteger factor : factors) {
            if (alpha.modPow(phi.divide(factor), prime).equals(BigInteger.ONE)) {
                return false;
            }
        }
        return true;
    }

    static Set<BigInteger> getPrimeFactors(BigInteger n) {
        Set<BigInteger> factors = new HashSet<>();
        BigInteger two = BigInteger.valueOf(2);

        while (n.mod(two).equals(BigInteger.ZERO)) {
            factors.add(two);
            n = n.divide(two);
        }

        for (BigInteger i = BigInteger.valueOf(3);
             i.multiply(i).compareTo(n) <= 0;
             i = i.add(two)) {

            while (n.mod(i).equals(BigInteger.ZERO)) {
                factors.add(i);
                n = n.divide(i);
            }
        }

        if (n.compareTo(BigInteger.ONE) > 0) {
            factors.add(n);
        }

        return factors;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a prime number (q): ");
        BigInteger prime = sc.nextBigInteger();

        System.out.print("Enter a primitive root modulo q (alpha): ");
        BigInteger g = sc.nextBigInteger();

        if (!isPrimitiveRoot(g, prime)) {
            System.out.println("The entered alpha is not a primitive root modulo " + prime);
            return;
        }

        System.out.print("Enter value of Xa: ");
        BigInteger privateKeyAlice = sc.nextBigInteger();

        System.out.print("Enter value of Xb: ");
        BigInteger privateKeyBob = sc.nextBigInteger();

        BigInteger publicKeyAlice = g.modPow(privateKeyAlice, prime); 
        BigInteger publicKeyBob   = g.modPow(privateKeyBob, prime);   

        System.out.println("\nPublic Key Calculation");
        System.out.println("Xa's Public Key: "+ publicKeyAlice);
        System.out.println("Xb's Public Key: "+ publicKeyBob);

        BigInteger sharedSecretAlice = publicKeyBob.modPow(privateKeyAlice, prime); 
        BigInteger sharedSecretBob   = publicKeyAlice.modPow(privateKeyBob, prime); 

        System.out.println("\n Shared Secret Calculation");
        System.out.println("Shared Secret (Ya): "+ sharedSecretAlice);
        System.out.println("Shared Secret (Yb): "+ sharedSecretBob);

        if (sharedSecretAlice.equals(sharedSecretBob)) {
            System.out.println("\n Both parties share the same secret key: " + sharedSecretAlice);
        } else {
            System.out.println("\n Secrets do not match.");
        }
        sc.close();
    }
}
