package com.hch.jf.domin;

import java.io.Serializable;

public class UnionInfo implements Serializable {

    private String sku;
    private String union;

    public UnionInfo(String sku, String union) {
        this.sku = sku;
        this.union = union;
    }

    public String getSku() {
        return sku;
    }

    public void setSku(String sku) {
        this.sku = sku;
    }

    public String getUnion() {
        return union;
    }

    public void setUnion(String union) {
        this.union = union;
    }

    @Override
    public String toString() {
        return "UnionInfo{" +
                "sku='" + sku + '\'' +
                ", union='" + union + '\'' +
                '}';
    }
}
