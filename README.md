# Flask Assignment

This is a Flask web application.

## Requirements

- Python 3.x
- Flask

## Description

This Flask web application serves as a simple example of a web server built using the Flask framework. It includes basic routing and template rendering functionalities.

### Features

- **Transaction Records**: A homepage form to displays transaction list.
- **Create Transaction**: A form to create a transaction.
- **Edit Transaction**: A form to update a transaction.
- **Delele Transaction**: A form to delete a transaction.

## Required Package

Flask framework is required to run this application.

To install Flask, open the terminal and run this command:
    ```
    pip install flask
    ```

## Usage

1. Open terminal and run the application:
    ```bash
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

## Running with Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:
    ```bash
    docker build -t flask_assignment .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 flask_assignment
    ```
3. Open your web browser and go to `http://127.0.0.1:5000`.
