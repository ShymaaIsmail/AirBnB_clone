#!/usr/bin/python3
"""Setting User info"""


from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
