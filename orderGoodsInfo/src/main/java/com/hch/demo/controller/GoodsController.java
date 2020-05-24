package com.hch.demo.controller;

import com.hch.demo.entity.Goods;
import com.hch.demo.service.GoodsService;
import com.hch.demo.util.RetMsg;
import com.hch.demo.util.RetObj;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * (Goods)表控制层
 *
 * @author makejava
 * @since 2020-05-19 17:43:16
 */
@RestController
@RequestMapping("goods")
public class GoodsController {
    /**
     * 服务对象
     */
    @Resource
    private GoodsService goodsService;
    
    /**
    * 查询所有
    */
    @GetMapping("selectAll")
    public List<Goods> selectAll() {
        return this.goodsService.queryAll(null);
    }

    @GetMapping("selectAllByLimit")
    public List<Goods> queryAllByLimit(
            @RequestParam(value = "page",required = false,defaultValue = "1")int page,
            @RequestParam(value = "size",required = false,defaultValue = "10") int size){
        //System.out.println(offset);
        //System.out.println(limit);
        int offset = page-1;

        //int total = goodsService.count();
        return goodsService.queryAllByLimit(offset,size);
    }
    
    /**
     * 通过主键查询单条数据
     *
     * @param id 主键
     * @return 单条数据
     */
    @GetMapping("selectOne")
    public RetObj selectOne(String id) {
        Goods goods = goodsService.queryById(id);
        System.out.println(goods);
        if(null==goods){
            return new RetObj(false);
        }
        return new RetObj(true,goods);
    }

    @RequestMapping("insert")
    public Goods insert(@RequestBody Goods goods){
        return this.goodsService.insert(goods);
    }

    @RequestMapping("update")
    public RetMsg update(@RequestBody Goods goods,
                         @RequestParam(value = "password",required = false,defaultValue = "1") String password){
        System.out.println("[goods] [update]");
        System.out.println(goods);
        System.out.println(password);
        if("123456".equals(password)){
            if(goodsService.update(goods)){
                return new RetMsg(true);
            }else{
                return new RetMsg(false,"更新失败");
            }
        }else{
            return new RetMsg(false,"密码错误");
        }

        //return this.goodsService.update(goods);
    }
    @RequestMapping("deleteById")
    public boolean deleteById(String id){
        return this.goodsService.deleteById(id);
    }
}