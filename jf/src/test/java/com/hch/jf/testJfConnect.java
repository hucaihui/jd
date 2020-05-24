package com.hch.jf;

import com.github.kevinsawicki.http.HttpRequest;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.web.client.RestTemplate;

import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.HashSet;

//@SpringBootTest(classes = JfApplication.class)
public class testJfConnect {

   //@Autowired
   //private RestTemplate restTemplate;
   //

   @Test
   public void testHttpRequest() throws JSONException {


      String cookie = "client_type=android;app_id=161;login_mode=2;jxjpin=a13218343010;tgt=AAJd9mHUAEDhOPEdYretO6pvIbiRA0k5qa4wxW54YXoWTxhftHC77mIvuingsM9tqciD3T0PHSZYdVPTSTAx7zCwD-Kd-z0V;qwd_chn=99;qwd_schn=1;jfShareSource=1_2_1";
      HashMap<String ,String> headers=new HashMap<>(){
         {
            put("Cookie",cookie);
            put("Host","qwd.jd.com");
            put("User-Agent","jxj/3.7.4");
            put("Connection","keep-alive");
         }
      };
      String fromContent = "https://item.m.jd.com/10902370587.html";
      HashMap<String,String> data = new HashMap<>(){
         {
            put("content",fromContent);
            put("shareSource","1_2_1");
         }
      };

      String url = "https://qwd.jd.com/cps/zl";
      HttpRequest request=HttpRequest.get(url,data,true);
      request.trustAllCerts().trustAllHosts();

      request.headers(headers);
      String resp = request.body();

      System.out.println(resp);
      JSONObject jsonObject = new JSONObject(resp);
      String toContent = jsonObject.getString("content");
      JSONArray skuInfos = jsonObject.getJSONArray("skuInfos");
      for (int i = 0; i < skuInfos.length() ; i++) {
          JSONObject skuInfo = skuInfos.getJSONObject(i);
          String skuId = skuInfo.getString("skuId");
          String unionUrl = skuInfo.getString("unionUrl");
          System.out.println(skuId);
          System.out.println(unionUrl);
      }

      //System.out.println(content);
   }


}
