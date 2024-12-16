# Car Management System

A secure, containerized REST API system for managing car information, featuring HTTPS encryption, load balancing, and a well-structured network infrastructure.

## Table of Contents

- [Network Infrastructure](#network-infrastructure)
- [Security](#security)
- [REST API](#rest-api)
- [Getting Started](#getting-started)

## Network Infrastructure

The system employs a Docker-based network architecture with the following components:

- **Custom Network**: 
  - Subnet: 172.28.0.0/24
  - Controlled IP assignments for predictable addressing

- **Services**:
  1. **API Service** (172.28.0.10):
     - Python Flask application
     - Internal port: 5000
     - Not directly exposed to external network
  
  2. **NGINX Service** (172.28.0.11):
     - Acts as reverse proxy and load balancer
     - Exposes ports 80 (HTTP) and 443 (HTTPS)
     - Handles SSL termination

- **Load Balancing**:
  - NGINX configured as load balancer
  - Capable of distributing traffic across multiple API instances
  - Automatic HTTP to HTTPS redirection

## Security

The system implements several security measures:

### SSL/TLS Encryption
- Self-signed certificates for HTTPS
- Certificate location: `nginx/certs/`
- SSL termination at NGINX level

### Network Security
- API service not directly exposed to external network
- All external traffic routed through NGINX
- Controlled internal network with fixed IP addresses

### Certificate Generation
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout server.key \
    -out server.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"
```

## REST API

The API provides CRUD operations for car management:

### Endpoints

#### GET /cars
Lists all cars
```bash
curl -k https://localhost/cars
```

#### POST /cars
Adds a new car
```bash
curl -k -X POST https://localhost/cars \
  -H 'Content-Type: application/json' \
  -d '{
    "plate": "XX-00-00",
    "model": "Car Model",
    "year": 0000
  }'
```

#### PUT /cars/<plate>
Updates car information
```bash
curl -k -X PUT https://localhost/cars/AA-12-34 \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "Updated Model",
    "year": 0000
  }'
```

#### DELETE /cars/<plate>
Removes a car
```bash
curl -k -X DELETE https://localhost/cars/XX-00-00
```

### Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 409: Conflict (Duplicate plate)
```

## Getting Started

1. Clone the repository
2. Generate SSL certificates:
```bash
make certificate
```

3. Start the services:
```bash
make up
```

4. Test the API:
```bash
# Test GET request
curl -k https://localhost/cars

# Test POST request
curl -k -X POST https://localhost/cars \
    -H 'Content-Type: application/json' \
    -d '{"plate": "CC-99-88", "model": "Ford Focus", "year": 2020}'
```

5. Stop the services:
```bash
make down
```

### Clean Up
To remove all containers and clean the system:
```bash
make clean
```

## Requirements

- Docker
- Docker Compose
- OpenSSL (for certificate generation)
- Make
```