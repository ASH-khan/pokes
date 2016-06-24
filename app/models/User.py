""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
from flask import Flask, flash

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """

    def get_all_users(self):
        return self.db.query_db("SELECT * FROM users")

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def register(self, users):
        print users

        # pattern for email
        email_pat = re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$")

        # pattern for password
        pwd_pat = re.compile(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z].{8,}$)")

        def is_password_valid(pwd):

            if not (re.match(pwd_pat, pwd)):
                return False
            else:
                return True

        def is_email_valid(email):

            if not (re.match(email_pat, email)):
                return False
            else:
                return True

        flag = True

        if not users['name']:
            flash("Name cannot be empty.", 'name')
            flag = False

        if not users['alias']:
            flash("Alias name cannot be empty.", 'alias')
            flag = False

        if not users['email']:
            flash("Email cannot be empty.", 'email')
            flag = False

        if len(users['name']) < 2:
            flash("First Name too short.", 'nshort')
            flag = False

        if len(users['alias']) < 2:
            flash("Last Name is too short.", 'ashort')
            flag = False

        if not users['name'].isalpha():
            flash('Name must be only alphabets.', 'name_int')
            flag = False

        if not users['alias'].isalpha():
            flash('Alias must be only alphabets.', 'alias_int')

        if not is_email_valid(users['email']):
            flash('Invalid Email.', 'notemail')
            flag = False

        if not is_password_valid(users['pwd']):
            flash('Password must be eight chars long , at least one upper case , one lowercase and numbers',
                  'pass_error')
            flag = False

        if str(users['pwd']) != str(users['cpwd']):
            flash('Password not matching.', 'no_match')
            flag = False

        if not users['dateofbirth']:
            flash('No date of birth provided', 'date')
            flag = False

        if not flag:
            return {'status': False}

        if flag:
            # bcrypted password
            pwd_hash = self.bcrypt.generate_password_hash(users['pwd'])
            print pwd_hash

            query1 = "INSERT INTO users (name, alias, email, password,dateofbirth, created_at, updated_at) VALUES (:name, :alias, :email, :dateofbirth, :pwdhash, now(), now())"

            data = {
                'name': users['name'],
                'alias': users['alias'],
                'email': users['email'],
                'pwdhash': pwd_hash,
                'dateofbirth': users['dateofbirth']
            }
            self.db.query_db(query1, data)
            flash('You are successfully registered! Please Sign in')

            # Then retrieve the last inserted user.
            query2 = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(query2)
            # print users
            return {"status": True, 'user': users[0]}

        def login(self, users):
            password = users['pwd']

            query = "SELECT * FROM users WHERE email= :email LIMIT 1"
            data = {'email': users['email']}
            user = self.db.query_db(query, data)

            if user:
                # check_password_hash() compares encrypted password in DB to one provided by user logging in
                if self.bcrypt.check_password_hash(user[0]['password'], password):
                    return user
                else:
                    return flash("Invalid password!", 'wrongpass')

                    # Whether we did not find the email, or if the password did not match, either way return False
            else:
                return flash('Please check your email or password', 'no_match')


