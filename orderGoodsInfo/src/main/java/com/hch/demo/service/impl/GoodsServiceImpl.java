package com.hch.demo.service.impl;

import com.hch.demo.entity.Goods;
import com.hch.demo.dao.GoodsDao;
import com.hch.demo.service.GoodsService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

/**
 * (Goods)表服务实现类
 *
 * @author makejava
 * @since 2020-05-19 17:43:16
 */
@Service("goodsService")
public class GoodsServiceImpl implements GoodsService {
    @Resource
    private GoodsDao goodsDao;

    /**
     * 通过ID查询单条数据
     *
     * @param sku 主键
     * @return 实例对象
     */
    @Override
    public Goods queryById(String sku) {
        return this.goodsDao.queryById(sku);
    }
       
    /**
    * 查询所有 
    * @return 对象列表
    */
    @Override
    public List<Goods> queryAll(Goods goods){
        return this.goodsDao.queryAll(goods);
    }
    /**
     * 查询多条数据
     *
     * @param offset 查询起始位置
     * @param limit 查询条数
     * @return 对象列表
     */
    @Override
    public List<Goods> queryAllByLimit(int offset, int limit) {
        return this.goodsDao.queryAllByLimit(offset, limit);
    }

    /**
     * 新增数据
     *
     * @param goods 实例对象
     * @return 实例对象
     */
    @Override
    public Goods insert(Goods goods) {
        this.goodsDao.insert(goods);
        return goods;
    }

    /**
     * 修改数据
     *
     * @param goods 实例对象
     * @return 实例对象
     */
    @Override
    public boolean update(Goods goods) {
        int cnt = goodsDao.update(goods);
        if (cnt>0){
            return true;
        }else {
            return false;
        }
        //return this.queryById(goods.getSku());
    }

    /**
     * 通过主键删除数据
     *
     * @param sku 主键
     * @return 是否成功
     */
    @Override
    public boolean deleteById(String sku) {
        return this.goodsDao.deleteById(sku) > 0;
    }

    @Override
    public int count() {
        return goodsDao.count();
    }
}