"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.load_model('Poke')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html')

    def get_all_users(self):
        all_users = self.models['User'].get_all_users()
        return self.load_view('poked.html', all_users=all_users)

    def register(self):
        user_status = self.models['User'].register(request.form)
        print user_status

        if user_status['status'] == False:
            return redirect('/')

        else:
            if user_status['status'] == True:
                # the user should have been created in the model
                # we can set the newly-created users id and name to session
                session['id'] = user_status['user']['id']
                session['name'] = user_status['user']['name']
                # we can redirect to the users profile page here
                all_users = self.models['User'].get_all_users()
                return self.load_view('poked.html', all_users=all_users)

    def login(self):
        data = {
            'email': request.form['email'],
            'password': request.form['pwd']
        }
        users = self.models['User'].login(data)
        print users
        # session varaible for admin vs normal users. using this to switch between html templates
        if users:
            session['id'] = users[0]['id']
            session['name'] = users[0]['name']
            # all_users = self.models['User'].get_all_users()
            return redirect('/get_all_users')
        else:
            return redirect('/register')

    def logout(self):
        session.clear()
        return redirect('/')
