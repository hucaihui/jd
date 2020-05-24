package com.hch.demo.entity;

import java.io.Serializable;

/**
 * (Goods)实体类
 *
 * @author makejava
 * @since 2020-05-19 17:43:14
 */
public class Goods implements Serializable {
    private static final long serialVersionUID = 333638243301965064L;
    
    private String sku;
    
    private String descInfo;
    
    private String articleNo;
    
    private String color;
    
    private String size;
    
    private Long price;


    public String getSku() {
        return sku;
    }

    public void setSku(String sku) {
        this.sku = sku;
    }

    public String getDescInfo() {
        return descInfo;
    }

    public void setDescInfo(String descInfo) {
        this.descInfo = descInfo;
    }

    public String getArticleNo() {
        return articleNo;
    }

    public void setArticleNo(String articleNo) {
        this.articleNo = articleNo;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public Long getPrice() {
        return price;
    }

    public void setPrice(Long price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Goods{" +
                        "sku='"+sku+'\''+
                        ", descInfo='"+descInfo+'\''+ 
                        ", articleNo='"+articleNo+'\''+ 
                        ", color='"+color+'\''+ 
                        ", size='"+size+'\''+ 
                        ", price='"+price+'\''+ 
                "}";
    }
}