# __init__.py
from flask import Flask, render_template, render_template, request, redirect, session, url_for, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "Colorado Rules! Best State"
bcrypt = Bcrypt(app)