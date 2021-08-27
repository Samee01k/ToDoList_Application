from flask import Flask, render_template
import os


def create_app():
    app = Flask("todolist")
    app.config.from_mapping(
        DATABASE="todos"
    )
        
        
    from . import db,todolist
    app.register_blueprint(todolist.bp)    
    
    db.init_app(app)
    
    return app
