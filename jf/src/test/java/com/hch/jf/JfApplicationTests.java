package com.hch.jf;

import com.hch.jf.server.RedisService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.core.RedisTemplate;

@SpringBootTest(classes = JfApplication.class)
class JfApplicationTests {

    @Autowired
    private RedisService redisService;
    @Autowired
    private RedisTemplate redisTemplate;

    @Test
    void contextLoads() {
        String key= "testConnect";

        redisTemplate.opsForValue().set(key,"test");
        String res = (String) redisTemplate.opsForValue().get(key);
        if("test".equals(res)){
            System.out.println("redis连接正常");
        }
    }

    @Test
    void testStringRedisService() {
        String key = "JfCookie_hucaihui";

        String cookie1 = "client_type=android;app_id=161;login_mode=2;jxjpin=a13218343010;tgt=AAJd9mHUAEDhOPEdYretO6pvIbiRA0k5qa4wxW54YXoWTxhftHC77mIvuingsM9tqciD3T0PHSZYdVPTSTAx7zCwD-Kd-z0V;qwd_chn=99;qwd_schn=1;jfShareSource=1_2_1";
        //redisService.set(key,cookie1,1000L);
        redisService.set(key,cookie1);

    }
}
