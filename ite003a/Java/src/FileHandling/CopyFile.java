package ite003a.Java.src.FileHandling;

import java.io.*;

public class CopyFile {
   public static void main(String args[]) throws IOException
   {
      FileInputStream in = null;
      FileOutputStream out = null;

      try {
         String p = "D:\\ISIDRO\\ariel\\Dropbox\\java\\myprograms\\ite003a\\Java\\src\\FileHandling\\";
         in = new FileInputStream(p+"input.txt");
         out = new FileOutputStream(p+"output.txt");
         
         int c;
         while ((c = in.read()) != -1) {
             System.out.println((char)c);
            out.write(c);
         }
      }finally {
         if (in != null) {
            in.close();
         }
         if (out != null) {
            out.close();
         }
      }
   }
}
