package com.hch.jf.util;

import java.io.Serializable;

public class RetMsg implements Serializable {

    private boolean success;
    private String msg;

    public RetMsg(boolean success) {
        this.success = success;
    }

    public RetMsg(boolean success, String msg) {
        this.success = success;
        this.msg = msg;
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    @Override
    public String toString() {
        return "RetMsg{" +
                "success=" + success +
                ", msg='" + msg + '\'' +
                '}';
    }
}
