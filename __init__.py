from flask import Flask
import os


def create_app():
    app = Flask("todolist")
    app.config.from_mapping(
        DATABASE="todos"
    )
        
    from . import db,todolist,auth
    app.register_blueprint(todolist.bp)    
    app.register_blueprint(auth.bp)
    
    db.init_app(app)
    
    return app
