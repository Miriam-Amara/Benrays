# ELD-Benrays Store Web Application 

This is a web application that allows ELD-Benrays company to record and keep track of their inventory.

## Features 

Dashboard page - Displays low stock alert and pending orders alert.
Product page - Allows employees to add, view, edit and delete products 
Employee page - for adding, viewing, editing and deleting employees 
orders page - for creating new orders, editing, viewing and deleting existing orders.


## Technologies used

UI Design:
 - Figma

Frontend:
 - html
 - css
 - bootstrap
 - flask

Backend:
- Sqlalchemy
- MySQL
- Flask


## Development Process 

The project is in three (3) parts:
1. Models
2. Api
3. Web_flask

### Models 

Contains all the system models, database module and test modules.
 - base_model
 - products
 - employees
 - warehouses
 - orders
 - order_items
 - sales
 - purchases
 - inventory
 - returns
 - inventory transactions
 - engine - contains db_storage
 - tests - contains all the unittests


### API
The main API endpoints include:

Employees:
Create:
 - /api/v1/employees/register 
Update:
- /api/v1/employees/update/<id>
Read:
 - /api/v1/employees/
 - /api/v1/employees/<id>
 - /api/v1/employees/data
 - /api/v1/employees/count
 Delete:
 - /api/v1/employees/<id>


Products:
Create:
 - /api/v1/products/register
 - /api/v1/products/category/register
 - /api/v1/products/color/register
 Update:
  - /api/v1/products/update/<id>
  - /api/v1/products/category/update/<id>
  - /api/v1/products/color/<id>


  ### Web_flask
  Contains all views templates and static files 



  ## How to use 

  Step 1 - Git close the repository
  Step 2 - In the parent (Benrays) folder run
           python3 web_flask/app.py
           In another tab run
           python3 api/v1/app.py
  
   
