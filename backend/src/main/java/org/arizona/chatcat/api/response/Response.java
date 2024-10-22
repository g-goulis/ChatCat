package org.arizona.chatcat.api.response;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;
import org.arizona.chatcat.api.Status;

import java.util.Optional;

// Do not include data if it is null (ERROR)
@JsonInclude(JsonInclude.Include.NON_NULL)
@Data
public class Response {

    private final int status;
    private final String message;
    private final String timestamp;
    private final String data;

    public Response(Optional<String> data, Status status) {
        this.status = status.getCode();
        this.message = status.getMessage();
        this.timestamp = java.time.LocalDateTime.now().toString();

        this.data = data.isPresent() ? data.get() : null;
    }

}
