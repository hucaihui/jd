package com.hch.jf.util;

import java.io.Serializable;

public class RetObj implements Serializable {

    private boolean success;
    private Object obj;

    public RetObj(boolean success) {
        this.success = success;
    }

    public RetObj(boolean success, String msg) {
        this.success = success;
        this.obj = msg;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public Object getObj() {
        return obj;
    }

    @Override
    public String toString() {
        return "RetObj{" +
                "success=" + success +
                ", obj=" + obj +
                '}';
    }

    public void setObj(Object obj) {
        this.obj = obj;
    }
}
