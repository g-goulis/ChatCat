package org.arizona.chatcat.api.error;

import org.arizona.chatcat.api.Status;
import org.arizona.chatcat.api.response.Response;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import java.util.Optional;

@ControllerAdvice
public class GlobalErrorHandler {

    @ExceptionHandler(Exception.class)
    public ResponseEntity<Response> handleResourceNotFound(Exception e) {
        Response errorResponse = new Response(Optional.empty(),Status.SERVER_ERROR);
        return new ResponseEntity<>(errorResponse, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    // Handle other exceptions...
}
