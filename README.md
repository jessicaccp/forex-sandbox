# forex-sandbox

A simple project that simulates a currency exchange quote API, built with Python and FastAPI.

The main goal of this repository is to serve as a practical example and a boilerplate for creating asynchronous APIs, demonstrating a clean project structure and the use of modern tools from the Python ecosystem.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Running Tests](#running-tests)
- [License](#license)

## Features

- **Organized Structure:** The code is separated by responsibilities (endpoints, services, schemas, etc.), making it easier to maintain and test.
- **Asynchronous Operations:** It uses async/await to simulate I/O-bound operations (like calls to other APIs or databases) without blocking the application, a cornerstone of high-performance APIs.
- **Modern Tooling:** Configured with uv for fast dependency management, Ruff for linting and formatting, and Taskipy to automate common tasks.
- **Error Handling:** Includes an example of how to create custom exceptions and global handlers to return consistent error responses.
- **Configured Tests:** Comes with a test suite using pytest and httpx, ready to run and ensure code quality.
- **Automatic Documentation:** Leverages FastAPI's native feature to generate interactive documentation with Swagger UI.

## Tech Stack

- **Backend:** Python 3.12, FastAPI, Pydantic
- **Server:** Uvicorn
- **Dev Environment:** uv, Taskipy
- **Testing & Quality:** Pytest, HTTPX, Coverage, Ruff

## Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

- Git
- Python 3.12+

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jessicaccp/forex-sandbox.git
    cd forex-sandbox
    ```

2. Create and activate the virtual environment:

    ```bash
    # Create the environment
    uv venv

    # Activate it (on macOS / Linux)
    source .venv/bin/activate

    # On Windows, use: .venv\Scripts\activate
    ```

3. Install all dependencies:
    The command below installs everything you need (for both production and development).

    ```bash
    task setup
    ```

### Running the Application

1. Start the development server:

    ```bash
    task run
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Usage

The best way to interact with the API is through the interactive Swagger UI documentation, available at  **<http://127.0.0.1:8000/docs>** after running the application.

### Get a Quote

- **Endpoint:** `GET /v1/quote`
- **Parameters:**
  - `from_currency` (string, required): The source currency code (e.g., `USD`).
  - `to_currency` (string, required): The destination currency code (e.g., `BRL`).
  - `amount` (float, required): The amount to be converted.
- **Example with cURL:**

    ```bash
    curl -X GET "http://127.0.0.1:8000/v1/quote?from_currency=USD&to_currency=BRL&amount=150.50"
    ```

- **Success Response (Example):**

    ```json
    {
    "from_currency": "USD",
    "to_currency": "BRL",
    "amount": 150.5,
    "exchange_rate": 5.2314,
    "converted_amount": 787.32,
    "timestamp": "2025-09-23T19:15:00.123456"
    }
    ```

## Running Tests

To run the test suite and generate a code coverage report:

1. Run the tests:

    ```bash
    task test
    ```

2. View the coverage report (opens `htmlcov/index.html`):

    ```bash
    task post_test
    ```

## License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
