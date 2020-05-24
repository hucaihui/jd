package com.hch.demo;

import com.hch.demo.entity.Goods;
import com.hch.demo.service.GoodsService;
import com.hch.demo.service.impl.GoodsServiceImpl;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.List;


//@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest(classes = OrderApplication.class)
class GoodsTests {

    @Autowired
    private GoodsService goodsService;


    @Test
    void contextLoads() {

        List<Goods> goods = goodsService.queryAll(null);
        System.out.println(goods);
    }

    @Test
    void testInsert() {
        Goods goods=new Goods();
        goods.setSku("1223");
        goods.setArticleNo("c77124");
        goods.setColor("c77124");
        goods.setSize("42");

        //goodsService.insert(goods);

    }
}
