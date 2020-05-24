package demo;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;


import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ResoverDemo {
    public static void main(String[] args) throws IOException {

        String sku="41507444717";
        String url ="https://item.jd.com/"+sku+".html" ;
        System.out.println(url);

        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet=new HttpGet(url);
        httpGet.setHeader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36");
        CloseableHttpResponse resp = httpClient.execute(httpGet);
        if(resp.getStatusLine().getStatusCode()==200){
            String content= EntityUtils.toString(resp.getEntity());
            //System.out.println(content);

            //规格
            String pattern="selected.*?value=\"(.*?)\">";
            Pattern r=Pattern.compile(pattern);
            Matcher mat=r.matcher(content);

            while(mat.find()){
                System.out.println(mat.group());
                System.out.println(mat.group(1));
            }

            //是否有货
            String pattern1="style.*?到货通知";
            Pattern r1=Pattern.compile(pattern1);
            Matcher mat1=r1.matcher(content);
            while (mat1.find()){
                System.out.println(mat1.group());
                if(mat1.group().contains("display:none")){
                    System.out.println("无货");
                }
            }

            //颜色规格
            Document document= Jsoup.parse(content);
            Element choseAttr1=  document.getElementById("choose-attr-1");
            String pattern3 = "data-sku=(.*?) data-value=(.*?)>";
            Pattern r3=Pattern.compile(pattern3);
            Matcher mat3=r3.matcher(choseAttr1.toString());
            //System.out.println(choseAttr1.toString());
            while(mat3.find()){
                System.out.println(mat3.group(0));
                System.out.println(mat3.group(1));
                System.out.println(mat3.group(2));

            }

            //尺码
            Document document2= Jsoup.parse(content);
            Element choseAttr2=  document2.getElementById("choose-attr-2");
            //System.out.println(choseAttr2.toString());
            String pattern4 = "data-sku=\"(.*?)\" data-value=\"(.*?)\">";
            Pattern r4=Pattern.compile(pattern4);
            Matcher mat4=r4.matcher(choseAttr2.toString());

            while(mat4.find()){
                System.out.println(mat4.group(0));
                System.out.println(mat4.group(1));
                System.out.println(mat4.group(2));

            }
        }
    }
}
