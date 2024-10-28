# Sales Stock Management

## Overview

This project consists of a Django backend and a Vue.js frontend. The backend serves as an API for the frontend, handling business logic and database interactions. The frontend provides a user interface for users to interact with the application.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Features

- User authentication (login, signup)
- Dashboard with visualizations (sales, invoices)
- Responsive design using Vuetify (for Vue.js)

## Technologies

### Backend (Django)
- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL (or any other database you choose)

### Frontend (Vue.js)
- Vue.js 2.x
- Vue Router
- Vuex (if state management is used)
- Vuetify for UI components

## Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Clone the Repository

git clone https://github.com/ankur7171/data_labs.git
cd data_labs_project

# Running the Application
To build and run both the Django backend and Vue.js frontend, use:
docker-compose up --build

# Accessing the Application
Django API: http://localhost:8000
Vue.js Frontend: http://localhost:8080
Usage
Django API

# Endpoints:
/api/login/: User login endpoint
/api/register/: User registration endpoint
/api/sales/: Retrieve sales data
/api/invoices/: Retrieve invoice data

# Vue.js Frontend
The frontend is designed for easy navigation and interaction with the API.
All API calls are made through the configured base URL.
