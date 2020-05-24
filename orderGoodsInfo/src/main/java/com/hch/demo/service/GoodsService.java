package com.hch.demo.service;

import com.hch.demo.entity.Goods;
import java.util.List;

/**
 * (Goods)表服务接口
 *
 * @author makejava
 * @since 2020-05-19 17:43:15
 */
public interface GoodsService {

    /**
     * 通过ID查询单条数据
     *
     * @param sku 主键
     * @return 实例对象
     */
    Goods queryById(String sku);
    
     /**
     * 查询所有
     * @return 对象列表
     */
    List<Goods> queryAll(Goods goods);
 

    /**
     * 查询多条数据
     *
     * @param offset 查询起始位置
     * @param limit 查询条数
     * @return 对象列表
     */
    List<Goods> queryAllByLimit(int offset, int limit);

    /**
     * 新增数据
     *
     * @param goods 实例对象
     * @return 实例对象
     */
    Goods insert(Goods goods);

    /**
     * 修改数据
     *
     * @param goods 实例对象
     * @return 实例对象
     */
    boolean update(Goods goods);

    /**
     * 通过主键删除数据
     *
     * @param sku 主键
     * @return 是否成功
     */
    boolean deleteById(String sku);

    int count();
}