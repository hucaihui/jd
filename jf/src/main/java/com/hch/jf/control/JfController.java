package com.hch.jf.control;


import com.hch.jf.server.JfService;
import com.hch.jf.server.RedisService;
import com.hch.jf.util.RetMsg;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

@RestController
@RequestMapping("jf")
public class JfController {
    @Autowired
    private JfService jfService;

    @Autowired
    private RedisService redisService;

    @RequestMapping("test")
    public String test(){
        return "test";
    }

    @RequestMapping("setJfCookie")
    public RetMsg setJfCookie(
            @RequestParam("name")String name,
            @RequestParam("cookie")String cookie){

        System.out.println(name);
        System.out.println(cookie);
        String checkUrl = "https://item.m.jd.com/10902370587.html";
        redisService.set("JfCookie_"+name,cookie);
        RetMsg tranRes = jfService.getTranRes(name, checkUrl);
        if(tranRes.isSuccess()){
            return new RetMsg(true,name+" cookie设置成功");
        }

        return new RetMsg(false,"cookie无效");

    }

    @RequestMapping("getTranRes")
    public RetMsg getTranRes(
            @RequestParam(value = "name",required = false,defaultValue = "hucaihui") String name,
            @RequestParam(value = "content") String content){

        if(!redisService.exists( "JfCookie_"+name)){
            return new RetMsg(false,"name错误，默认为空，找不到值");
        }

        return jfService.getTranRes(name,content);
    }

    @RequestMapping("findAll")
    public Object getAllContent(){
        System.out.println(redisService.findAll("content_*"));
        return redisService.findAll("content_*");
    }

}
