# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from flask_app.models import user
from datetime import datetime

"""
Change class construct, queries, and db for job
"""

class Job:
    # Use a alias for the database; call in classmethods as cls.db
    # For staticmethod need to call the database name not alias
    db = "volunteer_job_board"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.num_volunteers = data['num_volunteers']
        self.start_time = data['start_time']
        self.end_time = data['end_time']
        self.location = data['location']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # Needed to create this to capture the creator of the job
        self.creator = None

    # CRUD CREATE METHODS
    @classmethod
    def create_job(cls,data):
        """Create a job"""
        query = "INSERT INTO jobs (name, num_volunteers, start_time, end_time, location, description, user_id) VALUES (%(name)s, %(num_volunteers)s, %(start_time)s, %(end_time)s, %(location)s, %(description)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    # CRUD READ METHODS -- Modified for many to many
    @classmethod
    def get_all_jobs(cls):
        """Get all the jobs in db"""
        query = '''SELECT * FROM jobs
                JOIN users AS creators ON jobs.user_id = creators.id
                WHERE jobs.start_time > current_timestamp()
                ORDER BY jobs.start_time ASC;'''
        results = connectToMySQL(cls.db).query_db(query)
        all_jobs = []
        if not results:
            return all_jobs
        for r in results:
            job = (cls(r))
            # Create user_data dict for the creator of job
            user_data = {
                'id': r['creators.id'],
                'first_name': r['first_name'],
                'last_name': r['last_name'],
                'email': r['email'],
                'phone': r['phone'],
                'password': r['password'],
                'created_at': r['creators.created_at'],
                'updated_at': r['creators.updated_at']
            }
            one_user = user.User(user_data)
            # Set one_user to creator in job
            job.creator = one_user
            all_jobs.append(job)
        return all_jobs

    @classmethod
    def get_all_past_jobs(cls):
        """Get all the jobs in db before current date"""
        query = '''SELECT * FROM jobs
                JOIN users AS creators ON jobs.user_id = creators.id
                WHERE jobs.start_time < current_timestamp()
                ORDER BY jobs.start_time ASC;'''
        results = connectToMySQL(cls.db).query_db(query)
        all_jobs = []
        if not results:
            return all_jobs
        for r in results:
            job = (cls(r))
            # Create user_data dict for the creator of job
            user_data = {
                'id': r['creators.id'],
                'first_name': r['first_name'],
                'last_name': r['last_name'],
                'email': r['email'],
                'phone': r['phone'],
                'password': r['password'],
                'created_at': r['creators.created_at'],
                'updated_at': r['creators.updated_at']
            }
            one_user = user.User(user_data)
            # Set one_user to creator in job
            job.creator = one_user
            all_jobs.append(job)
        return all_jobs

    @classmethod
    def get_one_job(cls,data):
        """Get one job to display"""
        query = '''SELECT * FROM jobs
                JOIN users AS creators ON jobs.user_id = creators.id
                WHERE jobs.id = %(id)s;'''
        results = connectToMySQL(cls.db).query_db(query, data)
            # Create the job object
        if not results:
            return all_jobs
        for r in results:
            job = (cls(r))
            # Create user_data dict for the creator of job
            user_data = {
                'id': r['creators.id'],
                'first_name': r['first_name'],
                'last_name': r['last_name'],
                'email': r['email'],
                'phone': r['phone'],
                'password': r['password'],
                'created_at': r['creators.created_at'],
                'updated_at': r['creators.updated_at']
            }
            one_user = user.User(user_data)
            # Set one_user to creator in job
            job.creator = one_user
        return job

    # CRUD UPDATE METHODS
    @classmethod
    def update_job(cls,data):
        """Update the job"""
        query = "UPDATE jobs SET name=%(name)s, num_volunteers=%(num_volunteers)s, start_time=%(start_time)s, end_time=%(end_time)s, location=%(location)s, description=%(description)s  WHERE jobs.id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    # CRUD DELETE METHODS
    @classmethod
    def delete_job(cls,data):
        """Delete job"""
        query = "DELETE FROM jobs WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    # FORM VALIDATION
    @staticmethod
    def validate_form(job):
        """Validate the new job create form"""
        is_valid = True # We set True until False
        if len(job['name']) < 2:
            flash("The name must be at least 2 characters.", "danger")
            is_valid = False
        if len(job['num_volunteers']) < 1:
            flash("The number of volunteers can not be blank.", "danger")
            is_valid = False
        if len(job['location']) < 5:
            flash("The location must be greater than 5.", "danger")
            is_valid = False
        if len(job['description']) < 20:
            flash("The description must be greater than 20.", "danger")
            is_valid = False
        return is_valid

