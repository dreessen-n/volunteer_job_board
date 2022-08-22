# Import app
from flask_app import app
# Import modules from flask
from flask_app import Flask, render_template, request, redirect, session, url_for, flash, bcrypt

# Import models class
from flask_app.models import user, job, signup
from datetime import datetime
# CRUD CREATE ROUTES
@app.route('/job/create', methods=['POST'])
def create_new_job():
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Call staticmethod to validate form
    if not job.Job.validate_form(request.form):
        # Redirect back to new job page
        return redirect('/job/new')
    # Create data dict based on request form
    # the keys must match exactly to the var in the query set
    data = {
        'name': request.form['name'],
        'num_volunteers': request.form['num_volunteers'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'location': request.form['location'],
        'description': request.form['description'],
        'user_id': session['id']
    }
    job.Job.create_job(data)
    return redirect('/dashboard')

@app.route('/job/new')
def job_new():
    """Display the form to create a new job"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on user in session
    # the keys must match exactly to the var in the query set
    data = { 'id': session['id'] }
    # Call classmethod in models
    return render_template('new.html', user=user.User.get_user_by_id(data))

# CRUD READ ROUTES
@app.route('/dashboard')
def dashboard():
    """Dashboard"""
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data set to query user based on id to get name to display
    data = {
        'id': session['id']
    }
    # Pass the data dict to create_user method in class
    one_user = user.User.get_user_by_id(data)
    if one_user:
        session['email'] = one_user.email
        session['first_name'] = one_user.first_name
        session['last_name'] = one_user.last_name
        session['phone'] = one_user.phone
    # Add all_jobs to the dashboard
    all_jobs = job.Job.get_all_jobs()
    print(all_jobs)
    return render_template('dashboard.html', one_user=one_user, all_jobs=all_jobs)


@app.route('/past')
def past_jobs():
    """Past Jobs"""
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data set to query user based on id to get name to display
    data = {
        'id': session['id']
    }
    # Pass the data dict to create_user method in class
    one_user = user.User.get_user_by_id(data)
    if one_user:
        session['email'] = one_user.email
        session['first_name'] = one_user.first_name
        session['last_name'] = one_user.last_name
        session['phone'] = one_user.phone
    # Add all_jobs to the dashboard
    all_jobs = job.Job.get_all_past_jobs()
    print(all_jobs)
    return render_template('past.html', one_user=one_user, all_jobs=all_jobs)

@app.route('/job/show/<int:job_id>')
def job_show_one(job_id):
    """Show the job on a page"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on job_id
    # The keys must match exactly to the var in the query set
    data = { 'id': job_id }
    # Create additonal data dict for user
    data_user = { 'id': session['id'] }
    # Call classmethods and render_template edit template with data filled in
    return render_template('show.html', one_job=job.Job.get_one_job(data), user=user.User.get_user_by_id(data_user), signups=signup.Signup.get_job_signups(data))

@app.route('/job/show_past/<int:job_id>')
def job_show_past_one(job_id):
    """Show the job on a page"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on job_id
    # The keys must match exactly to the var in the query set
    data = { 'id': job_id }
    # Create additonal data dict for user
    data_user = { 'id': session['id'] }
    # Call classmethods and render_template edit template with data filled in
    return render_template('show_past.html', one_job=job.Job.get_one_job(data), user=user.User.get_user_by_id(data_user), signups=signup.Signup.get_job_signups(data))


# CRUD UPDATE ROUTES
# Show job to edit with populated info
@app.route('/job/edit/<int:job_id>')
def edit_job(job_id):
    """Edit the job"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on job_id
    # The keys must match exactly to the var in the query set
    data = { 'id': job_id }
    # Create additonal data dict for user
    data_user = { 'id': session['id'] }
    # Call classmethods and render_template edit template with data filled in
    return render_template('edit.html', one_job=job.Job.get_one_job(data), user=user.User.get_user_by_id(data_user))

# Update the job
@app.route('/job/update', methods=['POST'])
def update_job():
    """Update job after editing"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Call staticmethod to validate form
    if not job.Job.validate_form(request.form):
        # Redirect back to new job page
        id = int(request.form['id'])
        return redirect(f'/job/edit/{id}')
    # Create data dict based on job_id
    # The keys must match exactly to the var in the query set
    data = {
        'id': int(request.form['id']),
        'name': request.form['name'],
        'num_volunteers': request.form['num_volunteers'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'location': request.form['location'],
        'description': request.form['description'],
        'user_id': session['id']
    }
    # Call classmethod in models
    job.Job.update_job(data)
    id = request.form['id']
    # Give message that update was successful
    flash("Edit was successful", "success")
    # Redirect to dashboard after update
    return redirect(f'/job/edit/{id}')

# CRUD DELETE ROUTES
@app.route('/job/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    """Delete job if session user created"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on job_id
    # The keys must match exactly to the var in the query set
    data = { 'id': job_id }
    # Call classmethod in models
    job.Job.delete_job(data)
    # Redirect back to dashboard after deletion
    return redirect('/dashboard')

