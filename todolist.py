from flask import Blueprint, g, render_template, url_for, redirect, request
from . import db

bp = Blueprint("todolist","todolist",url_prefix="/")

@bp.route("/")
def index():
	return render_template("todolist/index.html")


    
@bp.route('/todolist/', methods=['GET', 'POST'])       
def todolist():
    conn = db.get_db()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("select * from todolist")
        data = cursor.fetchall()
        return render_template('todolist/todolist.html',data=data)
    elif request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        status= request.form.get("status")
        cursor.execute("insert into todolist (task, description,status) values (%s,%s,%s)", (title, description,status))
        conn.commit()
        #return render_template('todolist/todolist.html')
        return redirect(url_for("todolist.todolist"), 302)
        
@bp.route('/delete/<id>/', methods=['POST'])   
def delete(id):
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute("delete from todolist where id=(%s)",(id,))
    conn.commit()
    return redirect(url_for("todolist.todolist"), 302)
    
@bp.route('/update/<id>/',methods=['GET','POST'])
def update(id):
    conn = db.get_db()
    cursor = conn.cursor()
    if request.method == "POST":
        new_title = request.form.get("newtitle")
        new_description = request.form.get("newdescription")
        new_status= request.form.get("newstatus")
        cursor.execute("update todolist set task=%s, description=%s, status=%s where id=%s", (new_title, new_description, new_status, id))
        conn.commit()
        return redirect(url_for("todolist.todolist"), 302)

