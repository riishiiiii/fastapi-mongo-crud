# FastAPI MongoDB CRUD Application

This repository contains a FastAPI application that provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database. The application is containerized using Docker and can be easily deployed and run with Docker Compose.

## Prerequisites

Before running this application, make sure you have the following installed:

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/riishiiiii/fastapi-mongo-crud
cd fastapi-mongo-crud
```
2. Build and run the containers:
```bash
docker-compose up -d --build
```

This command will build the Docker images and start the containers in detached mode.

3. The application should now be running at `http://localhost:8000`. You can test the API endpoints using tools like cURL, Postman, or your preferred HTTP client.

## API Endpoints
 - `POST /items/`: Create a new item
 - `GET /items/`: Retrieve a list of all items
 - `GET /items/?name=<name>&is_offer=<true/false>`: Retrieve items based on query parameters
 - `PUT /items/<item_id>`: Update an existing item
 - `DELETE /items/<item_id>`: Delete an item

## Stopping the Application
To stop the containers, run:
```bash
docker-compose down
```