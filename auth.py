from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from . import db

bp = Blueprint('auth', 'auth',url_prefix="/")

@bp.route("login/", methods=['GET', 'POST'])
def login():
    conn = db.get_db()
    cursor = conn.cursor()
    if request.method == "GET":
        return render_template('todolist/login.html')
    elif request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')
        cursor.execute("select email from users")
        emails = cursor.fetchall()
        emails = [x[0] for x in emails]
        if email in emails:
                cursor.execute("select password, id from users where email = %s", (email,))
                userdata = cursor.fetchone()
                if password == userdata[0]:
                        return redirect(url_for("todolist.todolist", userid=userdata[1]), 302)
                else:
                        alert='Invalid password' 
                        return render_template('todolist/login.html', alert=alert) 
        else:	
                alert='The mail id you entered does not exist!'
                return render_template('todolist/login.html',alert=alert) 
	
	     
@bp.route("signup/", methods=['GET', 'POST'])
def signup():
	conn = db.get_db()
	cursor = conn.cursor()
	if request.method == "GET":
	    return render_template('todolist/signup.html')
	elif request.method == "POST":
	    name = request.form.get('name')
	    email = request.form.get('email')
	    password = request.form.get('password')
	    password2 = request.form.get('password2')
	    remember = request.form.get('remember')
	    cursor.execute("select email from users")
	    emails = cursor.fetchall()
	    emails = [x[0] for x in emails]
	    if email in emails:
	        alert='You already have an account'
	        return render_template('todolist/signup.html',alert=alert)
	    elif password!=password2:
	        alert='Passwords do not match'
	        return render_template('todolist/signup.html',alert=alert)
	    else:
	        cursor.execute("insert into users (name, email, password) values (%s,%s,%s)", (name, email, password))
	        conn.commit()
	        cursor.execute("select id from users where email = %s",(email,))
	        userid = cursor.fetchone()[0]
	        return redirect(url_for("todolist.todolist",userid=userid), 302)
