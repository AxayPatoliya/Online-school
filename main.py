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
        return render_template('dashboard.html', params=params, notice=notice, scroll=scroll, principal=principal, teacher=teacher, clerk=clerk, other=other, s9=s9, s10=s10, s11=s11, s12=s12, l9=l9)


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


@app.route("/subject-9/list-9/<string:name>", methods=["GET", "POST"])
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
    if name == 'Maths':
        return  render_template('list_9.html', params=params, name=name, l9=l9)   
    elif name=='Chemistry':
        return "This is a Chemistry subject"
    elif name =='Physics':
        return "This is a Physics subject"
    elif name=='English':
        return "This is a English subject"





@app.route("/subject-10/list-10/<string:name>")
def list_10(name):
    return render_template('list_10.html', params=params, name=name)

    
    
    
    

@app.route("/subject-11/list-11/<string:name>")
def list_11(name):
    return  render_template('list_11.html', params=params, name=name)

@app.route("/subject-12/list-12/<string:name>")
def list_12(name):
    return  render_template('list_12.html', params=params, name=name)


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