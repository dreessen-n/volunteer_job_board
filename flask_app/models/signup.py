
# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from flask_app.models import user, job

"""
Change class construct, queries, and db for job
Check controllers import on server
"""

class Signup:
    # Use a alias for the database; call in classmethods as cls.db
    # For staticmethod need to call the database name not alias
    db = "volunteer_job_board"

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.job_id = data['job_id']
        self.users_who_signuped = user.User.get_user_by_id({"id": self.user_id})

    # CRUD Create
    @classmethod
    def create_signup(cls, data):
        """Add signup to signup tbl"""
        query = '''INSERT INTO signups (user_id, job_id)
        VALUES (%(user_id)s, %(job_id)s);'''
        return connectToMySQL(cls.db).query_db(query,data)

    # CRUD Read
    @classmethod
    def get_job_signups(cls, data):
        """Get signups based on job id"""
        query = "SELECT * FROM signups WHERE job_id=%(id)s ORDER BY id DESC;"
        results = connectToMySQL(cls.db).query_db(query,data)
        signups = []
        if not results:
            return  signups
        for r in results:
            signups.append(cls(r))
        return signups

    # CRUD Delete
    @classmethod
    def delete_signup(cls, data):
        """Delete signup from job; based on user_id"""
        query = '''DELETE FROM signups
        WHERE user_id=%(user_id)s AND job_id=%(job_id)s;'''
        return connectToMySQL(cls.db).query_db(query,data)

