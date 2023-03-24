# Ecommerce-web-services

In this project, we are building an eCommerce API that provides a range of endpoints for managing products, orders, customers, and other aspects of an online store. The API is built using modern web technologies, including the REST architectural style, and is designed to be scalable, secure, and easy to use.

To ensure the API is easy to test and work with, we are using two popular tools: Swagger and Postman. Swagger provides a user-friendly interface for exploring and interacting with the API, while Postman is a powerful API client that allows developers to test the API and automate common tasks.

Overall, this project is focused on building a robust and reliable eCommerce API that can be easily integrated into a wide range of applications and platforms. By using Swagger and Postman for testing and development, we are able to ensure that the API meets our high standards for quality and usability.


## ER DIAGRAM
![ER DIAGRAM](/svg/er.drawio.svg "This is ER image.")

## Data Models
The following data model are used in this project:

**User Model:** This model contains the information about the users of the application, such as their name, email address, and password.

**Product Model:** This model contains information about the products offered by the application, such as their name, image, price, quantity.

**Cart Model:** This model contains information about which cart is associated to which user, such as their user id, cart amount, checkout status.

**Cart Details:** This model contains information about the products user added to his cart, such as their product id, cart price, cart quantity.

**Purchase History:** This model contains information about the orders placed by users, such as their user id, date, total price.

**Purchase History Details:** This model contains information about the details of orders placed by users, such as their history id, product name, quantity, total price.

## Data Flow Design

![data flow design](/svg/daraflow.drawio.svg "This is data flow image.")


The data flow design of an API shows us how data is exchanged between the client applications, and the backend data sources.

## Getting Started

### Overview
The following instructions will guide you through the installation process for our API project. The project is built using Python and flask, and provides a RESTful API for accessing and manipulating data. Before you begin, ensure that you have Python installed on your machine.

### System Requirements
Python: Version 3.10.9 or higher
Flask: Version 2.2.3 or higher

### Installation Steps:

1. Clone the project repository from GitHub: https://github.com/N-i-s-h-a-n-t/ecommerce-web-service.git
2. Open a terminal window and navigate to the project directory.
3. Run the following command to create virtual enviornment: `py -3 -m venv venv`
4. Install the requirements from command: `pip install -r requirements.txt`
5. The API will noe be accessible at `http://localhost:5000/`. You can test the API endpoints using postman and swagger.

### Updating:
To update the project, follow these steps:
1. Pull the latest changes from the GitHub repository: `git pull`
2. Run the following command to update project dependencies: `pip install -r requirements.txt`
3. Restart the server to apply any changes: `flask run`

### Configuration:
To add configuration: folow these steps:
1. Add config.py file in the repository.
2. Define `DEBUG` AND `SQL_ALCHEMY_DATABASE_URI` constants.
3. DEBUG value **True** for **development** and **False** for **production**.
4. Inside **SQL_ALCHEMY_DATABASE_URI** provide database URI.
## Example :
#### DEBUG = True
#### SQLALCHEMY_DATABASE_URI = "`postgresql://username:password@localhost/databasename`"