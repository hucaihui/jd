package com.horse.demomail.controller;

import com.horse.demomail.tool.MailTool;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Random;

@Controller
public class UserController {

    //页面控制
    @GetMapping({"/","/login"})
    public String login(){
        return "login";
    }

    @GetMapping("/register")
    public String register(){
        return "register";
    }

    @GetMapping("/admin")
    public String admin(){
        return "admin";
    }

    //验证码
    @RequestMapping("/getCode")
    @ResponseBody
    public boolean getCode(String email , HttpServletRequest request){
        //随机生成一个验证码
        Integer code=new Random().nextInt(500);
        request.getSession().setAttribute("code",code.toString());
        request.getSession().setAttribute("email",email);
        new Thread(
                new Runnable() {
                    @Override
                    public void run() {
                        MailTool.send(email,code);
                    }
                }
        ).start();
        return true;
    }

    //登陆
    @RequestMapping("/tologin")
    public String tologin(String email ,String code,HttpServletRequest request){
        String emailAddress = (String) request.getSession().getAttribute("email");
        String codeId = (String) request.getSession().getAttribute("code");
        if (email.equals(emailAddress) && code.equals(codeId)){
            return "redirect:/admin";
        }else {
            return "redirect:/error";
        }
    }


}
