from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
import math
import os


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

server = 'prod'
app=Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['mail-id'],
    MAIL_PASSWORD = params['mail-password']
)
mail = Mail(app)


if server == 'local':
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    query = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Notice(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    slug = db.Column(db.String(21), unique=True, nullable=False)

class Scroll(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scroll_notice = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Principal(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    info = db.Column(db.String(12), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)

class Teacher(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    info = db.Column(db.String(12), nullable=False)
    role = db.Column(db.String(12), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)
    
class Clerk(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    info = db.Column(db.String(12), nullable=False)
    role = db.Column(db.String(12), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)

class Other(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    info = db.Column(db.String(12), nullable=False)
    role = db.Column(db.String(12), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)

class S9(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)

class S10(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)

class S11(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)

class S12(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)

class L9(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)


class L9_hindi(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L9_eng(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L9_guj(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L9_ss(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L9_sk(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L9_sci(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)


class L10(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L10_sk(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L10_ss(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L10_sci(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L10_guj(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L10_eng(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)



class L11(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L11_chem(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L11_phy(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L11_eng(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L12(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L12_chem(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L12_phy(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

class L12_eng(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    decr = db.Column(db.String(12), nullable=False)
    pdf_decr1 = db.Column(db.String(12), nullable=False)
    pdf_file1 = db.Column(db.String(12), nullable=False)
    pdf_decr2 = db.Column(db.String(12), nullable=False)
    pdf_file2 = db.Column(db.String(12), nullable=False)
    pdf_decr3 = db.Column(db.String(12), nullable=False)
    pdf_file3 = db.Column(db.String(12), nullable=False)
    video_decr1 = db.Column(db.String(12), nullable=False)
    video_file1 = db.Column(db.String(12), nullable=False)
    video_decr2 = db.Column(db.String(12), nullable=False)
    video_file2 = db.Column(db.String(12), nullable=False)
    video_decr3 = db.Column(db.String(12), nullable=False)
    video_file3 = db.Column(db.String(12), nullable=False)

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return "Uploaded successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/notice-list")
def notice():
    notice = Notice.query.filter_by().all()
    return render_template('notice.html', params=params, notice=notice)

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        notice = Notice.query.filter_by(sno=sno).first()
        db.session.delete(notice)
        db.session.commit()
    return redirect('/dashboard')

# deleting endpoint for scroll notice

@app.route("/delete/scroll/<string:sno>", methods = ['GET', 'POST'])
def delete_scroll(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        scroll = Scroll.query.filter_by(sno=sno).first()
        db.session.delete(scroll)
        db.session.commit()
    return redirect('/dashboard')

# deleting endpoint for principal

@app.route("/delete/principal/<string:sno>", methods = ['GET', 'POST'])
def delete_principal(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        principal = Principal.query.filter_by(sno=sno).first()
        db.session.delete(principal)
        db.session.commit()
    return redirect('/dashboard')

# deleting endpoint for teacher

@app.route("/delete/teacher/<string:sno>", methods = ['GET', 'POST'])
def delete_teacher(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        teacher = Teacher.query.filter_by(sno=sno).first()
        db.session.delete(teacher)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for clerk

@app.route("/delete/clerk/<string:sno>", methods = ['GET', 'POST'])
def delete_clerk(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        clerk = Clerk.query.filter_by(sno=sno).first()
        db.session.delete(clerk)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for other

@app.route("/delete/other-staff/<string:sno>", methods = ['GET', 'POST'])
def delete_other(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        other = Other.query.filter_by(sno=sno).first()
        db.session.delete(other)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for s9

@app.route("/delete/s9/<string:sno>", methods = ['GET', 'POST'])
def delete_s9(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        s9 = S9.query.filter_by(sno=sno).first()
        db.session.delete(s9)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for s10

@app.route("/delete/s10/<string:sno>", methods = ['GET', 'POST'])
def delete_s10(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        s10 = S10.query.filter_by(sno=sno).first()
        db.session.delete(s10)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for s11

@app.route("/delete/s11/<string:sno>", methods = ['GET', 'POST'])
def delete_s11(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        s11 = S11.query.filter_by(sno=sno).first()
        db.session.delete(s11)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for s12

@app.route("/delete/s12/<string:sno>", methods = ['GET', 'POST'])
def delete_s12(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        s12 = S12.query.filter_by(sno=sno).first()
        db.session.delete(s12)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9

@app.route("/delete/l9/<string:sno>", methods = ['GET', 'POST'])
def delete_l9(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9 = L9.query.filter_by(sno=sno).first()
        db.session.delete(l9)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9_hindi

@app.route("/delete/l9_hindi/<string:sno>", methods = ['GET', 'POST'])
def delete_l9_hindi(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9_hindi = L9_hindi.query.filter_by(sno=sno).first()
        db.session.delete(l9_hindi)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9_eng

@app.route("/delete/l9_eng/<string:sno>", methods = ['GET', 'POST'])
def delete_l9_eng(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9_eng = L9_eng.query.filter_by(sno=sno).first()
        db.session.delete(l9_eng)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9_guj

@app.route("/delete/l9_guj/<string:sno>", methods = ['GET', 'POST'])
def delete_l9_guj(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9_guj = L9_guj.query.filter_by(sno=sno).first()
        db.session.delete(l9_guj)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9_ss

@app.route("/delete/l9_ss/<string:sno>", methods = ['GET', 'POST'])
def delete_l9_ss(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9_ss = L9_ss.query.filter_by(sno=sno).first()
        db.session.delete(l9_ss)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9_sk

@app.route("/delete/l9_sk/<string:sno>", methods = ['GET', 'POST'])
def delete_l9_sk(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9_sk = L9_sk.query.filter_by(sno=sno).first()
        db.session.delete(l9_sk)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l9_sci

@app.route("/delete/l9_sci/<string:sno>", methods = ['GET', 'POST'])
def delete_l9_sci(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l9_sci = L9_sci.query.filter_by(sno=sno).first()
        db.session.delete(l9_sci)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l10

@app.route("/delete/l10/<string:sno>", methods = ['GET', 'POST'])
def delete_l10(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l10 = L10.query.filter_by(sno=sno).first()
        db.session.delete(l10)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l10_sk

@app.route("/delete/l10_sk/<string:sno>", methods = ['GET', 'POST'])
def delete_l10_sk(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l10_sk = L10_sk.query.filter_by(sno=sno).first()
        db.session.delete(l10_sk)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l10_ss

@app.route("/delete/l10_ss/<string:sno>", methods = ['GET', 'POST'])
def delete_l10_ss(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l10_ss = L10_ss.query.filter_by(sno=sno).first()
        db.session.delete(l10_ss)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l10_sci

@app.route("/delete/l10_sci/<string:sno>", methods = ['GET', 'POST'])
def delete_l10_sci(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l10_sci = L10_sci.query.filter_by(sno=sno).first()
        db.session.delete(l10_sci)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l10_guj

@app.route("/delete/l10_guj/<string:sno>", methods = ['GET', 'POST'])
def delete_l10_guj(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l10_guj = L10_guj.query.filter_by(sno=sno).first()
        db.session.delete(l10_guj)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l10_eng

@app.route("/delete/l10_eng/<string:sno>", methods = ['GET', 'POST'])
def delete_l10_eng(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l10_eng = L10_eng.query.filter_by(sno=sno).first()
        db.session.delete(l10_eng)
        db.session.commit()
    return redirect('/dashboard')


# deleting point for l11

@app.route("/delete/l11/<string:sno>", methods = ['GET', 'POST'])
def delete_l11(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l11 = L11.query.filter_by(sno=sno).first()
        db.session.delete(l11)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l11_phy

@app.route("/delete/l11_phy/<string:sno>", methods = ['GET', 'POST'])
def delete_l11_phy(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l11_phy = L11_phy.query.filter_by(sno=sno).first()
        db.session.delete(l11_phy)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l11_chem

@app.route("/delete/l11_chem/<string:sno>", methods = ['GET', 'POST'])
def delete_l11_chem(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l11_chem = L11_chem.query.filter_by(sno=sno).first()
        db.session.delete(l11_chem)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l11_eng

@app.route("/delete/l11_eng/<string:sno>", methods = ['GET', 'POST'])
def delete_l11_eng(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l11_eng = L11_eng.query.filter_by(sno=sno).first()
        db.session.delete(l11_eng)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l12

@app.route("/delete/l12/<string:sno>", methods = ['GET', 'POST'])
def delete_l12(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l12 = L12.query.filter_by(sno=sno).first()
        db.session.delete(l12)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l12_phy

@app.route("/delete/l12_phy/<string:sno>", methods = ['GET', 'POST'])
def delete_l12_phy(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l12_phy = L12_phy.query.filter_by(sno=sno).first()
        db.session.delete(l12_phy)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l12_chem

@app.route("/delete/l12_chem/<string:sno>", methods = ['GET', 'POST'])
def delete_l12_chem(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l12_chem = L12_chem.query.filter_by(sno=sno).first()
        db.session.delete(l12_chem)
        db.session.commit()
    return redirect('/dashboard')

# deleting point for l12_eng

@app.route("/delete/l12_eng/<string:sno>", methods = ['GET', 'POST'])
def delete_l12_eng(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        l12_chem_eng = L12_eng.query.filter_by(sno=sno).first()
        db.session.delete(l12_eng)
        db.session.commit()
    return redirect('/dashboard')

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == 'POST':
        scroll_notice = request.form.get('scroll_notice')
        date = datetime.now()
        scroll = Scroll(scroll_notice=scroll_notice, date=datetime.now())
        db.session.add(scroll)
        db.session.commit()
    scroll = Scroll.query.filter_by().all()
    return render_template('index.html', params=params, scroll=scroll)

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        query = request.form.get('query')

        entry = Contacts(name=name, query=query, email=email, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('(from govt. trial website)New message from: ' + name,
                          recipients = [params['mail-id']],
                          sender=email,
                          body=query + '. Mobile no is:' + email
                          )    
    return  render_template('contact.html', params=params)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if ('user' in session and session['user'] == params['admin_user']):
        notice = Notice.query.all()
        scroll = Scroll.query.all()
        principal = Principal.query.all()
        teacher = Teacher.query.all()
        clerk = Clerk.query.all()
        other = Other.query.all()
        s9 = S9.query.all()
        s10 = S10.query.all()
        s11 = S11.query.all()
        s12 = S12.query.all()
        l9 = L9.query.all()
        l11 = L11.query.all()
        l11_phy = L11_phy.query.all()
        l11_chem = L11_chem.query.all()
        l11_eng = L11_eng.query.all()
        l12 = L12.query.all()
        l12_phy = L12_phy.query.all()
        l12_chem = L12_chem.query.all()
        l12_eng = L12_eng.query.all()
        l10 = L10.query.all()
        l10_sk = L10_sk.query.all()
        l10_ss = L10_ss.query.all()
        l10_sci = L10_sci.query.all()
        l10_guj = L10_guj.query.all()
        l10_eng = L10_eng.query.all()
        l9 = L9.query.all()
        l9_sk = L9_sk.query.all()
        l9_ss = L9_ss.query.all()
        l9_sci = L9_sci.query.all()
        l9_guj = L9_guj.query.all()
        l9_eng = L9_eng.query.all()
        l9_hindi = L9_hindi.query.all()
        return render_template('dashboard.html', params=params, notice=notice, scroll=scroll, principal=principal, teacher=teacher, clerk=clerk, other=other, s9=s9, s10=s10, s11=s11, s12=s12, l11=l11, l11_chem=l11_chem, l11_phy=l11_phy, l11_eng=l11_eng, l12=l12, l12_chem=l12_chem, l12_phy=l12_phy, l12_eng=l12_eng, l10=l10, l10_ss=l10_ss, l10_sk=l10_sk, l10_sci=l10_sci, l10_guj=l10_guj, l10_eng=l10_eng, l9=l9, l9_ss=l9_ss, l9_sk=l9_sk, l9_sci=l9_sci, l9_guj=l9_guj, l9_eng=l9_eng, l9_hindi=l9_hindi)


    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username==params['admin_user'] and userpass==params['admin_password']):
            session['user'] = username
            notice = Notice.query.all()
            return render_template('dashboard.html', params=params, notice=notice)
        else:
            return "please enter the valid username or password"


    
    return render_template('login.html', params=params)


@app.route("/edit/<string:sno>", methods=["GET","POST"])
def edit(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                box_title = request.form.get('title')
                category = request.form.get('category')
                content = request.form.get('content')
                img_file = request.form.get('img_file')
                slug = request.form.get('slug')
                date = datetime.now()

                if sno == '0':
                    notice = Notice(category=category, title=box_title, content=content, slug=slug, img_file=img_file)
                    db.session.add(notice)
                    db.session.commit()

                else:
                    notice = Notice.query.filter_by(sno=sno).first()
                    notice.title = box_title
                    notice.category = category
                    notice.content = content
                    notice.img_file = img_file
                    notice.slug = slug
                    notice.date = date
                    db.session.commit()
                    return redirect('/edit/'+sno)


            notice = Notice.query.filter_by(sno=sno).first()
            return render_template('edit.html', params=params, notice=notice, sno=sno)

# make here edit section for the scrolling notices

@app.route("/edit/scroll/<string:sno>", methods=["GET","POST"])
def edit_scroll(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                scroll_notice = request.form.get('scroll_notice')
                date = datetime.now()

                if sno == '0':
                    scroll = Scroll(scroll_notice=scroll_notice, date=date)
                    db.session.add(scroll)
                    db.session.commit()

                else:
                    scroll = Scroll.query.filter_by(sno=sno).first()
                    scroll.scroll_notice = scroll_notice
                    scroll.date = date
                    db.session.commit()
                    return redirect('/edit/scroll/'+sno)


            scroll = Scroll.query.filter_by(sno=sno).first()
            return render_template('edit_scroll.html', params=params, scroll=scroll, sno=sno)

# make the edit section for the principal

@app.route("/edit/principal/<string:sno>", methods=["GET","POST"])
def edit_principal(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                info = request.form.get('info')
                img_file = request.form.get('img_file')

                if sno == '0':
                    principal = Principal(name=name, info=info, img_file=img_file)
                    db.session.add(principal)
                    db.session.commit()

                else:
                    principal = Principal.query.filter_by(sno=sno).first()
                    principal.name = name
                    principal.info = info
                    principal.img_file = img_file
                    db.session.commit()
                    return redirect('/edit/principal/'+sno)


            principal = Principal.query.filter_by(sno=sno).first()
            return render_template('edit_principal.html', params=params, principal=principal, sno=sno)

# edit section for the teacher

@app.route("/edit/teacher/<string:sno>", methods=["GET","POST"])
def edit_teacher(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                info = request.form.get('info')
                img_file = request.form.get('img_file')
                role = request.form.get('role')

                if sno == '0':
                    teacher = Teacher(name=name, info=info, img_file=img_file, role=role)
                    db.session.add(teacher)
                    db.session.commit()

                else:
                    teacher = Teacher.query.filter_by(sno=sno).first()
                    teacher.name = name
                    teacher.info = info
                    teacher.img_file = img_file
                    teacher.role = role
                    db.session.commit()
                    return redirect('/edit/teacher/'+sno)


            teacher = Teacher.query.filter_by(sno=sno).first()
            return render_template('edit_teacher.html', params=params, teacher=teacher, sno=sno)

# edit section for the clerk

@app.route("/edit/clerk/<string:sno>", methods=["GET","POST"])
def edit_clerk(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                info = request.form.get('info')
                img_file = request.form.get('img_file')
                role = request.form.get('role')

                if sno == '0':
                    clerk = Clerk(name=name, info=info, img_file=img_file, role=role)
                    db.session.add(clerk)
                    db.session.commit()

                else:
                    clerk = Clerk.query.filter_by(sno=sno).first()
                    clerk.name = name
                    clerk.info = info
                    clerk.img_file = img_file
                    clerk.role = role
                    db.session.commit()
                    return redirect('/edit/clerk/'+sno)


            clerk = Clerk.query.filter_by(sno=sno).first()
            return render_template('edit_clerk.html', params=params, clerk=clerk, sno=sno)

# edit section for the other

@app.route("/edit/other-staff/<string:sno>", methods=["GET","POST"])
def edit_other(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                info = request.form.get('info')
                img_file = request.form.get('img_file')
                role = request.form.get('role')

                if sno == '0':
                    other = Other(name=name, info=info, img_file=img_file, role=role)
                    db.session.add(other)
                    db.session.commit()

                else:
                    other = Other.query.filter_by(sno=sno).first()
                    other.name = name
                    other.role = role
                    other.info = info
                    other.img_file = img_file
                    db.session.commit()
                    return redirect('/edit/other-saff/'+sno)


            other = Other.query.filter_by(sno=sno).first()
            return render_template('edit_otherstaff.html', params=params, other=other, sno=sno)

# edit section for the s9

@app.route("/edit/s9/<string:sno>", methods=["GET","POST"])
def edit_s9(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')

                if sno == '0':
                    s9 = S9(name=name, decr=decr)
                    db.session.add(s9)
                    db.session.commit()

                else:
                    s9 = S9.query.filter_by(sno=sno).first()
                    s9.name = name
                    s9.decr = decr
                    db.session.commit()
                    return redirect('/edit/s9/'+sno)

            s9 = S9.query.filter_by(sno=sno).first()
            return render_template('edit_s9.html', params=params, s9=s9, sno=sno)

# edit section for the s10

@app.route("/edit/s10/<string:sno>", methods=["GET","POST"])
def edit_s10(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')

                if sno == '0':
                    s10 = S10(name=name, decr=decr)
                    db.session.add(s10)
                    db.session.commit()

                else:
                    s10 = S10.query.filter_by(sno=sno).first()
                    s10.name = name
                    s10.decr = decr
                    db.session.commit()
                    return redirect('/edit/s10/'+sno)

            s10 = S10.query.filter_by(sno=sno).first()
            return render_template('edit_s10.html', params=params, s10=s10, sno=sno)

# edit section for the s11

@app.route("/edit/s11/<string:sno>", methods=["GET","POST"])
def edit_s11(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')

                if sno == '0':
                    s11 = S11(name=name, decr=decr)
                    db.session.add(s11)
                    db.session.commit()

                else:
                    s11 = S11.query.filter_by(sno=sno).first()
                    s11.name = name
                    s11.decr = decr
                    db.session.commit()
                    return redirect('/edit/s11/'+sno)

            s11 = S11.query.filter_by(sno=sno).first()
            return render_template('edit_s11.html', params=params, s11=s11, sno=sno)


# edit section for the s12

@app.route("/edit/s12/<string:sno>", methods=["GET","POST"])
def edit_s12(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')

                if sno == '0':
                    s12 = S12(name=name, decr=decr)
                    db.session.add(s12)
                    db.session.commit()

                else:
                    s12 = S12.query.filter_by(sno=sno).first()
                    s12.name = name
                    s12.decr = decr
                    db.session.commit()
                    return redirect('/edit/s12/'+sno)

            s12 = S12.query.filter_by(sno=sno).first()
            return render_template('edit_s12.html', params=params, s12=s12, sno=sno)


# edit section for the l9

@app.route("/edit/l9/<string:sno>", methods=["GET","POST"])
def edit_l9(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9 = L9(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9)
                    db.session.commit()

                else:
                    l9 = L9.query.filter_by(sno=sno).first()
                    l9.name = name
                    l9.decr = decr
                    l9.pdf_decr1 = pdf_decr1
                    l9.pdf_file1 = pdf_file1
                    l9.pdf_decr2 = pdf_decr2
                    l9.pdf_file2 = pdf_file2
                    l9.pdf_decr3 = pdf_decr3
                    l9.pdf_file3 = pdf_file3
                    l9.video_decr1 = video_decr1
                    l9.video_file1 = video_file1
                    l9.video_decr2 = video_decr2
                    l9.video_file2 = video_file2
                    l9.video_decr3 = video_decr3
                    l9.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9/'+sno)

            l9 = L9.query.filter_by(sno=sno).first()
            return render_template('edit_l9.html', params=params, l9=l9, sno=sno)



# edit section for the l9_sk

@app.route("/edit/l9_sk/<string:sno>", methods=["GET","POST"])
def edit_l9_sk(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9_sk = L9_sk(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9_sk)
                    db.session.commit()

                else:
                    l9_sk = L9_sk.query.filter_by(sno=sno).first()
                    l9_sk.name = name
                    l9_sk.decr = decr
                    l9_sk.pdf_decr1 = pdf_decr1
                    l9_sk.pdf_file1 = pdf_file1
                    l9_sk.pdf_decr2 = pdf_decr2
                    l9_sk.pdf_file2 = pdf_file2
                    l9_sk.pdf_decr3 = pdf_decr3
                    l9_sk.pdf_file3 = pdf_file3
                    l9_sk.video_decr1 = video_decr1
                    l9_sk.video_file1 = video_file1
                    l9_sk.video_decr2 = video_decr2
                    l9_sk.video_file2 = video_file2
                    l9_sk.video_decr3 = video_decr3
                    l9_sk.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9_sk/'+sno)

            l9_sk = L9_sk.query.filter_by(sno=sno).first()
            return render_template('edit_l9_sk.html', params=params, l9_sk=l9_sk, sno=sno)


# edit section for the l9_ss

@app.route("/edit/l9_ss/<string:sno>", methods=["GET","POST"])
def edit_l9_ss(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9_ss = L9_ss(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9_ss)
                    db.session.commit()

                else:
                    l9_ss = L9_ss.query.filter_by(sno=sno).first()
                    l9_ss.name = name
                    l9_ss.decr = decr
                    l9_ss.pdf_decr1 = pdf_decr1
                    l9_ss.pdf_file1 = pdf_file1
                    l9_ss.pdf_decr2 = pdf_decr2
                    l9_ss.pdf_file2 = pdf_file2
                    l9_ss.pdf_decr3 = pdf_decr3
                    l9_ss.pdf_file3 = pdf_file3
                    l9_ss.video_decr1 = video_decr1
                    l9_ss.video_file1 = video_file1
                    l9_ss.video_decr2 = video_decr2
                    l9_ss.video_file2 = video_file2
                    l9_ss.video_decr3 = video_decr3
                    l9_ss.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9_ss/'+sno)

            l9_ss = L9_ss.query.filter_by(sno=sno).first()
            return render_template('edit_l9_ss.html', params=params, l9_ss=l9_ss, sno=sno)

# edit section for the l9_sci

@app.route("/edit/l9_sci/<string:sno>", methods=["GET","POST"])
def edit_l9_sci(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9_sci = L9_sci(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9_sci)
                    db.session.commit()

                else:
                    l9_sci = L9_sci.query.filter_by(sno=sno).first()
                    l9_sci.name = name
                    l9_sci.decr = decr
                    l9_sci.pdf_decr1 = pdf_decr1
                    l9_sci.pdf_file1 = pdf_file1
                    l9_sci.pdf_decr2 = pdf_decr2
                    l9_sci.pdf_file2 = pdf_file2
                    l9_sci.pdf_decr3 = pdf_decr3
                    l9_sci.pdf_file3 = pdf_file3
                    l9_sci.video_decr1 = video_decr1
                    l9_sci.video_file1 = video_file1
                    l9_sci.video_decr2 = video_decr2
                    l9_sci.video_file2 = video_file2
                    l9_sci.video_decr3 = video_decr3
                    l9_sci.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9_sci/'+sno)

            l9_sci = L9_sci.query.filter_by(sno=sno).first()
            return render_template('edit_l9_sci.html', params=params, l9_sci=l9_sci, sno=sno)


# edit section for the l9_guj

@app.route("/edit/l9_guj/<string:sno>", methods=["GET","POST"])
def edit_l9_guj(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9_guj = L9_guj(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9_guj)
                    db.session.commit()

                else:
                    l9_guj = L9_guj.query.filter_by(sno=sno).first()
                    l9_guj.name = name
                    l9_guj.decr = decr
                    l9_guj.pdf_decr1 = pdf_decr1
                    l9_guj.pdf_file1 = pdf_file1
                    l9_guj.pdf_decr2 = pdf_decr2
                    l9_guj.pdf_file2 = pdf_file2
                    l9_guj.pdf_decr3 = pdf_decr3
                    l9_guj.pdf_file3 = pdf_file3
                    l9_guj.video_decr1 = video_decr1
                    l9_guj.video_file1 = video_file1
                    l9_guj.video_decr2 = video_decr2
                    l9_guj.video_file2 = video_file2
                    l9_guj.video_decr3 = video_decr3
                    l9_guj.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9_guj/'+sno)

            l9_guj = L9_guj.query.filter_by(sno=sno).first()
            return render_template('edit_l9_guj.html', params=params, l9_guj=l9_guj, sno=sno)

# edit section for the l9_eng

@app.route("/edit/l9_eng/<string:sno>", methods=["GET","POST"])
def edit_l9_eng(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9_eng = L9_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9_eng)
                    db.session.commit()

                else:
                    l9_eng = L9_eng.query.filter_by(sno=sno).first()
                    l9_eng.name = name
                    l9_eng.decr = decr
                    l9_eng.pdf_decr1 = pdf_decr1
                    l9_eng.pdf_file1 = pdf_file1
                    l9_eng.pdf_decr2 = pdf_decr2
                    l9_eng.pdf_file2 = pdf_file2
                    l9_eng.pdf_decr3 = pdf_decr3
                    l9_eng.pdf_file3 = pdf_file3
                    l9_eng.video_decr1 = video_decr1
                    l9_eng.video_file1 = video_file1
                    l9_eng.video_decr2 = video_decr2
                    l9_eng.video_file2 = video_file2
                    l9_eng.video_decr3 = video_decr3
                    l9_eng.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9_eng/'+sno)

            l9_eng = L9_eng.query.filter_by(sno=sno).first()
            return render_template('edit_l9_eng.html', params=params, l9_eng=l9_eng, sno=sno)

# edit section for the l9_hindi

@app.route("/edit/l9_hindi/<string:sno>", methods=["GET","POST"])
def edit_l9_hindi(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l9_hindi = L9_hindi(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l9_hindi)
                    db.session.commit()

                else:
                    l9_hindi = L9_hindi.query.filter_by(sno=sno).first()
                    l9_hindi.name = name
                    l9_hindi.decr = decr
                    l9_hindi.pdf_decr1 = pdf_decr1
                    l9_hindi.pdf_file1 = pdf_file1
                    l9_hindi.pdf_decr2 = pdf_decr2
                    l9_hindi.pdf_file2 = pdf_file2
                    l9_hindi.pdf_decr3 = pdf_decr3
                    l9_hindi.pdf_file3 = pdf_file3
                    l9_hindi.video_decr1 = video_decr1
                    l9_hindi.video_file1 = video_file1
                    l9_hindi.video_decr2 = video_decr2
                    l9_hindi.video_file2 = video_file2
                    l9_hindi.video_decr3 = video_decr3
                    l9_hindi.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l9_hindi/'+sno)

            l9_hindi = L9_hindi.query.filter_by(sno=sno).first()
            return render_template('edit_l9_hindi.html', params=params, l9_hindi=l9_hindi, sno=sno)



# edit section for the l10

@app.route("/edit/l10/<string:sno>", methods=["GET","POST"])
def edit_l10(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l10 = L10(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l10)
                    db.session.commit()

                else:
                    l10 = L10.query.filter_by(sno=sno).first()
                    l10.name = name
                    l10.decr = decr
                    l10.pdf_decr1 = pdf_decr1
                    l10.pdf_file1 = pdf_file1
                    l10.pdf_decr2 = pdf_decr2
                    l10.pdf_file2 = pdf_file2
                    l10.pdf_decr3 = pdf_decr3
                    l10.pdf_file3 = pdf_file3
                    l10.video_decr1 = video_decr1
                    l10.video_file1 = video_file1
                    l10.video_decr2 = video_decr2
                    l10.video_file2 = video_file2
                    l10.video_decr3 = video_decr3
                    l10.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l10/'+sno)

            l10 = L10.query.filter_by(sno=sno).first()
            return render_template('edit_l10.html', params=params, l10=l10, sno=sno)


# edit section for the l10_sk

@app.route("/edit/l10_sk/<string:sno>", methods=["GET","POST"])
def edit_l10_sk(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l10_sk = L10_sk(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l10_sk)
                    db.session.commit()

                else:
                    l10_sk = L10_sk.query.filter_by(sno=sno).first()
                    l10_sk.name = name
                    l10_sk.decr = decr
                    l10_sk.pdf_decr1 = pdf_decr1
                    l10_sk.pdf_file1 = pdf_file1
                    l10_sk.pdf_decr2 = pdf_decr2
                    l10_sk.pdf_file2 = pdf_file2
                    l10_sk.pdf_decr3 = pdf_decr3
                    l10_sk.pdf_file3 = pdf_file3
                    l10_sk.video_decr1 = video_decr1
                    l10_sk.video_file1 = video_file1
                    l10_sk.video_decr2 = video_decr2
                    l10_sk.video_file2 = video_file2
                    l10_sk.video_decr3 = video_decr3
                    l10_sk.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l10_sk/'+sno)

            l10_sk = L10_sk.query.filter_by(sno=sno).first()
            return render_template('edit_l10_sk.html', params=params, l10_sk=l10_sk, sno=sno)


# edit section for the l10_ss

@app.route("/edit/l10_ss/<string:sno>", methods=["GET","POST"])
def edit_l10_ss(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l10_ss = L10_ss(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l10_ss)
                    db.session.commit()

                else:
                    l10_ss = L10_ss.query.filter_by(sno=sno).first()
                    l10_ss.name = name
                    l10_ss.decr = decr
                    l10_ss.pdf_decr1 = pdf_decr1
                    l10_ss.pdf_file1 = pdf_file1
                    l10_ss.pdf_decr2 = pdf_decr2
                    l10_ss.pdf_file2 = pdf_file2
                    l10_ss.pdf_decr3 = pdf_decr3
                    l10_ss.pdf_file3 = pdf_file3
                    l10_ss.video_decr1 = video_decr1
                    l10_ss.video_file1 = video_file1
                    l10_ss.video_decr2 = video_decr2
                    l10_ss.video_file2 = video_file2
                    l10_ss.video_decr3 = video_decr3
                    l10_ss.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l10_ss/'+sno)

            l10_ss = L10_ss.query.filter_by(sno=sno).first()
            return render_template('edit_l10_ss.html', params=params, l10_ss=l10_ss, sno=sno)

# edit section for the l10_sci

@app.route("/edit/l10_sci/<string:sno>", methods=["GET","POST"])
def edit_l10_sci(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l10_sci = L10_sci(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l10_sci)
                    db.session.commit()

                else:
                    l10_sci = L10_sci.query.filter_by(sno=sno).first()
                    l10_sci.name = name
                    l10_sci.decr = decr
                    l10_sci.pdf_decr1 = pdf_decr1
                    l10_sci.pdf_file1 = pdf_file1
                    l10_sci.pdf_decr2 = pdf_decr2
                    l10_sci.pdf_file2 = pdf_file2
                    l10_sci.pdf_decr3 = pdf_decr3
                    l10_sci.pdf_file3 = pdf_file3
                    l10_sci.video_decr1 = video_decr1
                    l10_sci.video_file1 = video_file1
                    l10_sci.video_decr2 = video_decr2
                    l10_sci.video_file2 = video_file2
                    l10_sci.video_decr3 = video_decr3
                    l10_sci.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l10_sci/'+sno)

            l10_sci = L10_sci.query.filter_by(sno=sno).first()
            return render_template('edit_l10_sci.html', params=params, l10_sci=l10_sci, sno=sno)


# edit section for the l10_guj

@app.route("/edit/l10_guj/<string:sno>", methods=["GET","POST"])
def edit_l10_guj(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l10_guj = L10_guj(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l10_guj)
                    db.session.commit()

                else:
                    l10_guj = L10_guj.query.filter_by(sno=sno).first()
                    l10_guj.name = name
                    l10_guj.decr = decr
                    l10_guj.pdf_decr1 = pdf_decr1
                    l10_guj.pdf_file1 = pdf_file1
                    l10_guj.pdf_decr2 = pdf_decr2
                    l10_guj.pdf_file2 = pdf_file2
                    l10_guj.pdf_decr3 = pdf_decr3
                    l10_guj.pdf_file3 = pdf_file3
                    l10_guj.video_decr1 = video_decr1
                    l10_guj.video_file1 = video_file1
                    l10_guj.video_decr2 = video_decr2
                    l10_guj.video_file2 = video_file2
                    l10_guj.video_decr3 = video_decr3
                    l10_guj.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l10_guj/'+sno)

            l10_guj = L10_guj.query.filter_by(sno=sno).first()
            return render_template('edit_l10_guj.html', params=params, l10_guj=l10_guj, sno=sno)

# edit section for the l10_eng

@app.route("/edit/l10_eng/<string:sno>", methods=["GET","POST"])
def edit_l10_eng(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l10_eng = L10_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l10_eng)
                    db.session.commit()

                else:
                    l10_eng = L10_eng.query.filter_by(sno=sno).first()
                    l10_eng.name = name
                    l10_eng.decr = decr
                    l10_eng.pdf_decr1 = pdf_decr1
                    l10_eng.pdf_file1 = pdf_file1
                    l10_eng.pdf_decr2 = pdf_decr2
                    l10_eng.pdf_file2 = pdf_file2
                    l10_eng.pdf_decr3 = pdf_decr3
                    l10_eng.pdf_file3 = pdf_file3
                    l10_eng.video_decr1 = video_decr1
                    l10_eng.video_file1 = video_file1
                    l10_eng.video_decr2 = video_decr2
                    l10_eng.video_file2 = video_file2
                    l10_eng.video_decr3 = video_decr3
                    l10_eng.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l10_eng/'+sno)

            l10_eng = L10_eng.query.filter_by(sno=sno).first()
            return render_template('edit_l10_eng.html', params=params, l10_eng=l10_eng, sno=sno)


# edit section for the l11

@app.route("/edit/l11/<string:sno>", methods=["GET","POST"])
def edit_l11(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l11 = L11(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l11)
                    db.session.commit()

                else:
                    l11 = L11.query.filter_by(sno=sno).first()
                    l11.name = name
                    l11.decr = decr
                    l11.pdf_decr1 = pdf_decr1
                    l11.pdf_file1 = pdf_file1
                    l11.pdf_decr2 = pdf_decr2
                    l11.pdf_file2 = pdf_file2
                    l11.pdf_decr3 = pdf_decr3
                    l11.pdf_file3 = pdf_file3
                    l11.video_decr1 = video_decr1
                    l11.video_file1 = video_file1
                    l11.video_decr2 = video_decr2
                    l11.video_file2 = video_file2
                    l11.video_decr3 = video_decr3
                    l11.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l11/'+sno)

            l11 = L11.query.filter_by(sno=sno).first()
            return render_template('edit_l11.html', params=params, l11=l11, sno=sno)


# edit section for the l11_chem

@app.route("/edit/l11_chem/<string:sno>", methods=["GET","POST"])
def edit_l11_chem(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l11_chem = L11_chem(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l11_chem)
                    db.session.commit()

                else:
                    l11_chem = L11_chem.query.filter_by(sno=sno).first()
                    l11_chem.name = name
                    l11_chem.decr = decr
                    l11_chem.pdf_decr1 = pdf_decr1
                    l11_chem.pdf_file1 = pdf_file1
                    l11_chem.pdf_decr2 = pdf_decr2
                    l11_chem.pdf_file2 = pdf_file2
                    l11_chem.pdf_decr3 = pdf_decr3
                    l11_chem.pdf_file3 = pdf_file3
                    l11_chem.video_decr1 = video_decr1
                    l11_chem.video_file1 = video_file1
                    l11_chem.video_decr2 = video_decr2
                    l11_chem.video_file2 = video_file2
                    l11_chem.video_decr3 = video_decr3
                    l11_chem.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l11_chem/'+sno)

            l11_chem = L11_chem.query.filter_by(sno=sno).first()
            return render_template('edit_l11_chem.html', params=params, l11_chem=l11_chem, sno=sno)


# edit section for the l11_phy

@app.route("/edit/l11_phy/<string:sno>", methods=["GET","POST"])
def edit_l11_phy(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l11_phy = L11_phy(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l11_phy)
                    db.session.commit()

                else:
                    l11_phy = L11_phy.query.filter_by(sno=sno).first()
                    l11_phy.name = name
                    l11_phy.decr = decr
                    l11_phy.pdf_decr1 = pdf_decr1
                    l11_phy.pdf_file1 = pdf_file1
                    l11_phy.pdf_decr2 = pdf_decr2
                    l11_phy.pdf_file2 = pdf_file2
                    l11_phy.pdf_decr3 = pdf_decr3
                    l11_phy.pdf_file3 = pdf_file3
                    l11_phy.video_decr1 = video_decr1
                    l11_phy.video_file1 = video_file1
                    l11_phy.video_decr2 = video_decr2
                    l11_phy.video_file2 = video_file2
                    l11_phy.video_decr3 = video_decr3
                    l11_phy.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l11_phy/'+sno)

            l11_phy = L11_phy.query.filter_by(sno=sno).first()
            return render_template('edit_l11_phy.html', params=params, l11_phy=l11_phy, sno=sno)


# edit section for the l11_eng

@app.route("/edit/l11_eng/<string:sno>", methods=["GET","POST"])
def edit_l11_eng(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l11_eng = L11_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l11_eng)
                    db.session.commit()

                else:
                    l11_eng = L11_eng.query.filter_by(sno=sno).first()
                    l11_eng.name = name
                    l11_eng.decr = decr
                    l11_eng.pdf_decr1 = pdf_decr1
                    l11_eng.pdf_file1 = pdf_file1
                    l11_eng.pdf_decr2 = pdf_decr2
                    l11_eng.pdf_file2 = pdf_file2
                    l11_eng.pdf_decr3 = pdf_decr3
                    l11_eng.pdf_file3 = pdf_file3
                    l11_eng.video_decr1 = video_decr1
                    l11_eng.video_file1 = video_file1
                    l11_eng.video_decr2 = video_decr2
                    l11_eng.video_file2 = video_file2
                    l11_eng.video_decr3 = video_decr3
                    l11_eng.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l11_eng/'+sno)

            l11_eng = L11_eng.query.filter_by(sno=sno).first()
            return render_template('edit_l11_eng.html', params=params, l11_eng=l11_eng, sno=sno)



# edit section for the l12

@app.route("/edit/l12/<string:sno>", methods=["GET","POST"])
def edit_l12(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l12 = L12(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l12)
                    db.session.commit()

                else:
                    l12 = L12.query.filter_by(sno=sno).first()
                    l12.name = name
                    l12.decr = decr
                    l12.pdf_decr1 = pdf_decr1
                    l12.pdf_file1 = pdf_file1
                    l12.pdf_decr2 = pdf_decr2
                    l12.pdf_file2 = pdf_file2
                    l12.pdf_decr3 = pdf_decr3
                    l12.pdf_file3 = pdf_file3
                    l12.video_decr1 = video_decr1
                    l12.video_file1 = video_file1
                    l12.video_decr2 = video_decr2
                    l12.video_file2 = video_file2
                    l12.video_decr3 = video_decr3
                    l12.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l12/'+sno)

            l12 = L12.query.filter_by(sno=sno).first()
            return render_template('edit_l12.html', params=params, l12=l12, sno=sno)


# edit section for the l12_chem

@app.route("/edit/l12_chem/<string:sno>", methods=["GET","POST"])
def edit_l12_chem(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l12_chem = L12_chem(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l12_chem)
                    db.session.commit()

                else:
                    l12_chem = L12_chem.query.filter_by(sno=sno).first()
                    l12_chem.name = name
                    l12_chem.decr = decr
                    l12_chem.pdf_decr1 = pdf_decr1
                    l12_chem.pdf_file1 = pdf_file1
                    l12_chem.pdf_decr2 = pdf_decr2
                    l12_chem.pdf_file2 = pdf_file2
                    l12_chem.pdf_decr3 = pdf_decr3
                    l12_chem.pdf_file3 = pdf_file3
                    l12_chem.video_decr1 = video_decr1
                    l12_chem.video_file1 = video_file1
                    l12_chem.video_decr2 = video_decr2
                    l12_chem.video_file2 = video_file2
                    l12_chem.video_decr3 = video_decr3
                    l12_chem.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l12_chem/'+sno)

            l12_chem = L12_chem.query.filter_by(sno=sno).first()
            return render_template('edit_l12_chem.html', params=params, l12_chem=l12_chem, sno=sno)


# edit section for the l12_phy

@app.route("/edit/l12_phy/<string:sno>", methods=["GET","POST"])
def edit_l12_phy(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l12_phy = L12_phy(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l12_phy)
                    db.session.commit()

                else:
                    l12_phy = L12_phy.query.filter_by(sno=sno).first()
                    l12_phy.name = name
                    l12_phy.decr = decr
                    l12_phy.pdf_decr1 = pdf_decr1
                    l12_phy.pdf_file1 = pdf_file1
                    l12_phy.pdf_decr2 = pdf_decr2
                    l12_phy.pdf_file2 = pdf_file2
                    l12_phy.pdf_decr3 = pdf_decr3
                    l12_phy.pdf_file3 = pdf_file3
                    l12_phy.video_decr1 = video_decr1
                    l12_phy.video_file1 = video_file1
                    l12_phy.video_decr2 = video_decr2
                    l12_phy.video_file2 = video_file2
                    l12_phy.video_decr3 = video_decr3
                    l12_phy.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l12_phy/'+sno)

            l12_phy = L12_phy.query.filter_by(sno=sno).first()
            return render_template('edit_l12_phy.html', params=params, l12_phy=l12_phy, sno=sno)


# edit section for the l12_eng

@app.route("/edit/l12_eng/<string:sno>", methods=["GET","POST"])
def edit_l12_eng(sno):
        if ('user' in session and session['user'] == params['admin_user']):
            if request.method == 'POST':
                name = request.form.get('name')
                decr = request.form.get('decr')
                pdf_decr1 = request.form.get('pdf_decr1') 
                pdf_file1 = request.form.get('pdf_file1')
                pdf_decr2 = request.form.get('pdf_decr2') 
                pdf_file2 = request.form.get('pdf_file2')
                pdf_decr3 = request.form.get('pdf_decr3') 
                pdf_file3 = request.form.get('pdf_file3')
                video_decr1 = request.form.get('video_decr1') 
                video_file1 = request.form.get('video_file1')
                video_decr2 = request.form.get('video_decr2') 
                video_file2 = request.form.get('video_file2')
                video_decr3 = request.form.get('video_decr3') 
                video_file3 = request.form.get('video_file3')

                if sno == '0':
                    l12_eng = L12_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
                    db.session.add(l12_eng)
                    db.session.commit()

                else:
                    l12_eng = L12_eng.query.filter_by(sno=sno).first()
                    l12_eng.name = name
                    l12_eng.decr = decr
                    l12_eng.pdf_decr1 = pdf_decr1
                    l12_eng.pdf_file1 = pdf_file1
                    l12_eng.pdf_decr2 = pdf_decr2
                    l12_eng.pdf_file2 = pdf_file2
                    l12_eng.pdf_decr3 = pdf_decr3
                    l12_eng.pdf_file3 = pdf_file3
                    l12_eng.video_decr1 = video_decr1
                    l12_eng.video_file1 = video_file1
                    l12_eng.video_decr2 = video_decr2
                    l12_eng.video_file2 = video_file2
                    l12_eng.video_decr3 = video_decr3
                    l12_eng.video_file3 = video_file3
                    db.session.commit()
                    return redirect('/edit/l12_eng/'+sno)

            l12_eng = L12_eng.query.filter_by(sno=sno).first()
            return render_template('edit_l12_eng.html', params=params, l12_eng=l12_eng, sno=sno)



@app.route("/staff-info")
def staff():
    return  render_template('staff.html', params=params)

@app.route("/teachers", methods = ["GET", "POST"])
def teachers():
    if request.method == 'POST':
        name = request.form.get('name')
        info = request.form.get('info')
        img_file = request.form.get('img_file')
        role = request.form.get('role')
        teacher = Teacher(name=name, info=info, img_file=img_file, role=role)
        db.session.add(teacher)
        db.session.commit()
    teacher = Teacher.query.filter_by().all()
    return  render_template('teachers.html', params=params, teacher=teacher)

@app.route("/principal", methods=["GET", "POST"])
def principal():
    if request.method == 'POST':
        name = request.form.get('name')
        info = request.form.get('info')
        img_file = request.form.get('img_file')
        principal = Principal(name=name, info=info, img_file=img_file)
        db.session.add(principal)
        db.session.commit()
    principal = Principal.query.filter_by().all()
    return  render_template('principal.html', params=params, principal=principal)

@app.route("/clerks", methods=["GET", "POST"])
def clerks():
    if request.method == 'POST':
        name = request.form.get('name')
        info = request.form.get('info')
        img_file = request.form.get('img_file')
        role = request.form.get('role')
        clerk = Clerk(name=name, info=info, img_file=img_file, role=role)
        db.session.add(clerk)
        db.session.commit()
    clerk = Clerk.query.filter_by().all()
    return  render_template('clerks.html', params=params, clerk=clerk)

@app.route("/other-staff", methods=["GET", "POST"])
def otherstaff():
    if request.method == 'POST':
        name = request.form.get('name')
        info = request.form.get('info')
        img_file = request.form.get('img_file')
        role = request.form.get('role')
        other = Other(name=name, info=info, img_file=img_file, role=role)
        db.session.add(other)
        db.session.commit()
    other = Other.query.filter_by().all()
    return render_template('otherstaff.html', params=params, other=other)


@app.route("/subject-9/list-9/<name>", methods=["GET", "POST"])
def list_9(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9 = L9(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9)
        db.session.commit()
    l9 = L9.query.filter_by().all()
    l9_guj = L9_guj.query.filter_by().all()
    l9_ss = L9_ss.query.filter_by().all()
    l9_sk = L9_sk.query.filter_by().all()
    l9_eng = L9_eng.query.filter_by().all()
    l9_sci = L9_sci.query.filter_by().all()
    l9_hindi = L9_hindi.query.filter_by().all()
    if name == 'Maths':
        return  render_template('list_9.html', params=params, name=name, l9=l9)
    if name == 'Social-Science':
        return render_template('list_9_ss.html', params=params, name=name, l9_ss=l9_ss)
    if name == 'Sanskrit':
        return render_template('list_9_sk.html', params=params, name=name, l9_sk=l9_sk)
    if name == 'Science':
        return render_template('list_9_sci.html', params=params, name=name, l9_sci=l9_sci)
    if name == 'Gujarati':
        return render_template('list_9_guj.html', params=params, name=name, l9_guj=l9_guj)
    if name == 'English':
        return render_template('list_9_eng.html', params=params, name=name, l9_eng=l9_eng)
    if name == 'Hindi':
        return render_template('list_9_hindi.html', params=params, name=name, l9_hindi=l9_hindi)
    else:
        return "Chapters for this subject is not created yet!"
    

@app.route("/subject-9/list-9-ss/<string:name>", methods=["GET", "POST"])
def list_9_ss(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9_ss = L9_ss(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9_ss)
        db.session.commit()
    l9_ss = L9_ss.query.filter_by().all()
    return  render_template('list_9_ss.html', params=params, name=name, l9_ss=l9_ss)

@app.route("/subject-9/list-9-sk/<string:name>", methods=["GET", "POST"])
def list_9_sk(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9_sk = L9_sk(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9_sk)
        db.session.commit()
    l9_sk = L9_sk.query.filter_by().all()
    return  render_template('list_9_sk.html', params=params, name=name, l9_sk=l9_sk)


@app.route("/subject-9/list-9-sci/<string:name>", methods=["GET", "POST"])
def list_9_sci(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9_sci = L9_sci(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9_sci)
        db.session.commit()
    l9_sci = L9_sci.query.filter_by().all()
    return  render_template('list_9_sci.html', params=params, name=name, l9_sci=l9_sci)

@app.route("/subject-9/list-9-guj/<string:name>", methods=["GET", "POST"])
def list_9_guj(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9_guj = L9_guj(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9_guj)
        db.session.commit()
    l9_guj = L9_guj.query.filter_by().all()
    return  render_template('list_9_guj.html', params=params, name=name, l9_guj=l9_guj)


@app.route("/subject-9/list-9-eng/<string:name>", methods=["GET", "POST"])
def list_9_eng(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9_eng = L9_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9_eng)
        db.session.commit()
    l9_eng = L9_eng.query.filter_by().all()
    return  render_template('list_9_eng.html', params=params, name=name, l9_eng=l9_eng)


@app.route("/subject-9/list-9-hindi/<string:name>", methods=["GET", "POST"])
def list_9_hidni(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l9_hindi = L9_hindi(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l9_hindi)
        db.session.commit()
    l9_hindi = L9_hindi.query.filter_by().all()
    return  render_template('list_9_hindi.html', params=params, name=name, l9_hindi=l9_hindi)




@app.route("/subject-10/list-10/<name>", methods=["GET", "POST"])
def list_10(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l10 = L10(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l10)
        db.session.commit()
    l10 = L10.query.filter_by().all()
    l10_guj = L10_guj.query.filter_by().all()
    l10_ss = L10_ss.query.filter_by().all()
    l10_sk = L10_sk.query.filter_by().all()
    l10_eng = L10_eng.query.filter_by().all()
    l10_sci = L10_sci.query.filter_by().all()
    if name == 'Maths':
        return  render_template('list_10.html', params=params, name=name, l10=l10)
    if name == 'Social-Science':
        return render_template('list_10_ss.html', params=params, name=name, l10_ss=l10_ss)
    if name == 'Sanskrit':
        return render_template('list_10_sk.html', params=params, name=name, l10_sk=l10_sk)
    if name == 'Science':
        return render_template('list_10_sci.html', params=params, name=name, l10_sci=l10_sci)
    if name == 'Gujarati':
        return render_template('list_10_guj.html', params=params, name=name, l10_guj=l10_guj)
    if name == 'English':
        return render_template('list_10_eng.html', params=params, name=name, l10_eng=l10_eng)
    else:
        return "Chapters for this subject is not created yet!"

@app.route("/subject-10/list-10-ss/<string:name>", methods=["GET", "POST"])
def list_10_ss(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l10_ss = L10_ss(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l10_ss)
        db.session.commit()
    l10_ss = L10_ss.query.filter_by().all()
    return  render_template('list_10_ss.html', params=params, name=name, l10_ss=l10_ss)

@app.route("/subject-10/list-10-sk/<string:name>", methods=["GET", "POST"])
def list_10_sk(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l10_sk = L10_sk(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l10_sk)
        db.session.commit()
    l10_sk = L10_sk.query.filter_by().all()
    return  render_template('list_10_sk.html', params=params, name=name, l10_sk=l10_sk)


@app.route("/subject-10/list-10-sci/<string:name>", methods=["GET", "POST"])
def list_10_sci(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l10_sci = L10_sci(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l10_sci)
        db.session.commit()
    l10_sci = L10_sci.query.filter_by().all()
    return  render_template('list_10_sci.html', params=params, name=name, l10_sci=l10_sci)

@app.route("/subject-10/list-10-guj/<string:name>", methods=["GET", "POST"])
def list_10_guj(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l10_guj = L10_guj(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l10_guj)
        db.session.commit()
    l10_guj = L10_guj.query.filter_by().all()
    return  render_template('list_10_guj.html', params=params, name=name, l10_guj=l10_guj)


@app.route("/subject-10/list-10-eng/<string:name>", methods=["GET", "POST"])
def list_10_eng(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = requestciform.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l10_eng = L10_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l10_eng)
        db.session.commit()
    l10_eng = L10_eng.query.filter_by().all()
    return  render_template('list_10_eng.html', params=params, name=name, l10_eng=l10_eng)


    
    
    

@app.route("/subject-11/list-11/<name>", methods=["GET", "POST"])
def list_11(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l11 = L11(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l11)
        db.session.commit()
    l11 = L11.query.filter_by().all()
    l11_chem = L11_chem.query.filter_by().all()
    l11_phy = L11_phy.query.filter_by().all()
    l11_eng = L11_eng.query.filter_by().all()
    if name == 'Maths':
        return  render_template('list_11.html', params=params, name=name, l11=l11)
    if name == 'Chemistry':
        return render_template('list_11_chem.html', params=params, name=name, l11_chem=l11_chem)
    if name == 'Physics':
        return render_template('list_11_phy.html', params=params, name=name, l11_phy=l11_phy)
    if name == 'English':
        return render_template('list_11_eng.html', params=params, name=name, l11_eng=l11_eng)
    else:
        return "Chapters for this subject is not created yet!"


@app.route("/subject-11/list-11-chem/<string:name>", methods=["GET", "POST"])
def list_11_chem(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l11_chem = L11_chem(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l11_chem)
        db.session.commit()
    l11_chem = L11_chem.query.filter_by().all()
    return  render_template('list_11_chem.html', params=params, name=name, l11_chem=l11_chem)



@app.route("/subject-11/list-11-phy/<string:name>", methods=["GET", "POST"])
def list_11_phy(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l11_phy = L11_phy(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l11_phy)
        db.session.commit()
    l11_phy = L11_phy.query.filter_by().all()
    return  render_template('list_11_phy.html', params=params, name=name, l11_phy=l11_phy)


@app.route("/subject-11/list-11-eng/<string:name>", methods=["GET", "POST"])
def list_11_eng(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l11_eng = L11_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l11_eng)
        db.session.commit()
    l11_eng = L11_eng.query.filter_by().all()
    return  render_template('list_11_eng.html', params=params, name=name, l11_eng=l11_eng)

    

@app.route("/subject-12/list-12/<name>", methods=["GET", "POST"])
def list_12(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l12 = L12(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l12)
        db.session.commit()
    l12 = L12.query.filter_by().all()
    l12_chem = L12_chem.query.filter_by().all()
    l12_phy = L12_phy.query.filter_by().all()
    l12_eng = L12_eng.query.filter_by().all()
    if name == 'Maths':
        return  render_template('list_12.html', params=params, name=name, l12=l12)
    if name == 'Chemistry':
        return  render_template('list_12_chem.html', params=params, name=name, l12_chem=l12_chem)
    if name == 'Physics':
        return  render_template('list_12_phy.html', params=params, name=name, l12_phy=l12_phy)
    if name == 'English':
        return  render_template('list_12_eng.html', params=params, name=name, l12_eng=l12_eng)
    else:
        return "Chapters for this subject is not created yet!"


@app.route("/subject-12/list-12-chem/<string:name>", methods=["GET", "POST"])
def list_12_chem(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l12_chem = L12_chem(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l12_chem)
        db.session.commit()
    l12_chem = L12_chem.query.filter_by().all()
    return  render_template('list_12_chem.html', params=params, name=name, l12_chem=l12_chem)


@app.route("/subject-12/list-12-phy/<string:name>", methods=["GET", "POST"])
def list_12_phy(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l12_phy = L12_phy(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l12_phy)
        db.session.commit()
    l12_phy = L12_phy.query.filter_by().all()
    return  render_template('list_12_phy.html', params=params, name=name, l12_phy=l12_phy)

@app.route("/subject-12/list-12-eng/<string:name>", methods=["GET", "POST"])
def list_12_eng(name):
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        pdf_decr1 = request.form.get('pdf_decr1') 
        pdf_file1 = request.form.get('pdf_file1')
        pdf_decr2 = request.form.get('pdf_decr2') 
        pdf_file2 = request.form.get('pdf_file2')
        pdf_decr3 = request.form.get('pdf_decr3') 
        pdf_file3 = request.form.get('pdf_file3')
        video_decr1 = request.form.get('video_decr1') 
        video_file1 = request.form.get('video_file1')
        video_decr2 = request.form.get('video_decr2')
        video_file2 = request.form.get('video_file2')
        video_decr3 = request.form.get('video_decr3') 
        video_file3 = request.form.get('video_file3')
        l12_eng = L12_eng(name=name, decr=decr, pdf_decr1=pdf_decr1, pdf_decr2=pdf_decr2, pdf_decr3=pdf_decr3, video_decr1=video_decr1, video_decr2=video_decr2, video_decr3=video_decr3, pdf_file1=pdf_file1, pdf_file2=pdf_file2, pdf_file3=pdf_file3, video_file1=video_file1, video_file2=video_file2, video_file3=video_file3)
        db.session.add(l12_eng)
        db.session.commit()
    l12_eng = L12_eng.query.filter_by().all()
    return  render_template('list_12_eng.html', params=params, name=name, l12_eng=l12_eng)



@app.route("/subject-9", methods=["GET", "POST"])
def subject_9():
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        s9 = S9(name=name, decr=decr)
        db.session.add(s9)
        db.session.commit()
    s9 = S9.query.filter_by().all()
    return  render_template('subject_9.html', params=params, s9=s9)

@app.route("/subject-10", methods=["GET", "POST"])
def subject_10():
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        s10 = S10(name=name, decr=decr)
        db.session.add(s10)
        db.session.commit()
    s10 = S10.query.filter_by().all()
    return  render_template('subject_10.html', params=params, s10=s10)

@app.route("/subject-11", methods=["GET", "POST"])
def subject_11():
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        s11 = S10(name=name, decr=decr)
        db.session.add(s11)
        db.session.commit()
    s11 = S11.query.filter_by().all()
    return  render_template('subject_11.html', params=params, s11=s11)

@app.route("/subject-12", methods=["GET", "POST"])
def subject_12():
    if request.method == 'POST':
        name = request.form.get('name')
        decr = request.form.get('decr')
        s12 = S12(name=name, decr=decr)
        db.session.add(s12)
        db.session.commit()
    s12 = S12.query.filter_by().all()
    return  render_template('subject_12.html', params=params, s12=s12)


@app.route("/standard")
def standard():
    return  render_template('standard.html', params=params)

@app.route("/notice/<string:notice_slug>", methods = ["GET"])
def notice_route(notice_slug):
    notice = Notice.query.filter_by(slug=notice_slug).first()
    return render_template('notice1.html', params=params, notice=notice)


@app.route("/notice-1")
def notice1():
    return  render_template('notice1.html', params=params, notice=notice)

if __name__ == '__main__':
    app.run(debug=True)