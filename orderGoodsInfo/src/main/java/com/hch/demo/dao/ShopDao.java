package com.hch.demo.dao;

import com.hch.demo.entity.Shop;
import org.apache.ibatis.annotations.Param;
import java.util.List;

/**
 * (Shop)表数据库访问层
 *
 * @author makejava
 * @since 2020-05-19 16:32:57
 */
public interface ShopDao {

    /**
     * 通过ID查询单条数据
     *
     * @param shopNo 主键
     * @return 实例对象
     */
    Shop queryById(Integer shopNo);

    /**
     * 查询指定行数据
     *
     * @param offset 查询起始位置
     * @param limit 查询条数
     * @return 对象列表
     */
    List<Shop> queryAllByLimit(@Param("offset") int offset, @Param("limit") int limit);


    /**
     * 通过实体作为筛选条件查询
     *
     * @param shop 实例对象
     * @return 对象列表
     */
    List<Shop> queryAll(Shop shop);

    /**
     * 新增数据
     *
     * @param shop 实例对象
     * @return 影响行数
     */
    int insert(Shop shop);

    /**
     * 修改数据
     *
     * @param shop 实例对象
     * @return 影响行数
     */
    int update(Shop shop);

    /**
     * 通过主键删除数据
     *
     * @param shopNo 主键
     * @return 影响行数
     */
    int deleteById(Integer shopNo);

}