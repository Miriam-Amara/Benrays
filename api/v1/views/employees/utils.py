#!/usr/bin/python3


from flask_restful import reqparse, abort


def add_req_args(passwd=True):
    """
    Add arguments that are required from clients
    """
    employee_args = reqparse.RequestParser()

    employee_args.add_argument("first_name", type=str,
                            required=True, help="first name is required"
                            )
    employee_args.add_argument("middle_name", type=str,
                            help="middle name"
                            )
    employee_args.add_argument("last_name", type=str,
                            required=True, help="last name is required"
                            )
    employee_args.add_argument("age", type=str,
                            required=True, help="age is required"
                            )
    employee_args.add_argument("gender", type=str,
                            required=True, help="gender is required"
                            )
    employee_args.add_argument("marital_status", type=str,
                            required=True, help="marital status is required"
                            )
    employee_args.add_argument("phone_number", type=str,
                            required=True, help="phone number is required"
                            )
    employee_args.add_argument("email", type=str,
                            required=True, help="email is required"
                            )
    employee_args.add_argument("password", type=str,
                            required=passwd, help="password is required"
                            )
    employee_args.add_argument("street", type=str,
                            required=True, help="street name is required"
                            )
    employee_args.add_argument("city", type=str,
                            required=True, help="city name is required"
                            )
    employee_args.add_argument("state", type=str,
                            required=True, help="state name is required"
                            )
    employee_args.add_argument("role", type=str,
                            required=True, help="employee role is required"
                            )
    employee_args.add_argument("salary", type=str)
    employee_args.add_argument("work_experience", type=str)
    employee_args.add_argument("qualification", type=str)
    employee_args.add_argument("name_of_guarantor", type=str,
                            required=True,
                            help="Name of guarantor role is required"
                            )
    employee_args.add_argument("guarantor_contact", type=str,
                            required=True,
                            help="Guarantor's phone number role is required"
                            )
    employee_args.add_argument("permissions", type=str,
                            help="permissions"
                            )
    employee_args.add_argument(
        "warehouses", type=str,
        required=True,
        help="Warehouses id where the employee manages is required")
    
    return employee_args


def check_required_attributes(passwd=True):
    """
    Checks that required attributes value is not None
    """
    attr_list = ["first_name", "age", "gender",
            "marital_status", "phone_number", "email",
            "password", "street", "city", "state",
            "role", "name_of_guarantor", "guarantor_contact"]
    if passwd == False:
        attr_list.remove("password")

    try:
        employee_args = add_req_args(passwd)
        args = employee_args.parse_args()
    except Exception:
        abort(400, description="post data must be json")
    
    for key, value in args.items():
        if key in attr_list and value is None:
            abort(400, description=f"{key} cannot be null")
        
    if (len(args["phone_number"]) != 11 and
        len(args["guarantor_contact"]) != 11 and
        len(args["warehouses"]) != 36
    ):
        abort(
            400,
            description = "phone nubers must be 11 characters " +
            " and warehouse id 36 characters"
        )

        
   
    return args


def delete_attr(*args, employee_dict=None):
   """
    Deletes attributes from employee dict and returns
    the modified dict

    params:
    employee_dict(dict): The employee dictionary where values will
                        be deleted
    args(list): list of values to be deleted from the dict
   """
   if employee_dict:
    for arg in args:
       del employee_dict[arg]
