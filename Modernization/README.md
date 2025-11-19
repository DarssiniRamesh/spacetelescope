# JWQL Modernization

This directory contains the modernized Spring Boot 3.x (Java 17) implementation of the JWST monitoring application, migrating from the original Django-based system.

## Overview

The JWQL Modernization project is a Java-based microservice that provides REST API endpoints for James Webb Space Telescope (JWST) instrument monitoring, health tracking, and data trending.

### Technology Stack

- **Java**: 17 (LTS)
- **Framework**: Spring Boot 3.2.0
- **Build Tool**: Maven 3.9.5+
- **Container**: Docker (multi-stage build)
- **API Documentation**: SpringDoc OpenAPI (Swagger UI)

## Project Structure

```
jwql-java/
├── pom.xml                          # Maven project descriptor
├── Dockerfile                       # Multi-stage Docker build
├── src/
│   └── main/
│       ├── java/
│       │   └── org/jwql/modernization/
│       │       ├── JwqlApplication.java           # Main application class
│       │       └── web/
│       │           └── HelloController.java       # REST controller
│       └── resources/
│           └── application.yml                    # Application configuration
└── .mvn/
    └── wrapper/
        └── maven-wrapper.properties               # Maven wrapper config
```

## Prerequisites

### Local Development
- JDK 17 or higher
- Maven 3.9+ (or use included Maven wrapper)

### Docker Build
- Docker 20.10+
- Docker Compose (optional)

## Building the Application

### Local Build with Maven

```bash
cd Modernization/jwql-java

# Using Maven wrapper (recommended)
./mvnw clean package

# Or using system Maven
mvn clean package
```

The compiled JAR will be available at `target/jwql-modernization-0.0.1-SNAPSHOT.jar`

### Running Locally

```bash
# Run the Spring Boot application
./mvnw spring-boot:run

# Or run the JAR directly
java -jar target/jwql-modernization-0.0.1-SNAPSHOT.jar
```

The application will start on port **8080** by default.

## Docker Build and Run

### Build Docker Image

```bash
cd Modernization/jwql-java

# Build the Docker image
docker build -t jwql-modernization:latest .
```

### Run Container

```bash
# Run the container
docker run -d \
  --name jwql-modernization \
  -p 8080:8080 \
  jwql-modernization:latest

# View logs
docker logs -f jwql-modernization

# Stop container
docker stop jwql-modernization

# Remove container
docker rm jwql-modernization
```

### Docker Compose (Optional)

Create a `docker-compose.yml` in the Modernization directory:

```yaml
version: '3.8'
services:
  jwql-modernization:
    build:
      context: ./jwql-java
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=production
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:8080/actuator/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 40s
```

Run with:
```bash
docker-compose up -d
```

## API Endpoints

### Health Check Endpoints

1. **Actuator Health Endpoint**
   - **URL**: `http://localhost:8080/actuator/health`
   - **Method**: GET
   - **Description**: Spring Boot actuator health check
   - **Response**:
     ```json
     {
       "status": "UP"
     }
     ```

2. **Hello API Endpoint**
   - **URL**: `http://localhost:8080/api/hello`
   - **Method**: GET
   - **Description**: Simple API health verification
   - **Response**:
     ```json
     {
       "status": "ok"
     }
     ```

### API Documentation

- **Swagger UI**: `http://localhost:8080/swagger-ui.html`
- **OpenAPI JSON**: `http://localhost:8080/api-docs`

The Swagger UI provides interactive API documentation where you can explore and test all available endpoints.

## Verification

After starting the application, verify it's running correctly:

```bash
# Test actuator health endpoint
curl http://localhost:8080/actuator/health

# Test hello API endpoint
curl http://localhost:8080/api/hello

# Access Swagger UI in browser
open http://localhost:8080/swagger-ui.html
```

## Configuration

The application can be configured via `src/main/resources/application.yml` or environment variables:

- **Server Port**: `SERVER_PORT` (default: 8080)
- **Spring Profile**: `SPRING_PROFILES_ACTIVE` (default: none)
- **Log Level**: `LOGGING_LEVEL_ORG_JWQL` (default: DEBUG)

Example with environment variables:

```bash
docker run -d \
  -p 9090:9090 \
  -e SERVER_PORT=9090 \
  -e SPRING_PROFILES_ACTIVE=production \
  jwql-modernization:latest
```

## Development Workflow

1. **Make code changes** in `src/main/java/` or `src/main/resources/`
2. **Rebuild**: `./mvnw clean package`
3. **Run tests**: `./mvnw test`
4. **Run locally**: `./mvnw spring-boot:run`
5. **Build Docker image**: `docker build -t jwql-modernization:latest .`
6. **Test container**: `docker run -p 8080:8080 jwql-modernization:latest`

## Next Steps

### Immediate Tasks
1. ✅ Basic Spring Boot scaffold complete
2. ✅ Maven build configuration
3. ✅ Docker containerization
4. ✅ Health and hello endpoints
5. ✅ OpenAPI documentation

### Migration Roadmap
1. **Database Integration**: Add JPA/Hibernate for PostgreSQL
2. **Authentication**: Implement Spring Security with JWT
3. **API Migration**: Port Django REST endpoints to Spring controllers
4. **Monitoring**: Add JWST instrument-specific monitoring services
5. **Testing**: Implement unit and integration tests
6. **CI/CD**: Set up GitHub Actions pipeline
7. **MAST Integration**: Connect to external data sources

### Planned Features
- REST API for JWST proposal and file data
- Instrument health dashboards
- Automated data trending
- Integration with MAST and other services
- User authentication and authorization

## Troubleshooting

### Build Issues

**Problem**: Maven build fails with "Java version" error
```bash
# Verify Java version
java -version
# Should show version 17 or higher

# Set JAVA_HOME if needed
export JAVA_HOME=/path/to/jdk-17
```

**Problem**: Maven dependencies download slowly
```bash
# Use Maven daemon for faster builds
./mvnw --daemon clean package
```

### Runtime Issues

**Problem**: Port 8080 already in use
```bash
# Change port via environment variable
SERVER_PORT=9090 java -jar target/jwql-modernization-0.0.1-SNAPSHOT.jar
```

**Problem**: Health endpoint returns 503
- Check application logs: `docker logs jwql-modernization`
- Verify all dependencies started correctly
- Ensure adequate memory allocation

## Support and Documentation

- **Original JWQL Project**: [github.com/spacetelescope/jwql](https://github.com/spacetelescope/jwql)
- **Spring Boot Docs**: [spring.io/projects/spring-boot](https://spring.io/projects/spring-boot)
- **SpringDoc OpenAPI**: [springdoc.org](https://springdoc.org/)

## License

This project follows the same license as the original JWQL project.
