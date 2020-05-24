package demo;


import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class demo01 {

    public static void main(String[] args) throws IOException {

        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet=new HttpGet("http://www.itcast.cn/");
        CloseableHttpResponse resp = httpClient.execute(httpGet);
        if(resp.getStatusLine().getStatusCode()==200){
            String content= EntityUtils.toString(resp.getEntity());
            System.out.println(content);
        }
    }
}
