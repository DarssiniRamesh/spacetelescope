package org.jwql.modernization.web;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

/**
 * Simple REST controller for basic API health verification.
 * 
 * Provides a simple endpoint to verify that the application is running
 * and responding to HTTP requests correctly.
 */
@RestController
@RequestMapping("/api")
@Tag(name = "Hello", description = "Basic API health check endpoints")
public class HelloController {

    /**
     * Simple health check endpoint.
     * 
     * Returns a JSON response indicating the API is operational.
     * This endpoint can be used for basic connectivity and deployment verification.
     * 
     * @return ResponseEntity containing status map with "ok" status
     */
    // PUBLIC_INTERFACE
    @GetMapping("/hello")
    @Operation(
        summary = "Basic health check",
        description = "Returns a simple status response to verify the API is operational",
        responses = {
            @ApiResponse(
                responseCode = "200",
                description = "API is operational",
                content = @Content(
                    mediaType = "application/json",
                    schema = @Schema(implementation = Map.class)
                )
            )
        }
    )
    public ResponseEntity<Map<String, String>> hello() {
        return ResponseEntity.ok(Map.of("status", "ok"));
    }
}
