import Jama.Matrix;

public class HillCipher {
    public static void main(String[] args) {
        String text = "GFG";
        String key = "HILLMAGIC";
        int n = text.length();

        double[][] text_matrix = new double[n][1];
        double[][] key_matrix = new double[n][n];

        for(int i = 0 ; i < n ; i++){
            text_matrix[i][0] = text.charAt(i)-65;
        }

        int c = 0;
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < n ; j++){
                key_matrix[i][j] = key.charAt(c++)-65;
            }
        }


        Matrix a = new Matrix(text_matrix);
        Matrix b = new Matrix(key_matrix);

        double[][] product = b.times(a).getArray();
        double[][] result = new double[n][1];

        String encrypt = "";
        for(int i=0;i<n;i++){
            result[i][0] = (product[i][0])%26;
            encrypt += (char)(result[i][0]+65);
        }

        System.out.println(encrypt);


        Matrix inverse = new Matrix(key_matrix);
        inverse = inverse.inverse();

        double[][] decrypted_matrix = inverse.times(Matrix.constructWithCopy(product)).getArray();
        String decrypted = "";
        for(int i = 0 ; i < n ; i++){
            decrypted_matrix[i][0] = Math.round(decrypted_matrix[i][0]);
            decrypted+=(char)(decrypted_matrix[i][0]+65);
        }
        System.out.println(decrypted);
    }
}