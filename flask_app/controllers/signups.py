# Import app
from flask_app import app
# Import modules from flask
from flask_app import Flask, render_template, request, redirect, session, url_for, flash, bcrypt
from datetime import datetime

# Import models class
from flask_app.models import user, job, signup

# CRUD Create Routes
@app.route('/signup', methods=['POST'])
def add_signup_job():
    """Add a signup to the job"""
    # Check that user logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    signup.Signup.create_signup(request.form)
    return redirect(f"/job/show/{request.form['job_id']}")

# CRUD Delete Routes
@app.route('/signup/delete', methods=['POST'])
def job_delete_signup():
    """Delete the users signup from job"""
    # Check that user logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    signup.Signup.delete_signup(request.form)
    return redirect(f"/job/show/{request.form['job_id']}")


