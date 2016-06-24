"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model


class Poke(Model):
    def __init__(self):
        super(Poke, self).__init__()

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

    def poke_count(self, id):
        query = 'SELECT count(pokes.poked_by) as cnt FROM pokes where id = :id GROUP BY id'
        data = {'id': id}
        return self.db.query_db(query, data)

    def poke_number(self, id):
        query = 'select count(poked_by) as history, b.alias as alias from users a join pokes on a.id = pokes.user_id JOIN users b ON b.id = pokes.poked_by where a.id= :id group by poked_by'
        data = {'id': id}
        return self.db.query_db(query, data)

    def get_other_pokes(self, id):
        query = 'select a.name as name, a.alias as alias,a.id as userid, a.email as email, count(poked_by) as history from users a LEFT join pokes on a.id = pokes.user_id LEFT JOIN users b ON b.id = pokes.poked_by where a.id != :id group by a.id'
        data = {'id': id}
        return self.db.query_db(query, data)

    def add_poke(self, poke_id, user_id):
        query = "INSERT INTO pokes (poked_by,poke_number, poked_at,user_id) VALUES (:user_id,1,NOW(),:poke_id)"
        data = {'user_id': int(user_id), 'poke_id': int(poke_id)}
        return self.db.query_db(query, data)
