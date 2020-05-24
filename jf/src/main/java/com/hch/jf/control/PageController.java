package com.hch.jf.control;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class PageController {

    @RequestMapping("/list")
    public String  list(){
        System.out.println("list");
        return "goods";
    }

}
