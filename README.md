# Online Code Judge Platform
## Overview
The Online Code Judge Platform is a web application that facilitates fair assessment in programming exams or assignments. Developed similarly to LeetCode, it focuses on the Python programming language and provides a user-friendly interface for users to submit Python functions and upload code securely using tokens. The platform's backend functionality is handled by a Flask API to control the interaction between components. Celery is employed to distribute tasks efficiently and manage them. The entire project is wrapped in Docker for easier deployment and scalability. An automated testing mechanism with extensive test cases also evaluates code submissions and generates accurate scores.

## Features
- **User-Friendly Interface:** Allows users to submit Python functions and upload code securely using tokens.
- **Automated Testing:** Implements an automated testing mechanism with extensive test cases to evaluate code submissions and generate accurate scores.
- **Automated Python Function Checking:** Checks the format of Python function submissions automatically. The platform rejects submissions if the input is not in the specified format.
- **Controlled Python Package Usage:** Users can only use selected Python packages. The platform rejects submissions with prohibited libraries or dependencies.
- **Unified Docker Compose Setup:** Uses one Docker Compose file to start all services, including database, Celery, and API, simplifying deployment and management.

## Technologies
- **Flask API:** Handles backend functionality to control the interaction between components.
- **Celery:** Utilized for efficient task distribution and management.
- **MongoDB:** Used for database management to store data related to the Online Code Judge Platform.
- **Docker:** Entire project is containerized for easier deployment and scalability.

## Getting Started

To get started with the Online Code Judge Platform, follow these steps:

1. Clone the repository: \
`git clone https://github.com/yourusername/code-judge-platform.git`

2. Navigate to the project directory: \
`cd code-judge-platform`

3. Install Docker and Docker Compose if you haven't already. You can follow this guide for step-by-step instructions on installing them: [How to Install Docker and Docker Compose](https://dockerwebdev.com/tutorials/install-docker/)

4. Run the following command to start the application using Docker Compose: \
`docker-compose up`

5. Access the platform in your web browser at `http://localhost:1234`.

6. Monitor the submission activities by accessing the Celery Flower dashboard at `http://localhost:5000`.

7. For data management, access the MongoDB database at `http://localhost:27017`.

