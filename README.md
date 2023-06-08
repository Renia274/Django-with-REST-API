Django with REST API

This is a repository that demonstrates how to build a Django application with a RESTful API. It provides a basic setup for creating API endpoints, handling requests, and interacting with a database using Django's ORM.
Prerequisites

Before getting started, ensure that you have the following prerequisites installed on your machine:

    Python (version 3.6 or higher)
    Django (version 3.0 or higher)
    Django REST Framework (version 3.12 or higher)
    MySQL

Installation

Clone the repository to your local machine using the following command:

    git clone https://github.com/Renia274/Django_with_rest.git

Change into the project directory:

cd Django_with_rest

Create a virtual environment to isolate the project dependencies:

python3 -m venv env

Activate the virtual environment:

For macOS/Linux:

    source env/bin/activate

For Windows:

    .\env\Scripts\activate

Install the project dependencies:

    pip install -r requirements.txt

Run the database migrations:

    python manage.py migrate

Usage

To start the Django development server and access the API endpoints, follow these steps:

    Activate the virtual environment if it's not already activated:

        For macOS/Linux:

            source env/bin/activate

For Windows:

    .\env\Scripts\activate

Start the development server:

    python manage.py runserver

    Open your web browser and navigate to http://localhost:8000/ to access the API root view.

API Endpoints

This project provides the following API endpoints:

    /api/: The root endpoint that provides an overview of available API endpoints.
    /api/categories/: Endpoint for creating and retrieving categories.
    /api/products/{id}/: Endpoint for creating and retrieving categories.
  

Testing

To run the test suite for this project, follow these steps:

    Activate the virtual environment if it's not already activated:

        For macOS/Linux:

            source env/bin/activate

For Windows:

    .\env\Scripts\activate

Run the tests using the following command:

    python manage.py test
