package com.horse.demomail;

import com.horse.demomail.tool.MailToolDemo;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Random;

@SpringBootTest
class DemomailApplicationTests {

    @Test
    void contextLoads() {
        Integer code=new Random().nextInt(500);
        System.out.println(code);
        MailToolDemo.send("781223439@qq.com",code);
    }

}
