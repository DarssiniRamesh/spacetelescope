# JWQL Modernization - Quick Start Guide

## Project Summary

This is a Spring Boot 3.x application running on Java 17 that provides REST API endpoints for JWST monitoring.

## Quick Verification

### 1. Build the Project

```bash
cd Modernization/jwql-java
./mvnw clean package
```

Expected output: `BUILD SUCCESS` with JAR file created at `target/jwql-modernization-0.0.1-SNAPSHOT.jar`

### 2. Run the Application

```bash
java -jar target/jwql-modernization-0.0.1-SNAPSHOT.jar
```

Or use Maven:

```bash
./mvnw spring-boot:run
```

Application starts on port **8080** by default.

### 3. Test the Endpoints

**Health Check (Actuator):**
```bash
curl http://localhost:8080/actuator/health
```

Expected response:
```json
{
  "status": "UP",
  "components": {
    "diskSpace": {"status": "UP", "details": {...}},
    "ping": {"status": "UP"}
  }
}
```

**API Hello Endpoint:**
```bash
curl http://localhost:8080/api/hello
```

Expected response:
```json
{
  "status": "ok"
}
```

**API Documentation (Swagger UI):**

Open in browser: http://localhost:8080/swagger-ui.html

**OpenAPI Spec:**
```bash
curl http://localhost:8080/api-docs
```

## Docker Build (when Docker is available)

```bash
docker build -t jwql-modernization:latest .
docker run -p 8080:8080 jwql-modernization:latest
```

## Troubleshooting

### Port Already in Use

If port 8080 is already in use, run on a different port:

```bash
SERVER_PORT=8081 java -jar target/jwql-modernization-0.0.1-SNAPSHOT.jar
```

Or set in `application.yml`:
```yaml
server:
  port: 8081
```

### Java Version

Ensure Java 17 or higher:
```bash
java -version
```

## Next Steps

- Add database integration (PostgreSQL/JPA)
- Implement authentication (Spring Security)
- Migrate Django REST endpoints
- Add JWST monitoring services
- Implement unit and integration tests

For more details, see [README.md](../README.md)
