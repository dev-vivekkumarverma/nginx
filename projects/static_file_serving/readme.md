
# Dockerized Nginx Web Server with Docker Compose

This project sets up an Nginx web server inside a Docker container using Docker Compose.

## Architecture

![Docker-Nginx Architecture](/imgResource/satatic_file_serving_via_nginx.png)

## Setup & Usage

### Prerequisites
- Install [Docker](https://docs.docker.com/get-docker/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

### Running the Project

1. **Build and start the container**  
   ```sh
   docker-compose up -d --build
   ```

2. **Access the web page**  
   Open your browser and go to `http://localhost`.

3. **Check running containers**  
   ```sh
   docker ps
   ```

4. **Stop the container**  
   ```sh
   docker-compose down
   ```

### Project Structure
```
/project-root
│── Dockerfile
│── docker-compose.yml
│── /template
│   └── index.html
│── /test/nginx
│   └── nginx.conf
│── /container_data
│── README.md

```

### Logs
Nginx logs are stored in:
- `/logs/error.log` (General Nginx errors)
- `/logs/access.log` (Requests access logs)
- `/applogs/error.log` (Application-specific errors)
- `/applogs/access.log` (Application access logs)

## License
MIT License

