package com.hch.demo.dao;

import com.hch.demo.entity.Goods;
import org.apache.ibatis.annotations.Param;
import java.util.List;

/**
 * (Goods)表数据库访问层
 *
 * @author makejava
 * @since 2020-05-19 17:43:15
 */
public interface GoodsDao {

    /**
     * 通过ID查询单条数据
     *
     * @param sku 主键
     * @return 实例对象
     */
    Goods queryById(String sku);

    /**
     * 查询指定行数据
     *
     * @param offset 查询起始位置
     * @param limit 查询条数
     * @return 对象列表
     */
    List<Goods> queryAllByLimit(@Param("offset") int offset, @Param("limit") int limit);


    /**
     * 通过实体作为筛选条件查询
     *
     * @param goods 实例对象
     * @return 对象列表
     */
    List<Goods> queryAll(Goods goods);

    /**
     * 新增数据
     *
     * @param goods 实例对象
     * @return 影响行数
     */
    int insert(Goods goods);

    /**
     * 修改数据
     *
     * @param goods 实例对象
     * @return 影响行数
     */
    int update(Goods goods);

    /**
     * 通过主键删除数据
     *
     * @param sku 主键
     * @return 影响行数
     */
    int deleteById(String sku);

    /**总计录数
     *
     *
     */
    int count();
}