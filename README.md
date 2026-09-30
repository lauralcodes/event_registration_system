# Event Registration System

A small Python-based event registration application developed as a learning project.

The application allows users to view available events, select an event, and register with their name and email. Event data and registrations are stored in a MySQL database.

The project also includes a Flask REST API for managing events and registrations, with Swagger/OpenAPI documentation and JWT-based authentication for protected endpoints.

## Features

- View available events
- Display event details such as name, date, time, and price
- Register users for events
- Store events and registrations in MySQL
- Create new events through a REST API
- View all events through the API
- Delete events through the API
- Validate event information before saving
- Validate registration information
- Prevent duplicate event IDs
- Prevent duplicate registrations for the same event
- Check that an event exists before registration
- Return appropriate HTTP status codes and JSON responses
- Swagger/OpenAPI API documentation
- JWT-based authentication
- Protect API endpoints with JWT
- Store database credentials and JWT secret in environment variables

## Technologies

- Python 3
- Object-Oriented Programming
- MySQL
- Flask
- Flask-Smorest
- Swagger/OpenAPI
- JWT Authentication
- MySQL Connector/Python
- python-dotenv
- Marshmallow
- cURL

## Concepts Practiced

- Classes and objects
- Constructors and instance attributes
- Functions and modules
- Separation of responsibilities
- Database connections and SQL
- SELECT, INSERT, and DELETE
- Foreign keys and relationships
- REST API design
- HTTP methods
- JSON
- Input validation
- HTTP status codes
- API testing with cURL
- API documentation with Swagger/OpenAPI
- Request schemas with Marshmallow
- JWT authentication
- Environment variables
- Basic API security

## Swagger / OpenAPI

The API includes interactive Swagger documentation.

When the Flask application is running, Swagger UI is available at:

`http://127.0.0.1:5000/swagger-ui`

The OpenAPI specification is available at:

`http://127.0.0.1:5000/openapi.json`

Swagger can be used to:

- View available endpoints
- See request schemas
- Test API endpoints
- Authenticate using a JWT
- Send requests directly to the API

## Environment Variables

Database credentials and the JWT secret are stored in `.env`.

Example:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=event_registration
JWT_SECRET_KEY=your-secret-key

## Future Development

- Add user roles and permissions
- Add automated tests
- Add an endpoint to view individual events
- Add automatic handling of past events

## Project Goal

The goal of this project is to gradually build a more complete backend application while developing practical skills in Python, OOP, databases, REST APIs, Flask, authentication and software development practices.

The application is intentionally being developed step by step, with new features added as new concepts are learned.

**Status:** In Development# event_registration_system
