package com.hch.jf;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication
public class JfApplication {

    public static void main(String[] args) {
        SpringApplication.run(JfApplication.class, args);
    }

}
