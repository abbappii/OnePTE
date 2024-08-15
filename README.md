# Question and Answer Management System

## Overview
This project is designed to manage and evaluate various types of questions and their corresponding answers. The primary question types supported are:
- **SST (Summarize Spoken Text)**
- **RO (Re-Order Paragraph)**
- **RMMCQ (Reading Multiple Choice Questions)**

The system allows authenticated users to participate in test sessions, submit answers, and receive scores. Admin users have the ability to manage questions and sessions through a dedicated admin interface.

## Features
- **Question Management:** Create, update, and manage different types of questions, ensuring each question title is unique.
- **Answer Submission and Validation:** Users can submit answers, which are validated to ensure they correspond to the provided questions.
- **Test Sessions:** Users can participate in test sessions that include various types of questions, with sessions tracked by user.
- **Admin Interface:** Admins have the ability to manage the entire application, including questions, answers, and test sessions.
- **Postman Collection:** A comprehensive Postman collection is provided for easy API testing and integration.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Postman (for API testing)

### Steps
- clone repository or download it
- Install dependencies using **pip3 install -r requirements.txt**
- Migrate database using **python3 manage.py migrate**
- To run the server use **python3 manage.py runserver**

### Postman collection
- The Postman collection is available in the repository. Download it and import it into your Postman client.
