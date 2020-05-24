package com.hch.demo.entity;

import java.io.Serializable;

/**
 * (Shop)实体类
 *
 * @author makejava
 * @since 2020-05-19 16:32:57
 */
public class Shop implements Serializable {
    private static final long serialVersionUID = -82804446808618560L;
    
    private Integer shopNo;
    
    private String shopName;


    public Integer getShopNo() {
        return shopNo;
    }

    public void setShopNo(Integer shopNo) {
        this.shopNo = shopNo;
    }

    public String getShopName() {
        return shopName;
    }

    public void setShopName(String shopName) {
        this.shopName = shopName;
    }

    @Override
    public String toString() {
        return "Shop{" +
                        " shopNo='"+shopNo+'\''+
                        ", shopName='"+shopName+'\''+ 
                "}";
    }
}