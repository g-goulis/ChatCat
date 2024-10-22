package org.arizona.chatcat.api.request;

import lombok.Data;

@Data
public class Request {

    private String data;

    public Request() {}

    public Request(String data) {
        this.data = data;
    }

}
