package com.hch.demo.controller;

import com.hch.demo.entity.Shop;
import com.hch.demo.service.ShopService;
import com.hch.demo.util.RetObj;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * (Shop)表控制层
 *
 * @author makejava
 * @since 2020-05-19 16:32:57
 */
@RestController
@RequestMapping("shop")
public class ShopController {
    /**
     * 服务对象
     */
    @Resource
    private ShopService shopService;
    
    /**
    * 查询所有
    */
    @GetMapping("selectAll")
    public List<Shop> selectAll() {
        return this.shopService.queryAll(null);
    }
    
    
    /**
     * 通过主键查询单条数据
     *
     * @param id 主键
     * @return 单条数据
     */
    @GetMapping("selectOne")
    public RetObj selectOne(Integer id) {
        Shop shop=shopService.queryById(id);
        if(null==shop){
            return new RetObj(false);
        }
        return new RetObj(true,shop);
    }
    
    @RequestMapping("insert")
    public Shop insert(@RequestBody Shop shop){
        System.out.println(shop);
        return this.shopService.insert(shop);
    }

    @RequestMapping("update")
    public Shop update(@RequestBody Shop shop){
        return this.shopService.update(shop);
    }
    @RequestMapping("deleteById")
    public boolean deleteById(Integer id){
        return this.shopService.deleteById(id);
    }
}