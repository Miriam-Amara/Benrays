# ELD-Benrays Store Web Application 

This is a web application that allows ELD-Benrays company to record and keep track of their inventory.
**To view the data models, ER diagrams and UI designs, check out this link to the slide presentation: https://drive.google.com/file/d/11VnjXw7muhkJhuLKK0EAZJgjioYF6Cyp/view?usp=sharing**

## Features 

Dashboard page - Displays low stock alert and pending orders notifications.<br>
Product page - Enables employees to add, view, edit and delete products.<br> 
Employee page - Managing employees by adding, viewing, editing and deleting records.<br>
orders page - Create, view, edit and delete orders.<br>


## Technologies used

UI Design:
 - Figma

Frontend:
 - html
 - css
 - bootstrap
 - flask

Backend:
- Python
- Sqlalchemy
- MySQL
- Flask

Version Control:
- Git and GitHub


## Development Process 

The project is divided into three main parts:
1. **Models**
2. **Api**
3. **Web_flask**

### Models 

Contains all the models, database module and test modules.
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
The API endpoints include:

Employees<br>
Create:<br>
 - /api/v1/employees/register 
Update:<br>
 - `/api/v1/employees/update/<id>`
Read:<br>
 - /api/v1/employees/
 - `/api/v1/employees/<id>`
 - /api/v1/employees/data
 - /api/v1/employees/count
 Delete:<br>
 - `/api/v1/employees/<id>`


Products<br>
Create:<br>
 - /api/v1/products/register
 - /api/v1/products/category/register
 - /api/v1/products/color/register
 Update:<br>
  - `/api/v1/products/update/<id>`
  - `/api/v1/products/category/update/<id>`
  - `/api/v1/products/color/<id>`


### Web_flask
Contains all views, templates and static files 



## How to use 

### Step 1: Clone the repository
- git clone https://github.com/Miriam-Amara/Benrays.git
### Step 2: Install Python dependencies
- pip install -r requirements.txt
### Step 3: Set the PYTHONPATH environment variable
- export PYTHONPATH="~/Benrays:$PYTHONPATH"<br>
### Step 4: Run the application
 - In one terminal, run:
        python3 web_flask/app.py
- In another terminal, run:
         python3 api/v1/app.py<br>
### Step 5: Access the application in your browser
- Open 127.0.0.1:5000/benrays_store/employees/login/
