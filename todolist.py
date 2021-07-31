from flask import Blueprint, g, render_template, url_for, redirect, request
from . import db

bp = Blueprint("todolist","todolist",url_prefix="/")

@bp.route("/")
def index():
	return render_template("todolist/index.html")



#@bp.route("/todolist/")
#def todolist():
    #conn = db.get_db()
    #cursor = conn.cursor()
    #cursor.execute("select * from todolist")
    #todolist = cursor.fetchall()
#    return render_template("todolist/todolist.html")
    
    
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
        print(title)
        desc = request.form.get("desc")
        print(desc)
        status= request.form.get("status")
        cursor.execute("insert into todolist (task, description,status) values (%s,%s,%s)", (title, desc,status))
        conn.commit()
        #return render_template('todolist/todolist.html')
        return redirect(url_for("todolist.todolist"), 302)
