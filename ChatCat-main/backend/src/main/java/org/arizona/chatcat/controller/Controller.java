package org.arizona.chatcat.controller;

import org.arizona.chatcat.api.Status;
import org.arizona.chatcat.api.request.Request;
import org.arizona.chatcat.api.response.Response;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@CrossOrigin(origins = "http://localhost:3000")
@RequestMapping(path = "/api/v1", consumes = "application/json", produces = "application/json")
public class Controller {

    @GetMapping(path = "/ping")
    public ResponseEntity<Response> ping() {
        return new ResponseEntity<>(new Response(Optional.of("Hello World!"), Status.SUCCESS), HttpStatus.OK);
    }

    @PostMapping(path = "/message")
    public ResponseEntity<Response> message(@RequestBody Request request) {
        return new ResponseEntity<>(new Response(Optional.of(request.getData()), Status.SUCCESS), HttpStatus.OK);
    }
}
