package com.hch.demo.util;

public class RetObj {
    private boolean success;
    private Object obj;

    public RetObj(boolean success) {
        this.success = success;
    }

    public RetObj(boolean success, Object obj) {
        this.success = success;
        this.obj = obj;
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

    public void setObj(Object obj) {
        this.obj = obj;
    }

    @Override
    public String toString() {
        return "RetObj{" +
                "success=" + success +
                ", obj=" + obj +
                '}';
    }
}
