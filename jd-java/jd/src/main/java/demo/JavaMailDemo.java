package demo;

import java.util.Properties;


public class JavaMailDemo {

    public static  void main(String[] args) {

        Properties properties=new Properties();
        properties.setProperty("mail.host","smtp.qq.com");

        properties.setProperty("mail.transport.protocol","smtp");

        properties.setProperty("mail.smtp.auth","true");

        //MailSSLSocketFactory sf = new MailSSLSocketFactory();
        //sf.setTrustAllHosts(true);
        //properties.put("mail.smtp.ssl.enable", "true");
        //properties.put("mail.smtp.ssl.socketFactory", sf);
    }
}
