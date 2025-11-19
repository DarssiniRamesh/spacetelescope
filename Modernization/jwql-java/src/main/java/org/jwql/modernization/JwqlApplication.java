package org.jwql.modernization;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.Contact;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

/**
 * Main Spring Boot application class for JWQL Modernization.
 * 
 * This application provides REST API endpoints for JWST instrument monitoring
 * and data trending, migrated from the original Django-based application.
 * 
 * @author JWQL Team
 * @version 0.0.1
 */
@SpringBootApplication
public class JwqlApplication {

    /**
     * Main entry point for the Spring Boot application.
     * 
     * @param args command line arguments
     */
    // PUBLIC_INTERFACE
    public static void main(String[] args) {
        SpringApplication.run(JwqlApplication.class, args);
    }

    /**
     * Configure OpenAPI documentation for the application.
     * 
     * @return OpenAPI configuration bean
     */
    // PUBLIC_INTERFACE
    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("JWQL Modernization API")
                        .version("0.0.1")
                        .description("REST API for James Webb Space Telescope (JWST) instrument monitoring, health tracking, and data trending. Modernized Spring Boot implementation.")
                        .contact(new Contact()
                                .name("JWQL Team")
                                .url("https://github.com/spacetelescope/jwql")));
    }
}
