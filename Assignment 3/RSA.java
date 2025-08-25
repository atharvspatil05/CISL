import java.math.BigInteger;
import java.util.Scanner;

public class RSA {
    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static BigInteger gcd(BigInteger a, BigInteger b) {
        while (!b.equals(BigInteger.ZERO)) {
            BigInteger temp = b;
            b = a.mod(b);
            a = temp;
        }
        return a;
    }

    public static BigInteger modinv(BigInteger e, BigInteger phi) {
        BigInteger d = BigInteger.ZERO, x1 = BigInteger.ZERO, x2 = BigInteger.ONE, y1 = BigInteger.ONE;
        BigInteger tempPhi = phi;
        while (e.compareTo(BigInteger.ZERO) > 0) {
            BigInteger temp1 = tempPhi.divide(e);
            BigInteger temp2 = tempPhi.subtract(temp1.multiply(e));
            tempPhi = e;
            e = temp2;

            BigInteger x = x2.subtract(temp1.multiply(x1));
            BigInteger y = d.subtract(temp1.multiply(y1));

            x2 = x1;
            x1 = x;
            d = y1;
            y1 = y;
        }
        if (tempPhi.equals(BigInteger.ONE)) return d.add(phi);
        return null;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter first prime number (p): ");
            int p = sc.nextInt();
            System.out.print("Enter second prime number (q): ");
            int q = sc.nextInt();

            if (!isPrime(p) || !isPrime(q)) {
                System.out.println("Both numbers must be prime.");
                return;
            }

            BigInteger P = BigInteger.valueOf(p);
            BigInteger Q = BigInteger.valueOf(q);
            BigInteger n = P.multiply(Q);
            BigInteger phi = (P.subtract(BigInteger.ONE)).multiply(Q.subtract(BigInteger.ONE));

            BigInteger e = BigInteger.valueOf(2);
            while (e.compareTo(phi) < 0) {
                if (gcd(e, phi).equals(BigInteger.ONE)) break;
                e = e.add(BigInteger.ONE);
            }

            BigInteger d = modinv(e, phi);
            sc.nextLine();
            System.out.print("Enter plaintext message: ");
            String plaintext = sc.nextLine();

            BigInteger[] cipher = new BigInteger[plaintext.length()];
            for (int i = 0; i < plaintext.length(); i++) {
                cipher[i] = BigInteger.valueOf((int) plaintext.charAt(i)).modPow(e, n);
            }

            System.out.print("Encrypted message: [");
            for (int i = 0; i < cipher.length; i++) {
                System.out.print(cipher[i]);
                if (i < cipher.length - 1) System.out.print(", ");
            }
            System.out.println("]");

            StringBuilder decrypted = new StringBuilder();
            for (BigInteger c : cipher) {
                int m = c.modPow(d, n).intValue();
                decrypted.append((char) m);
            }

            System.out.println("Decrypted message: " + decrypted.toString());
        }
    }
}
