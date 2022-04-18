public class Kriptografi {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Orang amry = new Orang(2,19999);
        Orang reza = new Orang(2,19999);
        amry.mengirimPesan(reza, 1010);
    }
}

class Orang{
    private double privateKey;
    public double publicKey;
    private double id_number1;
    private double id_number2;

    public Orang(double id_number1, double id_number2) {
        this.privateKey = generatePrivateKey(id_number1,id_number2);
        this.publicKey = generatePublicKey(id_number1,id_number2);
        this.id_number1 = id_number1;
        this.id_number2 = id_number2;
    }

    public double gcd(double a,double b){
        return b==0 ? a : gcd(b, a%b); 
    }
    public double generatePrivateKey(double id_number1, double id_number2){
        double phi = (id_number1-1)*(id_number2-1);
        double e = 2;
        while (e < phi)
        {
            if (gcd(e, phi)==1)
                break;
            else
                e++;
        }
        int k = 2; 
        double d = (1 + (k*phi))/e;
        return d;
    }

    public double generatePublicKey(double id_number1, double id_number2){
        double e = 10;
        double phi = (id_number1-1)*(id_number2-1);
        while (e < phi)
        {
            if (gcd(e, phi)==1)
                break;
            else
                e++;
        }
        return e;
    }
    public void mengirimPesan(Orang penerima, double pesan){
        double enkripted = Math.pow(pesan, penerima.publicKey);
        enkripted %= penerima.id_number1*penerima.id_number2;
        System.out.println(enkripted);
        double dekripsi = Math.pow(enkripted, penerima.privateKey);
        dekripsi %= penerima.id_number1*penerima.id_number2;
        System.out.println(dekripsi);
    }
}
