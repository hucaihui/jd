package com.hch.jf.server;

import com.hch.jf.domin.UnionInfo;
import com.hch.jf.util.RetMsg;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import com.github.kevinsawicki.http.HttpRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;

@Service
public class JfService {

    @Autowired
    private RedisService redisService;


    public String transUrl(String name,String fromContent)  {
        System.out.println(name);
        System.out.println(fromContent);
        String key = "JfCookie_"+name;
        String cookie = (String) redisService.get(key);
        //System.out.println(cookie);
        //String cookie1 = "client_type=android;app_id=161;login_mode=2;jxjpin=a13218343010;tgt=AAJd9mHUAEDhOPEdYretO6pvIbiRA0k5qa4wxW54YXoWTxhftHC77mIvuingsM9tqciD3T0PHSZYdVPTSTAx7zCwD-Kd-z0V;qwd_chn=99;qwd_schn=1;jfShareSource=1_2_1";
        //System.out.println(cookie.equals(cookie1));
        HashMap<String ,String> headers=new HashMap<>(){
            {
                put("Cookie",cookie);
                put("Host","qwd.jd.com");
                put("User-Agent","jxj/3.7.4");
                put("Connection","keep-alive");
            }
        };

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


        return resp;
    }


    public RetMsg getTranRes(String name, String content)  {
        if(redisService.exists("content_"+content)){
            System.out.println("该content已在库中");
            return new RetMsg(true,(String)redisService.get("content_"+content));
        }

        String resp = null;
        resp = transUrl(name,content);
        // 最后一次返回值，有可能会出现cookie失效
        redisService.set("LastResp"+name,resp);

        try {

            JSONObject jsonObject = new JSONObject(resp);
            String toContent = jsonObject.getString("content");
            JSONArray skuInfos = jsonObject.getJSONArray("skuInfos");

            //ArrayList<UnionInfo> unionInfos = new ArrayList<>();
            for (int i = 0; i < skuInfos.length() ; i++) {
                JSONObject skuInfo = skuInfos.getJSONObject(i);
                String skuId = skuInfo.getString("skuId");
                String unionUrl = skuInfo.getString("unionUrl");
                System.out.println(skuId);
                System.out.println(unionUrl);

            }


            // 防止多次请求,有效期是3天
            redisService.set("content_"+content,toContent,259200L);

            return new RetMsg(true,toContent);
        } catch (JSONException e) {
            e.printStackTrace();
            return new RetMsg(false,"json解析错误");

        }


    }



}
