import java.util.Scanner;

// Caesar Cipher program is used to encrypt and decrypt
// the messages with the key value 3.

public class CaesarCipher {


    // Method to encrypt the text message with 3.
    public static String encrypt(String text , int key){

        String encrypted_text = "";
        for(char ch : text.toCharArray()){
            char c = Character.isUpperCase(ch) ? 'A' : 'a';
            if(Character.isAlphabetic(ch)) {
                encrypted_text += (char) (c + (ch + key - c) % 26);
            }else {
                encrypted_text+=ch;
            }
        }
        return encrypted_text;
    }


    //Method to decrypt the text message with 3.
    public static String decrypt(String text , int key){
        String decrypted_text = "";
        for(char ch : text.toCharArray()){
            char c = Character.isUpperCase(ch) ? 'A' : 'a';
            if(Character.isAlphabetic(ch)) {
                decrypted_text += (char) (c + (ch - key - c) % 26);
            }else {
                decrypted_text+=ch;
            }
        }
        return decrypted_text;
    }

    public static void main(String[] args) {

        // Taking input from the user.
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();

        // Take the shift value from the user.
        int key = sc.nextInt();

        // Calling the encrypt method with text and key = 3.
        String encrypted_text = encrypt(text,key);
        System.out.println("After Encryption : "+encrypted_text);

        // Calling the decrypt method with encrypted text and key = 3.
        String decrypt_text = decrypt(encrypted_text,key);
        System.out.println("After Decryption :"+decrypt_text);
    }

}